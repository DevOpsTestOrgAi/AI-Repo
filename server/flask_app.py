from flask import Flask, request, jsonify
from gensim.models import Word2Vec
import pandas as pd
from gunicorn_config import *  # Import Gunicorn configuration

app = Flask(__name__)

# Load the Word2Vec model
model = Word2Vec.load("word2vec_model.model")

# Load the DataFrame
df = pd.read_csv('datajumia.csv', header=None, names=['Category', 'Transaction_Id'])
df['Processed_Category'] = df['Category'].apply(lambda x: x.lower())

# Endpoint for suggestion
@app.route('/ai/suggest', methods=['GET'])
def suggest():
    input_text = request.args.get('category')

    if not input_text:
        return jsonify({'error': 'Input text parameter is missing'}), 400

    input_text = preprocess_text(input_text)
    
    # Get the transaction_id for the input text
    transaction_id = df[df['Processed_Category'] == input_text]['Transaction_Id'].values
    if len(transaction_id) == 0:
        return jsonify({'error': 'Input text not found in the dataset'}), 404
    
    transaction_id = transaction_id[0]

    # Get similar words based on the transaction_id
    similar_words = model.wv.most_similar(input_text, topn=5)

    # Extract words and their similarities
    suggestions = [{'word': word.split('_')[0], 'similarity': similarity} for word, similarity in similar_words]

    return jsonify({'input_text': input_text, 'transaction_id': transaction_id, 'suggestions': suggestions})

def preprocess_text(text):
    return text.lower()

if __name__ == '__main__':
    app.run(debug=True, **{'workers': workers, 'bind': bind})
