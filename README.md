# Smart Text Cleaner & Analyzer

A beginner-friendly NLP web application built with Streamlit. Paste raw English text and get cleaned text, word statistics, keyword extraction, sentiment analysis, and a visualization of the top words.

## Features
- Streamlit-based web interface
- Large multiline text input
- Text preprocessing:
  - Lowercasing
  - Remove punctuation
  - Remove numeric characters
  - Tokenization
  - Remove English stopwords (NLTK)
- Displays cleaned text
- Shows total word count and unique word count
- Generates a sorted word frequency table
- Extracts top 10 keywords by frequency
- Performs sentiment analysis using TextBlob (with classification: Positive / Neutral / Negative)
- Visualizes the top 10 words using a Matplotlib bar chart

## Tech Stack
- Python
- Streamlit
- NLTK
- TextBlob
- Pandas
- Matplotlib

## Installation

1. Clone or download this project.
2. (Optional but recommended) Create and activate a virtual environment:
   - python -m venv venv
   - On macOS/Linux: source venv/bin/activate
   - On Windows: venv\Scripts\activate
3. Install dependencies:
   - pip install -r requirements.txt

Note: The app will automatically download the necessary NLTK data (`punkt` and `stopwords`) on first run.

If you want to ensure TextBlob corpora are available (usually not required for basic sentiment), run:
- python -m textblob.download_corpora

## Run the Streamlit App

From the project directory run:

streamlit run app.py

The app will open in your browser (usually at http://localhost:8501).

## Usage

1. Paste or type English text into the large text box.
2. Click "Analyze Text".
3. View the cleaned text, statistics, word frequency table, top keywords, sentiment score/label, and bar chart.

## Notes

- The sentiment score is computed on the original raw text using TextBlob's polarity.
- The cleaning and keyword extraction are case-insensitive and use NLTK English stopwords.

Enjoy exploring your text!