# 🇦🇿 Azerbaijani N-Gram Autocompleter

A real-time word prediction tool trained on Azerbaijani news text using N-Gram models (bigram and trigram). It suggests the next word based on the current sentence context using Laplace-smoothed probabilities.

Project URL: [Huggingface URL]((https://huggingface.co/spaces/firdouzov/autocompleter)

---

## ✨ Features

- 🔤 Bigram and trigram next-word prediction  
- 🧠 Laplace smoothing for unseen combinations  
- 🌐 Gradio interface for easy interaction  
- 📚 Trained on Azerbaijani news corpora  
- 🧪 Jupyter notebook for preprocessing  

---

## 🚀 Demo

> Input: `Azərbaycan respublikası`  
> Output: `Azərbaycan respublikası ərəb`

![Alt text](/autocomplete.png?raw=true "Screenshot Title")

Start typing any phrase related to Azerbaijani news, and the model will suggest the most probable next word.

⚠️ **Note**: Do not include trailing spaces after words. Example:  
✅ `Azərbaycan respublikası`  
❌ `Azərbaycan respublikası `

---

## 🛠️ Installation

```bash
git clone https://github.com/firdouzov/ngrams_autocomplete.git
cd az-ngrams-autocompleter
```

### Install dependencies

If you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install gradio
```

---

## 📁 Project Structure

ngram-autocompleter/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── ngram_preprocessor.ipynb # Data preprocessing notebook
├── trigram.pkl.gz         # Trained trigram model (not uploaded)
├── bigram.pkl.gz          # Trained bigram model (not uploaded)
└── README.md              # This file

---
## 🌐 Deployment
Hugging Face Spaces
- This project is designed to be deployed on Hugging Face Spaces:
- 1. Create a new Space on Hugging Face
- 2. Upload all project files including model files
- 3. The app will automatically deploy with a permanent URL
   
---

## 🧠 How It Works

- If only **1 word** is entered → uses **bigram model**  
- If **2+ words** are entered → tries **trigram model**, falls back to **bigram** if needed  
- Uses Laplace smoothing for better prediction accuracy  
- Gradio provides the interactive web UI  

---

## 📊 Model Information

- The n-gram models were trained on the LocalDoc/news_azerbaijan dataset from Hugging Face. The preprocessing pipeline includes:
- * Text tokenization using NLTK
- * Lowercasing
- * Vocabulary filtering (threshold: 300 occurrences)
- * Unknown token handling (<UNK>)
- * Start/end tokens (<s>, </s>)

---
## Model Statistics
- * Vocabulary size: Filtered based on frequency threshold
- * N-gram orders: Unigram, Bigram, and Trigram
- * Smoothing: Laplace smoothing with k=1
---

## ▶️ Run the App

```bash
python main.py
```

This launches the Gradio web interface locally.

---

## 👤 Author

**Aydin Firdouzov**  
GitHub: [@firdouzov](https://github.com/firdouzov)

---

## 🙌 Acknowledgements
- Dataset: [LocalDoc/news_azerbaijan](https://huggingface.co/datasets/LocalDoc/news_azerbaijan)
- Built with [Gradio](https://gradio.app)  
- Inspired by traditional NLP N-Gram models  
