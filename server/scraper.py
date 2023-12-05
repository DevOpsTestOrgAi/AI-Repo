from flask import Flask, request
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
    # Use Gunicorn as the WSGI server
    from gunicorn import GunicornApplication

    class FlaskApplication(GunicornApplication):
        def init(self, parser, opts, args):
            return {
                'bind': f'0.0.0.0:8080',
                'workers': 1 # Adjust the number of workers based on your needs
            }

    FlaskApplication().run()
