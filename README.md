# SentimentAI - Movie Review Sentiment Analysis

A modern web application that analyzes the sentiment of movie reviews using machine learning. Built with Python, Flask, and a beautiful responsive UI.

![SentimentAI Logo](static/favicon.svg)

## Overview

SentimentAI is a sophisticated sentiment analysis tool that can determine whether a movie review is positive or negative. It uses machine learning models trained on the IMDB Movie Reviews dataset to provide accurate sentiment predictions with confidence scores.

## Features

- 🧠 Advanced sentiment analysis using machine learning
- 📊 Confidence score visualization
- 💫 Modern, responsive UI with smooth animations
- ⚡ Real-time analysis with loading states
- 🎨 Beautiful gradient design elements
- 📱 Mobile-friendly interface

## Technical Implementation

### Data Processing and Model Training

1. Dataset: IMDB Movie Reviews (50,000 reviews)
2. Data Preprocessing Steps:
   - Removed duplicates (418 duplicates found)
   - Encoded sentiments (positive: 1, negative: 0)
   - Text preprocessing (lowercase, special character removal)
   - Vectorization using TF-IDF

### Machine Learning Models

Two models were implemented and compared:
1. Logistic Regression
2. Random Forest Classifier

Both models were trained on the preprocessed IMDB dataset to classify reviews as positive or negative.

## Project Structure

```
sentiment_analysis/
├── app.py              # Flask application
├── main.py            # Model training and utilities
├── templates/
│   └── index.html     # Main application template
├── static/
│   ├── style.css      # Application styling
│   ├── script.js      # Frontend JavaScript
│   ├── favicon.svg    # Vector favicon
│   └── favicon.ico    # Fallback favicon
└── sentiment_analysis.ipynb  # Model development notebook
```

## Setup and Installation

1. Clone the repository
```bash
git clone [repository-url]
cd sentiment_analysis
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter a movie review text in the input box
2. Click "Analyze with AI" or press Enter
3. View the sentiment analysis results:
   - Sentiment (Positive/Negative)
   - Confidence score with visual indicator
   - Clear the input using the "Clear" button

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: scikit-learn, pandas, numpy
- **UI Components**: Font Awesome icons
- **Design**: Custom CSS with gradients and animations

## Future Improvements

- Add support for batch analysis
- Implement user accounts to save analysis history
- Add more detailed sentiment analysis (e.g., neutral, very positive, very negative)
- Integrate with movie databases for additional context
- Add support for multiple languages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
