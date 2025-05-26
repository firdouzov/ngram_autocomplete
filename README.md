# 🇦🇿 Azerbaijani N-Gram Autocompleter

A real-time word prediction tool trained on Azerbaijani news text using N-Gram models (bigram and trigram). It suggests the next word based on the current sentence context using Laplace-smoothed probabilities.



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
> Output: `Azərbaycan respublikası prezidenti`

Start typing any phrase related to Azerbaijani news, and the model will suggest the most probable next word.

⚠️ **Note**: Do not include trailing spaces after words. Example:  
✅ `Azərbaycan respublikası`  
❌ `Azərbaycan respublikası `

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/az-ngrams-autocompleter.git
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

## 📁 Files

| File                      | Description                                                        |
|---------------------------|--------------------------------------------------------------------|
| `main.py`                 | Main app: loads models, computes probabilities, Gradio UI          |
| `ngram_preprocessor.ipynb`| Jupyter notebook to generate n-gram models from text corpus        |
| `bigram.pkl.gz`           | Gzipped pickle of bigram frequency dictionary                      |
| `trigram.pkl.gz`          | Gzipped pickle of trigram frequency dictionary                     |

---

## 🧠 How It Works

- If only **1 word** is entered → uses **bigram model**  
- If **2+ words** are entered → tries **trigram model**, falls back to **bigram** if needed  
- Uses Laplace smoothing for better prediction accuracy  
- Gradio provides the interactive web UI  

---

## ▶️ Run the App

```bash
python main.py
```

This launches the Gradio web interface locally.

---

## 🪪 License

MIT License. See `LICENSE` file for details.

---

## 👤 Author

**Your Name**  
GitHub: [@yourusername](https://github.com/yourusername)

---

## 🙌 Acknowledgements

- Built with [Gradio](https://gradio.app)  
- Inspired by traditional NLP N-Gram models  
