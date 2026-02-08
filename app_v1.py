import re
from collections import Counter

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob

# Ensure required NLTK data is available
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt_tab', quiet=True)
        nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

STOPWORDS = set(stopwords.words("english"))

st.set_page_config(page_title="Smart Text Cleaner & Analyzer", layout="centered")

st.title("Smart Text Cleaner & Analyzer")
st.write("Paste raw English text below and click **Analyze Text** to see cleaning and analysis results.")

text_input = st.text_area("Enter text", height=250, placeholder="Paste or type text here...")

def preprocess(text: str):
    text = text.lower()
    text = re.sub(r"\d+", " ", text)  # remove numbers
    text = re.sub(r"[^\w\s]", " ", text)  # remove punctuation (keep letters and whitespace)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha() and t not in STOPWORDS and len(t) > 2]
    return tokens

def analyze_text(raw_text: str):
    tokens = preprocess(raw_text)
    
    if not tokens:
        return None
    
    cleaned_text = " ".join(tokens)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    freq = Counter(tokens)
    freq_df = (
        pd.DataFrame(freq.items(), columns=["word", "count"])
        .sort_values(by="count", ascending=False)
        .reset_index(drop=True)
    )
    top10 = freq_df.head(10)
    
    try:
        polarity = TextBlob(raw_text).sentiment.polarity
    except Exception:
        polarity = 0.0
    
    if polarity > 0.1:
        sentiment_label = "Positive 😊"
    elif polarity < -0.1:
        sentiment_label = "Negative 😔"
    else:
        sentiment_label = "Neutral 😐"
    
    return {
        "cleaned_text": cleaned_text,
        "total_words": total_words,
        "unique_words": unique_words,
        "freq_df": freq_df,
        "top10": top10,
        "polarity": polarity,
        "sentiment_label": sentiment_label,
    }

if st.button("Analyze Text", type="primary"):
    if not text_input or not text_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        result = analyze_text(text_input)
        
        if result is None:
            st.error("No meaningful words found after cleaning. Try entering more text.")
        else:
            st.subheader("Cleaned Text")
            st.text_area("Cleaned output", value=result["cleaned_text"], height=180, disabled=True)

            st.subheader("📊 Statistics")
            cols = st.columns(2)
            cols[0].metric("Total words (after cleaning)", result["total_words"])
            cols[1].metric("Unique words", result["unique_words"])

            st.subheader("📈 Word Frequency (all words)")
            st.dataframe(result["freq_df"], use_container_width=True, hide_index=True)

            st.subheader("🎯 Top 10 Keywords")
            st.dataframe(result["top10"].reset_index(drop=True), use_container_width=True, hide_index=True)

            st.subheader("💭 Sentiment Analysis")
            col1, col2 = st.columns(2)
            col1.metric("Polarity Score", f"{result['polarity']:.3f}")
            col2.metric("Sentiment", result['sentiment_label'])

            if not result["top10"].empty:
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.bar(result["top10"]["word"], result["top10"]["count"], color="#4c78a8", edgecolor="black", alpha=0.7)
                ax.set_xlabel("Words", fontsize=12)
                ax.set_ylabel("Frequency", fontsize=12)
                ax.set_title("Top 10 Most Frequent Words", fontsize=14, fontweight="bold")
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()
                st.pyplot(fig)