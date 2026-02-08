"""
Smart Text Cleaner & Analyzer - Version 2
Advanced NLP application with multiple features and beautiful UI
"""

import streamlit as st
import pandas as pd
import textwrap
import streamlit.components.v1 as components
from utils.text_processing import preprocess_text, get_tokens, get_text_statistics
from utils.nlp_features import (
    get_sentiment, get_readability, get_language,
    extract_entities, extract_ngrams, get_tfidf_keywords
)
from utils.visualizations import (
    create_wordcloud, create_ngram_chart, create_sentiment_gauge,
    create_frequency_comparison
)
from utils.exporters import export_to_csv, export_to_json

# Page configuration
st.set_page_config(
    page_title="Smart Text Analyzer",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Note: theme-specific CSS is applied after the sidebar selection so
# dark/light mode can be switched at runtime.

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    # Theme toggle
    st.markdown("### Theme")
    theme = st.radio("Choose theme:", ["Light", "Dark"], label_visibility="collapsed")
    
    # Analysis options
    st.markdown("### Analysis Options")
    remove_stopwords = st.checkbox("Remove English Stopwords", value=True)
    min_word_length = st.slider("Minimum Word Length:", 1, 5, 3)
    
    st.markdown("---")
    
    # Features toggle
    st.markdown("### Features to Analyze")
    show_sentiment = st.checkbox("📊 Sentiment Analysis", value=True)
    show_readability = st.checkbox("📚 Readability Score", value=True)
    show_entities = st.checkbox("🏷️ Named Entities", value=True)
    show_ngrams = st.checkbox("🔤 N-gram Analysis", value=True)
    show_wordcloud = st.checkbox("☁️ Word Cloud", value=True)
    show_tfidf = st.checkbox("🎯 TF-IDF Keywords", value=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### 📖 About
    Smart Text Analyzer v2.0  
    Advanced NLP application for text analysis
    """)

# Main header
def apply_theme(selected_theme: str):
    """Inject CSS for light or dark theme at runtime."""
    common_css = """
<style>
.main-header { text-align: center; padding: 20px 0; border-radius: 10px; margin-bottom: 20px; }
.feature-box { padding: 15px; border-radius: 8px; margin-bottom: 10px; }
.metric-card { padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
</style>
    """

    if selected_theme == "Dark":
        # Strong CSS overrides (high specificity + !important) to force dark theme
        dark_css = """
    <style>
    /* Force app background and text */
    .stApp, .main, .block-container { background: #0f1724 !important; color: #e6eef8 !important; }
    /* Sidebar */
    [data-testid="stSidebar"] { background: #071020 !important; color: #cfe6ff !important; }
    /* Header gradient */
    .main-header { background: linear-gradient(135deg,#1f3a93 0%,#4b2b6f 100%) !important; color: #ffffff !important; padding: 24px !important; }
    /* Info boxes */
    .feature-box, .stCard { background: #0b1320 !important; border-left: 4px solid #2b6fb3 !important; }
    .metric-card, .stMetric { background: #071022 !important; box-shadow: 0 2px 6px rgba(0,0,0,0.6) !important; }
    /* Inputs and textareas */
    textarea, input, .stTextArea textarea, .stTextInput input, .stTextInput>div>div>input { background: #071022 !important; color: #e6eef8 !important; }
    /* Tables and dataframes */
    .stDataFrame, .stDataFrame div, .stTable { background: #0f1724 !important; color: #e6eef8 !important; }
    /* Buttons */
    .stButton>button { background: linear-gradient(90deg,#334b86,#6b3f90) !important; color: #fff !important; }
    /* Plotly and matplotlib backgrounds */
    .js-plotly-plot .plotly, .plotly, svg { background: transparent !important; }
    /* Ensure code blocks don't show injected CSS */
    .stExpander pre, .stCodeBlock pre { background: #071022 !important; color: #e6eef8 !important; }
    </style>
    """
        components.html(textwrap.dedent(common_css + dark_css), height=0)
    else:
        # Strong CSS overrides for light theme (ensure consistent look)
        light_css = """
    <style>
    .stApp, .main, .block-container { background: #ffffff !important; color: #0b1b2b !important; }
    [data-testid="stSidebar"] { background: #f0f2f6 !important; color: #0b1b2b !important; }
    .main-header { background: linear-gradient(135deg,#667eea 0%,#764ba2 100%) !important; color: #ffffff !important; padding: 20px !important; }
    .feature-box, .stCard { background: #f9f9f9 !important; border-left: 4px solid #667eea !important; }
    .metric-card, .stMetric { background: #ffffff !important; box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important; }
    textarea, input, .stTextArea textarea, .stTextInput input { background: #f7fafc !important; color: #0b1b2b !important; }
    .stDataFrame, .stTable { background: #ffffff !important; color: #0b1b2b !important; }
    .stButton>button { background: linear-gradient(90deg,#ff7b7b,#ffb86b) !important; color: #fff !important; }
    </style>
    """
        components.html(textwrap.dedent(common_css + light_css), height=0)


# apply selected theme
apply_theme(theme)

# Main header
st.markdown(textwrap.dedent("""
<div class="main-header">
    <h1>🔍 Smart Text Analyzer</h1>
    <p>Advanced Natural Language Processing & Text Analysis Tool</p>
</div>
"""), unsafe_allow_html=True)

# Main content area
tab1, tab2, tab3, tab4 = st.tabs(["📝 Analyze", "📊 Dashboard", "🔄 Compare", "ℹ️ Help"])

with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("Enter Your Text")
        text_input = st.text_area(
            "Paste or type text here...",
            height=250,
            placeholder="Enter text for analysis...",
            label_visibility="collapsed"
        )
    
    with col2:
        st.write("### 📋 Quick Info")
        if text_input:
            st.metric("Characters", len(text_input))
            st.metric("Words", len(text_input.split()))
            st.metric("Sentences", len([s for s in text_input.split('.') if s.strip()]))
    
    # Analyze button
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        analyze_btn = st.button("🚀 Analyze Text", type="primary", use_container_width=True)
    with col2:
        clear_btn = st.button("🗑️ Clear", use_container_width=True)
    
    if clear_btn:
        st.rerun()
    
    # Analysis results
    if analyze_btn and text_input.strip():
        with st.spinner("🔄 Analyzing text..."):
            try:
                # Text processing
                tokens = get_tokens(text_input, remove_stopwords, min_word_length)
                cleaned_text = " ".join(tokens)
                
                if not tokens:
                    st.error("❌ No meaningful words found. Try adjusting the minimum word length or using different text.")
                else:
                    # Get all statistics
                    stats = get_text_statistics(text_input, tokens)
                    sentiment = get_sentiment(text_input) if show_sentiment else None
                    readability = get_readability(text_input) if show_readability else None
                    language = get_language(text_input)
                    entities = extract_entities(text_input) if show_entities else None
                    
                    # Display Cleaned Text
                    st.markdown("---")
                    st.subheader("✨ Cleaned Text")
                    st.info(cleaned_text)
                    
                    # Statistics Dashboard
                    st.markdown("---")
                    st.subheader("📊 Text Statistics")
                    
                    stat_cols = st.columns(5)
                    with stat_cols[0]:
                        st.metric("Total Words (Cleaned)", stats["total_words_cleaned"])
                    with stat_cols[1]:
                        st.metric("Unique Words", stats["unique_words"])
                    with stat_cols[2]:
                        st.metric("Sentences", stats["sentence_count"])
                    with stat_cols[3]:
                        st.metric("Avg Word Length", stats["avg_word_length"])
                    with stat_cols[4]:
                        st.metric("Reading Time (min)", stats["reading_time_minutes"])
                    
                    # Sentiment Analysis
                    if show_sentiment and sentiment:
                        st.markdown("---")
                        st.subheader("💭 Sentiment Analysis")
                        sent_cols = st.columns(3)
                        with sent_cols[0]:
                            st.metric("Polarity", sentiment["polarity"], delta=sentiment["label"])
                        with sent_cols[1]:
                            st.metric("Subjectivity", sentiment["subjectivity"])
                        with sent_cols[2]:
                            st.metric("Sentiment", sentiment["label"])
                    
                    # Readability
                    if show_readability and readability:
                        st.markdown("---")
                        st.subheader("📚 Readability Score")
                        read_cols = st.columns(3)
                        with read_cols[0]:
                            st.metric("Flesch-Kincaid Grade", readability["flesch_kincaid_grade"])
                        with read_cols[1]:
                            st.metric("Flesch Reading Ease", readability["flesch_reading_ease"])
                        with read_cols[2]:
                            st.write(f"**Difficulty Level:**  \n{readability['difficulty_level']}")
                    
                    # Named Entities
                    if show_entities and entities and "error" not in entities:
                        st.markdown("---")
                        st.subheader("🏷️ Named Entities")
                        entity_cols = st.columns(2)
                        with entity_cols[0]:
                            if entities["PERSON"]:
                                st.write("**👤 Persons:**")
                                for person in entities["PERSON"][:5]:
                                    st.write(f"- {person}")
                        with entity_cols[1]:
                            if entities["LOCATION"]:
                                st.write("**📍 Locations:**")
                                for loc in entities["LOCATION"][:5]:
                                    st.write(f"- {loc}")
                    
                    # Word Frequency Table
                    st.markdown("---")
                    st.subheader("📈 Word Frequency")
                    st.dataframe(stats["freq_df"].head(15), use_container_width=True, hide_index=True)
                    
                    # N-gram Analysis
                    if show_ngrams:
                        st.markdown("---")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("🔤 Bigrams (2-word phrases)")
                            bigrams = extract_ngrams(tokens, 2)
                            if bigrams:
                                bigrams_df = pd.DataFrame(bigrams, columns=["bigram", "frequency"])
                                fig_bigram = create_ngram_chart(bigrams, 2)
                                st.plotly_chart(fig_bigram, use_container_width=True)
                        with col2:
                            st.subheader("🔤 Trigrams (3-word phrases)")
                            trigrams = extract_ngrams(tokens, 3)
                            if trigrams:
                                trigrams_df = pd.DataFrame(trigrams, columns=["trigram", "frequency"])
                                fig_trigram = create_ngram_chart(trigrams, 3)
                                st.plotly_chart(fig_trigram, use_container_width=True)
                    
                    # TF-IDF Keywords
                    if show_tfidf:
                        st.markdown("---")
                        st.subheader("🎯 TF-IDF Keywords")
                        tfidf_df = get_tfidf_keywords(text_input, 10)
                        if not tfidf_df.empty and "error" not in tfidf_df.columns:
                            st.dataframe(tfidf_df.head(10), use_container_width=True, hide_index=True)
                    
                    # Word Cloud
                    if show_wordcloud:
                        st.markdown("---")
                        st.subheader("☁️ Word Cloud")
                        wc_fig = create_wordcloud(tokens, "Most Frequent Words")
                        if wc_fig:
                            st.pyplot(wc_fig)
                    
                    # Frequency Chart
                    st.markdown("---")
                    st.subheader("📊 Interactive Frequency Chart")
                    freq_chart = create_frequency_comparison(stats["freq_df"], 10)
                    st.plotly_chart(freq_chart, use_container_width=True)
                    
                    # Export Section
                    st.markdown("---")
                    st.subheader("💾 Export Results")
                    exp_col1, exp_col2 = st.columns(2)
                    
                    with exp_col1:
                        csv_data = export_to_csv({
                            "total_words_cleaned": stats["total_words_cleaned"],
                            "unique_words": stats["unique_words"],
                            "total_words_original": stats["total_words_original"],
                            "characters": stats["characters"],
                            "reading_time_minutes": stats["reading_time_minutes"],
                            "sentiment": sentiment,
                            "readability": readability,
                        })
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv_data,
                            file_name="analysis_results.csv",
                            mime="text/csv"
                        )
                    
                    with exp_col2:
                        json_data = export_to_json({
                            "total_words_cleaned": stats["total_words_cleaned"],
                            "unique_words": stats["unique_words"],
                            "total_words_original": stats["total_words_original"],
                            "characters": stats["characters"],
                            "reading_time_minutes": stats["reading_time_minutes"],
                            "sentiment": sentiment,
                            "readability": readability,
                            "language": language,
                            "entities": entities,
                            "freq_df": stats["freq_df"],
                        })
                        st.download_button(
                            label="📥 Download JSON",
                            data=json_data,
                            file_name="analysis_results.json",
                            mime="application/json"
                        )
            
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")

with tab2:
    st.markdown("### 📊 Dashboard")
    st.info("Analyze text in the first tab to see the dashboard with visualizations.")

with tab3:
    st.markdown("### 🔄 Text Comparison")
    col1, col2 = st.columns(2)
    
    with col1:
        text1 = st.text_area("Text 1:", height=200, key="text1")
    
    with col2:
        text2 = st.text_area("Text 2:", height=200, key="text2")
    
    if st.button("Compare Texts", type="primary"):
        if text1 and text2:
            tokens1 = set(get_tokens(text1, True, 3))
            tokens2 = set(get_tokens(text2, True, 3))
            
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Common Words", len(tokens1 & tokens2))
            with col2:
                st.metric("Unique to Text 1", len(tokens1 - tokens2))
            with col3:
                st.metric("Unique to Text 2", len(tokens2 - tokens1))
            
            st.markdown("---")
            st.subheader("📝 Common Words")
            common_words = sorted(list(tokens1 & tokens2))
            if common_words:
                st.write(", ".join(common_words[:50]))

with tab4:
    st.markdown("### ℹ️ Help & Guide")
    st.markdown(textwrap.dedent("""
#### 🎯 Features

**Text Cleaning**
- Remove punctuation and special characters
- Convert to lowercase
- Remove English stopwords (optional)
- Filter by minimum word length

**Analysis Features**
- 📊 Sentiment Analysis (Polarity & Subjectivity)
- 📚 Readability Scores (Flesch-Kincaid, etc.)
- 🏷️ Named Entity Recognition (Persons, Locations)
- 🔤 N-gram Analysis (Bigrams & Trigrams)
- ☁️ Word Cloud Visualization
- 🎯 TF-IDF Keyword Extraction
- 📈 Interactive Frequency Charts

**Export Options**
- 📥 Download as CSV
- 📥 Download as JSON

#### 💡 Tips
- Adjust the minimum word length to filter very short words
- Use the stopwords toggle to include/exclude common words
- Compare two texts to find similarities and differences

#### 📧 Contact
For issues or suggestions, please reach out!
"""))
