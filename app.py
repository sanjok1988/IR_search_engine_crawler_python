from flask import Flask, render_template, request, jsonify
from whoosh.index import open_dir
from whoosh import scoring
from whoosh.qparser import QueryParser
import crawler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    # crawler.crawl_and_index()
    query = request.args.get('query', '')
    print(query)
    return searchDocs(query)

def searchDocs(query):
    ix = open_dir(crawler.INDEX_PATH)
    
    # Search the index
    with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
        query_parser = QueryParser("title", ix.schema)
        query = query_parser.parse(query)
        results = searcher.search(query, terms=True)
        
        formatted_results = [{'Title': result['title'],
                      'Authors': result['authors'],
                      'Year': result['year'],
                      'Publication URL': result['publication_url'],
                      'Author Profile URL': result['author_profile_url']}
                     for result in results]
    
        return jsonify(formatted_results)

if __name__ == '__main__':
    app.run(debug=True)
