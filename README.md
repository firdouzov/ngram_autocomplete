# Azerbaijani N-Gram Autocompleter

This project is a simple yet powerful autocompletion tool for Azerbaijani news text using N-Gram language models. It supports bigram and trigram predictions to suggest the next likely word in a sentence based on historical n-gram frequencies.

## Features

- Real-time text autocompletion
- Bigram and trigram prediction support
- Fallback to bigram if trigram data is unavailable
- Simple Gradio interface for ease of use
- Laplace smoothing for better generalization
- Trained on Azerbaijani news text

## Demo

Run the app locally and start typing a sentence. The model will suggest the next word.

> Example:  
> Input: `Azərbaycan respublikası`  
> Output: `Azərbaycan respublikası prezidenti`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/az-ngrams-autocompleter.git
   cd az-ngrams-autocompleter
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not present, install the main packages manually:

bash
Copy
Edit
pip install gradio
Ensure the following files are in the project directory:

main.py

trigram.pkl.gz

bigram.pkl.gz

Run the application:

bash
Copy
Edit
python main.py
File Overview
main.py: Contains the Gradio interface and core logic for n-gram based prediction.

ngram_preprocessor.ipynb: Jupyter notebook used to preprocess and generate the bigram and trigram models.

trigram.pkl.gz / bigram.pkl.gz: Gzipped pickle files storing the frequency dictionaries.

How It Works
The user inputs a sentence.

If two or more words are entered, the model uses trigram statistics for prediction.

If only one word is entered, the model uses bigram statistics.

Laplace smoothing ensures the model can handle unseen word combinations.

The top-ranked predicted word is appended to the sentence.

Notes
This tool is trained specifically on Azerbaijani news text, and performance on other types of text may vary.

Avoid typing a space after the last word to ensure correct prediction (e.g., use Azərbaycan respublikası, not Azərbaycan respublikası ).

License
MIT License

Author
Your Name – @firdouzov


---

Let me know if you'd like to customize it further (e.g., add badges, update author info, or write a `requirements.txt`).
