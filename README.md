# 🔍 NLP Inspector  
**Advanced Text Analysis & Intelligence Platform**

---

<div align="center">

[![Live Demo](https://img.shields.io/badge/🚀%20Launch%20App-Streamlit%20Cloud-blue?style=for-the-badge&logo=streamlit)](https://nlp-inspector-mpt4gcpljcjke4dcdbwea4.streamlit.app)
[![GitHub](https://img.shields.io/badge/📦%20GitHub-Source%20Code-black?style=for-the-badge&logo=github)](https://github.com/ManakRaj-7/nlp-inspector)

[![Python](https://img.shields.io/badge/python-3.9+-green?style=flat&logo=python)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28%2B-red?style=flat&logo=streamlit)](https://streamlit.io)
[![License](https://img.shields.io/badge/license-MIT-orange?style=flat)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active%20Development-brightgreen?style=flat)

</div>

---

## 📌 Overview

**NLP Inspector** is a comprehensive, production-ready Natural Language Processing application built with Streamlit. It provides advanced text analysis, visualization, and export capabilities with an intuitive, modern interface.

Whether you're analyzing customer feedback, researching text sentiment, extracting key information, or exploring linguistic patterns — NLP Inspector has you covered.

---

## ✨ Key Features

### 🧠 Intelligent Analysis
- **Sentiment Analysis** — Detect polarity, subjectivity, and emotional tone
- **Named Entity Recognition** — Extract persons, locations, organizations, and more
- **Readability Metrics** — Flesch-Kincaid, Dale-Chall, SMOG indices
- **Language Detection** — Auto-identify text language
- **TF-IDF & N-Gram Analysis** — Advanced keyword and phrase extraction
- **Character & Word Statistics** — Comprehensive text metrics

### 📊 Rich Visualizations
- **Word Clouds** — Beautiful, frequency-based word visualization
- **Interactive Charts** — Plotly-powered, responsive visualizations
- **Comparative Analysis** — Side-by-side text comparison
- **Real-time Dashboard** — All insights in one unified view

### 🎨 Professional UI/UX
- **Multi-Tab Interface** — Organized, intuitive navigation
- **Dark/Light Themes** — Seamless theme switching
- **Responsive Design** — Works on desktop, tablet, and mobile
- **Sidebar Configuration** — Customizable analysis parameters
- **One-Click Export** — CSV and JSON download options

### ⚡ Enterprise Features
- **Batch Processing** — Analyze multiple texts efficiently
- **Export Functionality** — Save results in standard formats
- **Text Comparison Tool** — Compare and contrast multiple texts
- **Detailed Reporting** — Comprehensive analysis summaries

---

## 🚀 Quick Start

### Option 1: Try Online (No Installation)
Click the button below to launch the live demo instantly:

[![Live Demo](https://img.shields.io/badge/🚀%20Open%20Live%20App-blue?style=for-the-badge)](https://nlp-inspector-mpt4gcpljcjke4dcdbwea4.streamlit.app)

### Option 2: Run Locally

#### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

#### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/ManakRaj-7/nlp-inspector.git
cd nlp-inspector

# 2. Create virtual environment
python -m venv venv

# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download NLTK data
python -m nltk.downloader punkt_tab stopwords averaged_perceptron_tagger maxent_ne_chunker words

# 5. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🎯 How to Use

### Analyze Tab (Main Analysis)
1. **Enter Text** — Paste or type English text (any length)
2. **Configure** — Use sidebar to customize analysis:
   - Toggle analysis features
   - Set minimum word length
   - Enable/disable stopword removal
3. **Analyze** — Click "🚀 Analyze Text"
4. **Explore** — Review insights, charts, and statistics
5. **Export** — Download results as CSV or JSON

### Dashboard Tab (Comprehensive View)
- View all analysis results in one unified dashboard
- Interactive visualizations with hover tooltips
- Real-time statistics and metrics
- Export entire dashboard as JSON

### Compare Tab (Text Comparison)
- Paste two texts for comparison
- Find common words and phrases
- Identify unique elements
- View frequency differences

### Help Tab (Documentation)
- Feature descriptions
- Usage tips and best practices
- FAQ section

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | Streamlit | Interactive UI & real-time app |
| **NLP Processing** | NLTK, spaCy | Tokenization, entity recognition |
| **Sentiment** | TextBlob | Polarity & subjectivity analysis |
| **Visualization** | Plotly, Matplotlib | Interactive & static charts |
| **Text Metrics** | Textstat | Readability scores |
| **Language Detection** | Langdetect | Multi-language support |
| **Data Processing** | Pandas, scikit-learn | Data manipulation & TF-IDF |
| **Hosting** | Streamlit Cloud | Free, global deployment |

---

## 📦 Project Structure

```
nlp-inspector/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── GIT_GUIDE.md             # Git workflow guide
├── BUILD_SUMMARY.md         # Build documentation
├── CHANGELOG_V2.md          # Version history
│
├── utils/                    # Utility modules
│   ├── __init__.py
│   ├── text_processing.py   # Text cleaning & tokenization
│   ├── nlp_features.py      # NLP analysis functions
│   ├── visualizations.py    # Chart & graph generation
│   └── exporters.py         # CSV/JSON export
│
├── .streamlit/
│   └── config.toml          # Streamlit configuration
│
└── .git/                     # Version control
    ├── main branch          # Production (default)
    ├── development branch   # Active development
    └── master branch        # Version 1.0 archive
```

---

## 📋 Requirements

```
streamlit>=1.28.0          # Web framework
nltk>=3.8                  # NLP toolkit
textblob>=0.17.0           # Sentiment analysis
pandas>=2.0.0              # Data processing
matplotlib>=3.7.0          # Visualizations
wordcloud>=1.9.3           # Word cloud generation
textstat>=0.7.3            # Readability metrics
langdetect>=1.0.9          # Language detection
scikit-learn>=1.3.0        # ML utilities
spacy>=3.6.0               # Advanced NLP
plotly>=5.17.0             # Interactive charts
python-docx>=0.8.11        # Document export
```

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙋 Support & Feedback

Found a bug? Have a feature request? We'd love to hear from you!

- **Issues**: [GitHub Issues](https://github.com/ManakRaj-7/nlp-inspector/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ManakRaj-7/nlp-inspector/discussions)

---

## 📊 Version History

- **v2.0** (Current) — Advanced NLP, interactive UI, exports, multi-tab interface
- **v1.0** — Basic text cleaning and sentiment analysis

See [CHANGELOG_V2.md](CHANGELOG_V2.md) for detailed changes.

---

## 🎓 Learning Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [NLTK Documentation](https://www.nltk.org)
- [spaCy Guide](https://spacy.io)
- [NLP Basics](https://en.wikipedia.org/wiki/Natural_language_processing)

---

<div align="center">

**Made with ❤️ by Randhir (ManakRaj-7)**

⭐ If you find this project useful, please consider starring it on GitHub!

[⬆ Back to Top](#-nlp-inspector)

</div>