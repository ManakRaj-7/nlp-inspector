# 🚀 Project Version Control Guide

## Current Git Setup

### **Branches:**
- **master** ✅ - Version 1 (Stable, working version)
- **development** 🔧 - Version 2+ (New ambitious features)

### **How to Use:**

#### **Switch to Version 1 (Stable):**
```bash
git checkout master
```

#### **Switch to Development (New Features):**
```bash
git checkout development
```

#### **View all commits:**
```bash
git log --oneline
```

#### **View current branch:**
```bash
git branch
```

---

## Version 1 Status ✅
**Commit:** `3d2c65c`  
**Status:** Stable & Working  
**Features:**
- Text cleaning (lowercase, remove punctuation, tokenize)
- Word frequency analysis
- Sentiment analysis (TextBlob)
- Word statistics (total & unique words)
- Top 10 keywords extraction
- Bar chart visualization
- Basic UI with Streamlit

---

## Version 2 (Development) - In Progress 🚀
Currently on `development` branch. Ready to implement:

### **Phase 1: UI/UX Overhaul**
- Custom styling and themes
- Sidebar navigation
- Dark mode toggle
- Improved layout

### **Phase 2: Advanced NLP**
- Named Entity Recognition (NER)
- Part-of-Speech Tagging
- Word Cloud Visualization
- N-gram Analysis
- Readability Scores

### **Phase 3: Advanced Features**
- Text Comparison
- Export to CSV/PDF
- Language Detection
- Batch Processing
- Real-time Analysis

---

## Important Git Commands:

```bash
# Check current branch
git branch

# See differences between branches
git diff master development

# Merge development into master (when ready)
git checkout master
git merge development

# Create a new branch
git branch feature/name

# Commit changes
git add .
git commit -m "Description of changes"

# View commit history
git log --oneline

# Undo changes (go back to last commit)
git reset --hard HEAD
```

---

## Tips:
- **Always commit** before switching branches
- **Keep master stable** - only merge tested code
- **Use descriptive commit messages** for easy tracking
- **Development branch** is for experimenting with new features
