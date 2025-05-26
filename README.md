# N-Gram Autocompleter for Azerbaijani News Text

A real-time text autocomplete system built using n-gram language models trained on Azerbaijani news data. The application provides word suggestions as you type, helping users complete sentences in Azerbaijani.

![N-Gram Autocompleter Demo]

## 🚀 Features

- **Real-time autocomplete**: Suggestions update instantly as you type
- **Trigram/Bigram models**: Uses trigram model with bigram fallback for better predictions
- **Azerbaijani language support**: Specifically trained on Azerbaijani news corpus
- **Web interface**: Built with Gradio for easy interaction
- **Smoothing techniques**: Implements Laplace smoothing for handling unseen n-grams

## 📋 Requirements

- Python 3.8+
- Required packages listed in `requirements.txt`

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ngram-autocompleter.git
cd ngram-autocompleter
