"""Visualization utilities"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter
import streamlit as st


def create_wordcloud(tokens: list, title: str = "Word Cloud"):
    """
    Create and display a word cloud.
    
    Args:
        tokens: List of tokens
        title: Title for the word cloud
        
    Returns:
        Plotly figure
    """
    try:
        text = " ".join(tokens)
        
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis',
            max_words=100
        ).generate(text)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        
        return fig
    except Exception as e:
        st.error(f"Error creating word cloud: {str(e)}")
        return None


def create_ngram_chart(ngrams: list, n: int = 2):
    """
    Create a bar chart for n-grams.
    
    Args:
        ngrams: List of (ngram, frequency) tuples
        n: N-gram size
        
    Returns:
        Plotly figure
    """
    if not ngrams:
        return None
    
    ngrams_text = [ng[0] for ng in ngrams]
    frequencies = [ng[1] for ng in ngrams]
    
    fig = go.Figure(data=[
        go.Bar(x=ngrams_text, y=frequencies, marker=dict(color='#4c78a8'))
    ])
    
    fig.update_layout(
        title=f"Top {len(ngrams)} {n}-grams",
        xaxis_title="N-grams",
        yaxis_title="Frequency",
        template="plotly_white",
        height=500,
        showlegend=False,
    )
    
    fig.update_xaxes(tickangle=-45)
    
    return fig


def create_sentiment_gauge(polarity: float, subjectivity: float):
    """
    Create a gauge chart for sentiment.
    
    Args:
        polarity: Sentiment polarity (-1 to 1)
        subjectivity: Sentiment subjectivity (0 to 1)
        
    Returns:
        Plotly figure
    """
    # Convert polarity from -1,1 to 0,100 scale
    polarity_scale = ((polarity + 1) / 2) * 100
    subjectivity_scale = subjectivity * 100
    
    fig = go.Figure(data=[
        go.Indicator(
            mode="gauge+number",
            value=polarity_scale,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Sentiment Polarity"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 33], 'color': "lightcoral"},
                    {'range': [33, 66], 'color': "lightyellow"},
                    {'range': [66, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 50
                }
            }
        )
    ])
    
    fig.update_layout(height=400)
    
    return fig


def create_frequency_comparison(freq_df, top_n=10):
    """
    Create an interactive frequency bar chart.
    
    Args:
        freq_df: DataFrame with word frequencies
        top_n: Number of top words to show
        
    Returns:
        Plotly figure
    """
    top_df = freq_df.head(top_n)
    
    fig = px.bar(
        top_df,
        x='word',
        y='count',
        title=f"Top {top_n} Most Frequent Words",
        labels={'word': 'Word', 'count': 'Frequency'},
        color='count',
        color_continuous_scale='Viridis',
    )
    
    fig.update_layout(
        template="plotly_white",
        height=500,
        showlegend=False,
        xaxis_tickangle=-45,
    )
    
    return fig
