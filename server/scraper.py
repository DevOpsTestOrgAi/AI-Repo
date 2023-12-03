from flask import Flask, request
import requests
from bs4 import BeautifulSoup as Bs

app = Flask(__name__)

def jumia(url):

    try:
        response = requests.get(url)
        print(response)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
        soup = Bs(response.text, 'html.parser')
        wrapBody = soup.find('div', '-df -j-bet')
        cat = soup.find('div','brcbs col16 -pts -pbm')
        category = cat.a.findNext('a').findNext('a').findNext('a').text
        title = wrapBody.find('h1').text
        print(title)
        print(category)
        """save_file"""
        return { "title": title, "category": category}

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

@app.route('/scraper', methods=['GET'])
def handle_request():
    url_param = request.args.get('url', '')
    # return f'OK - Received URL: {url_param}'
    return jumia(url_param)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
