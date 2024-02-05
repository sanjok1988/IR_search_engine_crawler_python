from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

import os
import os.path

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import defaultdict
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import LockError
from itertools import chain

app = Flask(__name__)

# Constant variables
BASE_URL = "https://pureportal.coventry.ac.uk/en/organisations/centre-for-health-and-life-sciences"
INDEX_PATH = "storage"

# Crawler to fetch data from the Coventry University Research Centre for Health and Life Sciences (RCHL) portal
def crawl_and_index():
    # Fetch the page containing the list of publications
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize Whoosh index
    # schema = Schema(title=TEXT(stored=True))
    schema = Schema(title=TEXT(stored=True), authors=TEXT(stored=True), year=ID(stored=True), 
                    publication_url=ID(stored=True, unique=True), author_profile_url=ID(stored=True))
    
    if not os.path.exists(INDEX_PATH):
        os.mkdir(INDEX_PATH)
        
    ix = create_in(INDEX_PATH, schema)
    writer = ix.writer()

    # Extract publication information
    for publication_div in soup.find_all('div', class_='result-container'):
        title_tag = publication_div.find('h3', class_="title")

        if title_tag:
            title = title_tag.get_text(strip = True)
        else:
            title = "N/A"
        
            
        authors_tags = publication_div.find_all('a', class_='link person')
        authors = [author.text.strip() for author in authors_tags] if authors_tags else ["N/A"]


        year_tag = publication_div.find('span', class_='date')
        year = year_tag.text.strip() if year_tag else "N/A"

        publication_url_tag = publication_div.find('a', class_='title')
        publication_url = urljoin(BASE_URL, publication_url_tag['href']) if publication_url_tag else "N/A"

        author_profile_url_tag = publication_div.find('a', class_='link person')
        author_profile_url = urljoin(BASE_URL, author_profile_url_tag['href']) if author_profile_url_tag else "N/A"
        
        # Add data to the Whoosh index
        try:
            writer.add_document(title=title, authors=', '.join(authors), year=year,
                            publication_url=publication_url, author_profile_url=author_profile_url)
            
            # print(title, authors, year, publication_url, author_profile_url)

        except LockError as e:
            print(f"LockError: {e}")
            print("Attempting to clean up lock files...")

            # Manually clean up lock files
            lock_file_path = f"{INDEX_PATH}/write.lock"

            try:
                os.remove(lock_file_path)
                print(f"Lock file {lock_file_path} removed.")
            except Exception as cleanup_error:
                print(f"Error cleaning up lock file: {cleanup_error}")

    # Commit changes to the index
    print("Committing please wait...")
    writer.commit()
    print("Finished")

# Initialize the scheduler
scheduler = BackgroundScheduler(daemon=True)

# Schedule the task to run every week
scheduler.add_job(crawl_and_index, 'interval', weeks=1)

# Start the scheduler
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
