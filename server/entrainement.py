# entrainement.py

import pandas as pd
from gensim.models import Word2Vec

# Function to preprocess text
def preprocess_text(text):
    return text.lower()

# Load the DataFrame with encoding specified
df = pd.read_csv('datajumia.csv', header=None, names=['Category', 'Transaction_Id'], encoding='utf-8')

# Apply preprocessing to categories
df['Processed_Category'] = df['Category'].apply(preprocess_text)

# Prepare sentences for Word2Vec by grouping based on transaction_ids
sentences = df.groupby('Transaction_Id')['Processed_Category'].apply(list).tolist()

# Train the Word2Vec model
word2vec_model = Word2Vec(sentences=sentences, vector_size=100, window=10, min_count=1, workers=4, epochs=100)

def get_similar_words(input_text):
    target_keyword_work = preprocess_text(input_text)
    target_transaction_id = df[df['Processed_Category'] == target_keyword_work]['Transaction_Id'].values[0]

    # Get similar words based on the transaction_id
    similar_words = word2vec_model.wv.most_similar(f"{target_keyword_work}", topn=5)

    # Return only the list of similar words without similarity scores
    return [word.split('_')[0] for word, _ in similar_words]
