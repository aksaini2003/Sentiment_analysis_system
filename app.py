from flask import Flask, render_template, request, jsonify
import joblib
import re
import string
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import numpy as np
import traceback

# Download required NLTK data
try:
    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('english'))
except:
    stop_words = set()

# Initialize Flask app
app = Flask(__name__)

# Load the models and vectorizer
try:
    model = joblib.load('log_reg_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    slang_dict = joblib.load('slang_dictionary.pkl')
except Exception as e:
    print(f"Error loading models: {str(e)}")
    model = None
    vectorizer = None
    slang_dict = {}

def preprocess_text(text):
    try:
        # Convert to lowercase
        text = text.lower()
        
        # Remove HTML tags
        text = re.sub(r'<.*?>', '', text)
        
        # Remove URLs
        text = re.sub(r'http[s]?://\S+|www\.\S+', '', text)
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        
        # Replace slang words
        for slang, meaning in slang_dict.items():
            text = re.sub(r'\b' + re.escape(slang.lower()) + r'\b', meaning, text)
        
        # Correct spelling using TextBlob
        text = str(TextBlob(text).correct())
        
        # Remove stopwords
        words = text.split()
        words = [word for word in words if word not in stop_words]
        text = ' '.join(words)
        
        return text.strip()
    except Exception as e:
        print(f"Error in preprocessing: {str(e)}")
        return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input text from request
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        text = data['text']
        if not text.strip():
            return jsonify({'error': 'Empty text provided'}), 400
        
        # Preprocess the text
        processed_text = preprocess_text(text)
        
        # Transform text using vectorizer
        if vectorizer is None:
            return jsonify({'error': 'Model not loaded properly'}), 500
        
        text_vectorized = vectorizer.transform([processed_text])
        
        # Make prediction
        prediction = model.predict(text_vectorized)[0]
        probability = model.predict_proba(text_vectorized)[0]
        confidence = max(probability)
        
        # Determine sentiment and confidence
        sentiment = 'positive' if prediction == 1 else 'negative'
        
        return jsonify({
            'sentiment': sentiment,
            'confidence': float(confidence)
        })
        
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': 'An error occurred while analyzing the text'}), 500

if __name__ == '__main__':
    app.run(debug=True)