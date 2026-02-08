# 🔍 Smart Text Analyzer - Version 2.0

**Advanced NLP Application with Professional UI and Enterprise Features**

![Version](https://img.shields.io/badge/version-2.0-blue)
![Status](https://img.shields.io/badge/status-development-orange)
![Python](https://img.shields.io/badge/python-3.9+-green)
![License](https://img.shields.io/badge/license-MIT-red)

## 🌟 Features Overview

### 📊 Core Analysis Features
- ✨ **Sentiment Analysis** - Polarity and subjectivity scoring
- 📚 **Readability Metrics** - Flesch-Kincaid, Dale-Chall, Reading Ease
- 🏷️ **Named Entity Recognition** - Extract persons, locations, organizations
- 🔤 **N-gram Analysis** - Bigrams and trigrams extraction
- 🎯 **TF-IDF Extraction** - Advanced keyword extraction
- 🌐 **Language Detection** - Auto-detect text language
- ☁️ **Word Cloud Visualization** - Beautiful word frequency visualization
- 📈 **Interactive Charts** - Plotly-powered visualizations

### 🎨 User Interface
- 📱 **Responsive Design** - Works on desktop and tablet
- 🎛️ **Sidebar Settings** - Customizable analysis options
- 📑 **Multi-Tab Interface** - Organized feature navigation
- 🌙 **Theme Support** - Light and dark mode options
- 📥 **Export Functionality** - CSV and JSON export
- 🔄 **Text Comparison** - Compare two texts side-by-side

### ⚡ Advanced Features
- 📊 Real-time statistics preview
- 🔍 Character and word count
- ⏱️ Reading time estimation
- 📋 Multiple analysis tabs
- 💾 Download results
- 🎯 Customizable analysis parameters

## 📋 Requirements

**Python**: 3.9 or higher  
**OS**: Windows, macOS, Linux

## 🚀 Installation

### 1. Clone/Download the Project
```bash
cd d:\College6thsem\nlp\files
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Required NLTK Data
```bash
python -m nltk.downloader punkt_tab stopwords averaged_perceptron_tagger maxent_ne_chunker words
```

## ⚙️ Usage

### Start the Application
```bash
streamlit run app.py
```

The app will open at: `http://localhost:8501`

### Navigation

**📝 Analyze Tab**
1. Enter text in the text area
2. Adjust settings in sidebar (word length, stopwords, etc.)
3. Toggle features you want to analyze
4. Click "🚀 Analyze Text" button
5. View results with visualizations
6. Export as CSV or JSON

**📊 Dashboard Tab**
- View comprehensive statistics
- See all visualizations together
- Interactive charts with hover data

**🔄 Compare Tab**
- Paste two different texts
- Compare for common words
- Find unique words in each text
- Get similarity metrics

**ℹ️ Help Tab**
- Feature documentation
- Usage tips
- Feature descriptions

## 📦 Dependencies

```
streamlit>=1.28.0         # Web framework
nltk>=3.8                 # NLP toolkit
textblob>=0.17.0          # Sentiment analysis
pandas>=2.0.0             # Data manipulation
matplotlib>=3.7.0         # Visualization
wordcloud>=1.9.3          # Word cloud generation
textstat>=0.7.3           # Readability metrics
langdetect>=1.0.9         # Language detection
scikit-learn>=1.3.0       # ML utilities
spacy>=3.6.0              # Advanced NLP
plotly>=5.17.0            # Interactive charts
python-docx>=0.8.11       # Document export
```

## 📁 Project Structure

```
smart-text-analyzer/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Project dependencies
├── GIT_GUIDE.md                   # Git version control guide
├── CHANGELOG_V2.md                # Version 2 changelog
├── README.md                       # This file
│
├── utils/                          # Utilities module
│   ├── __init__.py
│   ├── text_processing.py         # Text cleaning & tokenization
│   ├── nlp_features.py            # Advanced NLP functions
│   ├── visualizations.py          # Chart generation
│   └── exporters.py               # Export functionality
│
├── venv/                           # Virtual environment (auto-created)
│
└── .git/                           # Git repository
    ├── master branch               # Version 1.0 (stable)
    └── development branch          # Version 2.0 (current)
```

## 🎯 How to Use Each Feature

### Text Cleaning
```
Input: "Hello, World! This is a TEST."
Output: "hello world test"
- Removes punctuation
- Converts to lowercase
- Removes stopwords (optional)
- Filters by word length
```

### Sentiment Analysis
```
Returns:
- Polarity: -1 (negative) to 1 (positive)
- Subjectivity: 0 (objective) to 1 (subjective)
- Label: Positive 😊 | Neutral 😐 | Negative 😔
```

### Readability Score
```
Shows:
- Flesch-Kincaid Grade Level
- Flesch Reading Ease (0-100)
- Dale-Chall Score
- Difficulty interpretation
```

### Named Entities
```
Extracts:
- PERSON: Names of people
- LOCATION: Places and regions
- ORGANIZATION: Company and org names
```

### N-gram Analysis
```
Bigrams: "natural language", "text analysis"
Trigrams: "natural language processing", "text sentiment analysis"
```

### Word Cloud
```
Visual representation of word frequencies
- Larger words = more frequent
- Colors = variety and visual appeal
```

## 🔄 Git Version Control

### Switch Between Versions

**Go back to Version 1 (Stable)**
```bash
git checkout master
```

**Use Version 2 (Development)**
```bash
git checkout development
```

**View commit history**
```bash
git log --oneline --all --graph
```

### Version Information
- **v1.0 (master)**: Basic text analyzer - Simple and stable
- **v2.0 (development)**: Advanced analyzer - Full-featured and professional

See [GIT_GUIDE.md](GIT_GUIDE.md) for detailed git commands.

## 💡 Tips & Tricks

1. **Adjust Word Length**: Increase minimum word length to filter very short words
2. **Toggle Stopwords**: Remove common words for cleaner analysis
3. **Export Results**: Use CSV for spreadsheets, JSON for applications
4. **Compare Texts**: Find similarities between different documents
5. **Large Texts**: For texts over 10,000 words, features may take longer to process
6. **Language Detection**: Works best with texts in single language

## ⚠️ Limitations

- NER works best with longer texts (100+ words)
- Word cloud needs minimum 10 words
- Sentiment analysis optimized for English
- Large file processing may be slow (>50KB)
- Some advanced features require proper NLTK data

## 🐛 Troubleshooting

### NLTK Data Missing
```bash
python -m nltk.downloader punkt_tab stopwords
```

### Streamlit Not Starting
```bash
# Ensure virtual environment is active
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Reinstall streamlit
pip install streamlit --upgrade
```

### Out of Memory
- Reduce text size
- Restart the application
- Close other applications

## 🚀 Performance Notes

- Text processing: < 1 second for most texts
- Sentiment analysis: < 500ms
- Word cloud generation: 1-3 seconds
- N-gram analysis: < 500ms
- TF-IDF extraction: < 1 second

## 📊 Example Outputs

### Sentiment Analysis Output
```
Polarity: 0.567
Subjectivity: 0.723
Sentiment: Positive 😊
```

### Readability Output
```
Flesch-Kincaid Grade: 8.5
Flesch Reading Ease: 62.3
Difficulty: Standard (9-12 years)
```

### Statistics Output
```
Total Words (Cleaned): 156
Unique Words: 89
Sentences: 5
Avg Word Length: 4.5
Reading Time: 0.78 minutes
```

## 📚 Documentation

- [GIT_GUIDE.md](GIT_GUIDE.md) - Version control guide
- [CHANGELOG_V2.md](CHANGELOG_V2.md) - Detailed changelog
- Inline code documentation in utils/

## 🤝 Contributing

This is a personal project. Feel free to:
- Enhance existing features
- Add new analysis tools
- Improve UI/UX
- Fix bugs
- Create new branches for experiments

## 📄 License

MIT License - Feel free to use for educational and personal projects

## 👨‍💻 Author

Developed as an educational NLP project  
**Version**: 2.0  
**Last Updated**: February 8, 2026

## 🎓 Learning Resources

- **Streamlit**: https://streamlit.io/
- **NLTK**: https://www.nltk.org/
- **TextBlob**: https://textblob.readthedocs.io/
- **Plotly**: https://plotly.com/
- **Scikit-learn**: https://scikit-learn.org/

## ✅ Checklist for First Run

- [ ] Python 3.9+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] NLTK data downloaded
- [ ] Streamlit started: `streamlit run app.py`
- [ ] Browser opened at http://localhost:8501
- [ ] Test with sample text

## 🎉 Ready to Go!

Your Smart Text Analyzer is now ready to analyze any English text with professional-grade NLP features!

For questions or issues, check the Help tab in the application.

---

**Enjoy analyzing! 🚀**
