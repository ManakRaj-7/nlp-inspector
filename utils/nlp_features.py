"""Advanced NLP features"""
from textblob import TextBlob
import textstat
from langdetect import detect, DetectorFactory
import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from collections import Counter

DetectorFactory.seed = 0

# Ensure NLTK data
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger', quiet=True)

try:
    nltk.data.find('chunkers/maxent_ne_chunker')
except LookupError:
    nltk.download('maxent_ne_chunker', quiet=True)

try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words', quiet=True)


def get_sentiment(text: str) -> dict:
    """
    Perform sentiment analysis using TextBlob.
    
    Args:
        text: Input text
        
    Returns:
        Dictionary with polarity, subjectivity, and label
    """
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        if polarity > 0.1:
            label = "Positive 😊"
            color = "green"
        elif polarity < -0.1:
            label = "Negative 😔"
            color = "red"
        else:
            label = "Neutral 😐"
            color = "gray"
        
        return {
            "polarity": round(polarity, 3),
            "subjectivity": round(subjectivity, 3),
            "label": label,
            "color": color,
        }
    except Exception as e:
        return {
            "polarity": 0.0,
            "subjectivity": 0.0,
            "label": "Error",
            "color": "gray",
            "error": str(e)
        }


def get_readability(text: str) -> dict:
    """
    Get readability statistics.
    
    Args:
        text: Input text
        
    Returns:
        Dictionary with various readability scores
    """
    try:
        flesch_kincaid = textstat.flesch_kincaid_grade(text)
        flesch_reading = textstat.flesch_reading_ease(text)
        dale_chall = textstat.dale_chall_readability_score(text)
        
        # Interpret Flesch Reading Ease
        if flesch_reading > 90:
            difficulty = "Very Easy (5-6 years)"
        elif flesch_reading > 80:
            difficulty = "Easy (6-7 years)"
        elif flesch_reading > 70:
            difficulty = "Fairly Easy (7-9 years)"
        elif flesch_reading > 60:
            difficulty = "Standard (9-12 years)"
        elif flesch_reading > 50:
            difficulty = "Fairly Difficult (12-15 years)"
        elif flesch_reading > 30:
            difficulty = "Difficult (College)"
        else:
            difficulty = "Very Difficult (College graduate)"
        
        return {
            "flesch_kincaid_grade": round(flesch_kincaid, 2),
            "flesch_reading_ease": round(flesch_reading, 2),
            "dale_chall_score": round(dale_chall, 2),
            "difficulty_level": difficulty,
        }
    except Exception as e:
        return {"error": str(e)}


def get_language(text: str) -> str:
    """
    Detect language of text.
    
    Args:
        text: Input text
        
    Returns:
        Language code (e.g., 'en', 'es', 'fr')
    """
    try:
        return detect(text)
    except Exception:
        return "unknown"


def extract_entities(text: str) -> dict:
    """
    Extract Named Entities using NLTK.
    
    Args:
        text: Input text
        
    Returns:
        Dictionary with persons, organizations, locations
    """
    try:
        sentences = sent_tokenize(text)
        all_entities = {"PERSON": [], "ORGANIZATION": [], "LOCATION": [], "OTHER": []}
        
        for sentence in sentences:
            tokens = word_tokenize(sentence)
            pos_tags = pos_tag(tokens)
            ne_tree = ne_chunk(pos_tags)
            
            for subtree in ne_tree:
                if hasattr(subtree, 'label'):
                    entity_name = " ".join([word for word, tag in subtree.leaves()])
                    entity_type = subtree.label()
                    
                    if entity_type == "PERSON":
                        all_entities["PERSON"].append(entity_name)
                    elif entity_type == "ORGANIZATION":
                        all_entities["ORGANIZATION"].append(entity_name)
                    elif entity_type == "GPE":  # Geo-political entity
                        all_entities["LOCATION"].append(entity_name)
                    else:
                        all_entities["OTHER"].append(f"{entity_name} ({entity_type})")
        
        # Remove duplicates
        for key in all_entities:
            all_entities[key] = list(set(all_entities[key]))
        
        return all_entities
    except Exception as e:
        return {"error": str(e)}


def extract_ngrams(tokens: list, n: int = 2) -> list:
    """
    Extract n-grams from tokens.
    
    Args:
        tokens: List of tokens
        n: N-gram size (2 for bigrams, 3 for trigrams)
        
    Returns:
        List of (n-gram, frequency) tuples
    """
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngram = " ".join(tokens[i:i + n])
        ngrams.append(ngram)
    
    freq = Counter(ngrams)
    return freq.most_common(10)


def get_tfidf_keywords(text: str, n_keywords: int = 10) -> pd.DataFrame:
    """
    Extract keywords using TF-IDF.
    
    Args:
        text: Input text
        n_keywords: Number of keywords to extract
        
    Returns:
        DataFrame with keywords and scores
    """
    try:
        # Split into sentences and create documents
        sentences = text.split('.')
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if len(sentences) < 2:
            # If only one sentence, split into phrases
            sentences = text.split(',')
            sentences = [s.strip() for s in sentences if s.strip()]
        
        if len(sentences) < 2:
            return pd.DataFrame({"keyword": ["text_too_short"], "score": [0]})
        
        vectorizer = TfidfVectorizer(max_features=n_keywords, stop_words='english')
        X = vectorizer.fit_transform(sentences)
        
        scores = X.sum(axis=0).A1
        keywords = vectorizer.get_feature_names_out()
        
        df = pd.DataFrame({
            "keyword": keywords,
            "score": scores
        }).sort_values('score', ascending=False)
        
        return df
    except Exception as e:
        return pd.DataFrame({"error": [str(e)]})
