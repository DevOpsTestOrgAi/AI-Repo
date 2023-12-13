# flask_app.py

from flask import Flask, request, jsonify
from urllib.parse import unquote
from entrainement import get_similar_words, word2vec_model

app = Flask(__name__)

# Endpoint for suggestion
@app.route('/ai/suggest', methods=['GET'])
def suggest():
    input_text_encoded = request.args.get('input')

    if not input_text_encoded:
        return jsonify({'error': 'Input text parameter is missing'}), 400

    # Decode the URL-encoded input
    input_text = unquote(input_text_encoded)

    # Get similar words for the input text using the pre-trained model
    suggestions = get_similar_words(input_text)

    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
