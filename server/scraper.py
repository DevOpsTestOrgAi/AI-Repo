from flask import Flask, request
import requests
from bs4 import BeautifulSoup as Bs

from Jumia import jumia
from ResultScraper import res

app = Flask(__name__)

@app.route('/scraper', methods=['GET'])
def handleScraper():
    url_param = request.args.get('url', '')
    return jumia(url_param)

@app.route('/searcher', methods=['GET'])
def handleSearcher():
    keyword = request.args.get('keyword', '')
    return res(keyword)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
