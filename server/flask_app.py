from flask import Flask, request, jsonify
from gensim.models import Word2Vec
import pandas as pd
from gunicorn_config import *  # Import Gunicorn configuration
from urllib.parse import unquote  # Import the unquote function for URL decoding

app = Flask(__name__)

# Load the Word2Vec model
model = Word2Vec.load("word2vec_model.model")

# Load the DataFrame
df = pd.read_csv('datajumia.csv', header=None, names=['Category', 'Transaction_Id'])
df['Processed_Category'] = df['Category'].apply(lambda x: x.lower())

# Endpoint for suggestion
@app.route('/ai/suggest', methods=['GET'])
def suggest():
    input_text_encoded = request.args.get('input')

    if not input_text_encoded:
        return jsonify({'error': 'Input text parameter is missing'}), 400

    # Decode the URL-encoded input
    input_text = unquote(input_text_encoded)

    input_text = preprocess_text(input_text)
    
    # Get similar words based on the input text
    similar_words = model.wv.most_similar(input_text, topn=5)

    # Extract words from the similar_words list
    suggestions = [word.split('_')[0] for word, _ in similar_words]

    return jsonify(suggestions)

def preprocess_text(text):
    return text.lower()

if __name__ == '__main__':
    app.run(debug=True, **{'workers': workers, 'bind': bind})
