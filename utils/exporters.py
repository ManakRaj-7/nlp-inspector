"""Export utilities for different formats"""
import pandas as pd
import json
import streamlit as st
from io import BytesIO, StringIO


def export_to_csv(results: dict) -> bytes:
    """
    Export analysis results to CSV format.
    
    Args:
        results: Dictionary containing analysis results
        
    Returns:
        CSV bytes
    """
    try:
        data = {
            "Analysis Metric": [
                "Total Words (Cleaned)",
                "Unique Words",
                "Total Words (Original)",
                "Characters",
                "Reading Time (minutes)",
                "Sentiment Polarity",
                "Sentiment Subjectivity",
                "Readability Grade",
                "Flesch Reading Ease",
            ],
            "Value": [
                results.get("total_words_cleaned", "N/A"),
                results.get("unique_words", "N/A"),
                results.get("total_words_original", "N/A"),
                results.get("characters", "N/A"),
                results.get("reading_time_minutes", "N/A"),
                results.get("sentiment", {}).get("polarity", "N/A"),
                results.get("sentiment", {}).get("subjectivity", "N/A"),
                results.get("readability", {}).get("flesch_kincaid_grade", "N/A"),
                results.get("readability", {}).get("flesch_reading_ease", "N/A"),
            ]
        }
        
        df = pd.DataFrame(data)
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        
        return csv_buffer.getvalue().encode()
    except Exception as e:
        st.error(f"Error exporting to CSV: {str(e)}")
        return b""


def export_to_json(results: dict) -> bytes:
    """
    Export analysis results to JSON format.
    
    Args:
        results: Dictionary containing analysis results
        
    Returns:
        JSON bytes
    """
    try:
        # Convert DataFrames to dictionaries for JSON serialization
        json_data = {
            "text_statistics": {
                "total_words_cleaned": results.get("total_words_cleaned"),
                "unique_words": results.get("unique_words"),
                "total_words_original": results.get("total_words_original"),
                "characters": results.get("characters"),
                "reading_time_minutes": results.get("reading_time_minutes"),
            },
            "sentiment": results.get("sentiment", {}),
            "readability": results.get("readability", {}),
            "language": results.get("language", "unknown"),
            "entities": results.get("entities", {}),
        }
        
        # Add top keywords if available
        if "freq_df" in results and not results["freq_df"].empty:
            json_data["top_keywords"] = results["freq_df"].head(10).to_dict(orient="records")
        
        return json.dumps(json_data, indent=2).encode()
    except Exception as e:
        st.error(f"Error exporting to JSON: {str(e)}")
        return b""


def create_download_button(file_format: str, content: bytes, filename: str):
    """
    Create a download button for the exported file.
    
    Args:
        file_format: File format (csv, json, txt)
        content: File content as bytes
        filename: Name of the file to download
    """
    st.download_button(
        label=f"📥 Download as {file_format.upper()}",
        data=content,
        file_name=filename,
        mime=f"application/{file_format if file_format != 'csv' else 'csv'}"
    )
