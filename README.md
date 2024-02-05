# Crawler System Documentation

## Overview

The Crawler System is a web scraping application built using Python and Flask. It is designed to crawl a website, extract publication information related to Coventry University's Research Centre for Health and Life Sciences (RCHL), and provide a search interface for users to query the publications.

## Components

### 1. Web Crawler

The web crawler is responsible for fetching data from the Coventry University Research Centre for Health and Life Sciences (RCHL) portal. It uses BeautifulSoup for HTML parsing and extracts information such as publication title, authors, publication year, publication URL, and author profile URL.

### 2. Whoosh Indexing

The Whoosh library is employed to create and manage an index for efficient searching. The extracted publication data is indexed, allowing users to perform searches quickly.

### 3. Flask Web Application

The Flask web application serves as the user interface. It provides a simple search page where users can enter keywords or queries. The search results are displayed in a manner similar to Google Scholar, listing relevant publications from RCHL members.

### 4. Scheduler

The application includes a scheduler using the APScheduler library. The scheduler triggers the web crawler to run periodically, updating the index with the latest publication information. In this setup, the scheduler is configured to run the crawler once per week.

## Usage

1. Clone the repository.

   ```bash
   git clone https://github.com/yourusername/crawler-system.git

### Set up a virtual environment.
python -m venv venv

### Activate the virtual environment.
#### On Windows:

```bash
.\venv\Scripts\activate
```

#### On macOS or Linux:
```bash
source venv/bin/activate
```
#### Install required dependencies.
```bash
pip install -r requirements.txt
````

#### Run the Flask application.
```bash
python app.py
```

#### Access the application in your web browser at http://127.0.0.1:5000/.



