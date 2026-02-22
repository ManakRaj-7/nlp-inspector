"""Text processing utilities"""
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
# Ensure NLTK data is available
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

STOPWORDS = set(stopwords.words("english"))

@staticmethod
def preprocess_text(text: str, remove_stopwords: bool = True, min_length: int = 3) -> str:
    """
    Clean and preprocess text.
    
    Args:
        text: Input text to preprocess
        remove_stopwords: Whether to remove English stopwords
        min_length: Minimum word length to keep
        
    Returns:
        Cleaned text
    """
    text = text.lower()
    text = re.sub(r"\d+", " ", text)  # remove numbers
    text = re.sub(r"[^\w\s]", " ", text)  # remove punctuation
    tokens = word_tokenize(text)
    
    if remove_stopwords:
        tokens = [t for t in tokens if t.isalpha() and t not in STOPWORDS and len(t) >= min_length]
    else:
        tokens = [t for t in tokens if t.isalpha() and len(t) >= min_length]
    
    return " ".join(tokens)

@staticmethod
def get_tokens(text: str, remove_stopwords: bool = True, min_length: int = 3) -> list:
    """
    Get list of tokens from text.
    
    Args:
        text: Input text
        remove_stopwords: Whether to remove stopwords
        min_length: Minimum word length
        
    Returns:
        List of tokens
    """
    text = text.lower()
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    tokens = word_tokenize(text)
    
    if remove_stopwords:
        tokens = [t for t in tokens if t.isalpha() and t not in STOPWORDS and len(t) >= min_length]
    else:
        tokens = [t for t in tokens if t.isalpha() and len(t) >= min_length]
    
    return tokens

def get_text_statistics(text: str, tokens: list) -> dict:
    """
    Get basic text statistics.
    
    Args:
        text: Original text
        tokens: Preprocessed tokens
        
    Returns:
        Dictionary of statistics
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    words_in_original = len(text.split())
    characters = len(text)
    characters_no_space = len(text.replace(" ", ""))
    avg_word_length = characters_no_space / len(text.split()) if text.split() else 0
    
    # Estimate reading time (200 words per minute)
    reading_time_minutes = len(text.split()) / 200
    
    freq = Counter(tokens)
    freq_df = pd.DataFrame(freq.items(), columns=["word", "count"]).sort_values(by="count", ascending=False)
    
    return {
        "total_words_cleaned": len(tokens),
        "unique_words": len(set(tokens)),
        "total_words_original": words_in_original,
        "characters": characters,
        "characters_no_space": characters_no_space,
        "avg_word_length": round(avg_word_length, 2),
        "sentence_count": len(sentences),
        "reading_time_minutes": round(reading_time_minutes, 2),
        "freq_df": freq_df,
        "top10": freq_df.head(10),
    }
