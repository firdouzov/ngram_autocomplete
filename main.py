import pickle
import gradio as gr
import gzip

with gzip.open('trigram.pkl.gz', 'rb') as f:
    trigram = pickle.load(f)

with gzip.open('bigram.pkl.gz', 'rb') as f:
    bigram = pickle.load(f)


def probability(word, prev_words, ngram, nmingram, k):
    """
    Calculate smoothed probability of a word given previous words using Laplace smoothing
    
    :param word: The word to calculate probability for
    :param prev_words: Tuple of previous words (context)
    :param ngram: Dictionary of n-gram counts
    :param nmingram: Dictionary of (n-1)-gram counts
    :param k: Smoothing parameter
    
    :return: Smoothed probability value
    """
    nominator = ngram.get((*prev_words, word), 0) + k
    vocab_size = len(set(w for ngram_key in nmingram for w in ngram_key))
    denominator = nmingram.get(prev_words, 0) + k * vocab_size
    return nominator / denominator

def all_prob(prev_words, ngram):
    """
    Calculate probability distribution for all possible next words given context
    
    :param prev_words: Tuple of previous words (context)
    :param ngram: Dictionary of n-gram counts
    
    :return: Dictionary mapping n-grams to their probabilities
    """
    filtered = {k: v for k, v in ngram.items() if k[:len(prev_words)] == prev_words}
    total = sum(filtered.values())
    return {k: v / total for k, v in filtered.items()}

def predict_bigram(words, bigram):
    """
    Predict next word using bigram model
    
    :param words: List of words in current sentence
    :param bigram: Bigram frequency dictionary
    
    :return: Complete sentence with predicted next word
    """
    if len(words) >= 1:
        context = (words[-1].lower(),)
        probabilities = all_prob(context, bigram)
        sorted_probs = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))
        for k, v in sorted_probs.items():
            next_word = k[-1]
            if next_word not in {'<UNK>', "''", '"', '(', ')'}:
                return ' '.join(words + [next_word])
    return ' '.join(words)

def predict(sentence, bigram=None, trigram=None):
    """
    Predict next word using trigram model with bigram fallback
    
    :param sentence: Input sentence string
    :param bigram: Bigram frequency dictionary
    :param trigram: Trigram frequency dictionary
    
    :return: Complete sentence with predicted next word
    """
    words = sentence.split(' ')
    
    # Use bigram for single word input
    if len(words)==1:
        sentence = predict_bigram(words=words,bigram=bigram)
    elif len(words)==0:
        raise ValueError("Need at least one word for bigram prediction")
    else:
        # Try trigram prediction first
        context = tuple(word.lower() for word in words[-2:])
        probabilities = all_prob(context, trigram)
        sorted_probs = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))
        
        # If trigram has predictions, use them
        if len(sorted_probs)!=0:
            for k, v in sorted_probs.items():
                next_word = k[-1]
                if next_word not in {'<UNK>', "''", '"', '(', ')'}:
                    sentence = ' '.join(words + [next_word])
        else:
            # Fall back to bigram if no trigram predictions
            sentence = predict_bigram(words=words,bigram=bigram)
    
    return sentence

def autocomplete(input_text):
    """
    Main autocomplete function that wraps the prediction logic
    
    :param input_text: User's input text
    
    :return: Input text with suggested next word appended
    """
    return predict(input_text, bigram=bigram, trigram=trigram)


with gr.Blocks(title="N-Gram Autocompleter") as interface:
    gr.Markdown("# N-Gram Autocompleter")
    gr.Markdown("Type a few words and get real-time autocomplete Azerbaijani News text suggestions using a ngram model. Please don't write spacings after words like 'Azərbaycan respublikası ' use 'Azərbaycan respublikası'")
    
    with gr.Row():
        with gr.Column():

            input_box = gr.Textbox(
                label="Start typing...", 
                placeholder="Type a sentence...", 
                lines=3,
                autofocus=True
            )
            

            suggestion_display = gr.Textbox(
                label="Suggested completion:",
                interactive=False,
                lines=1
            )
    
    input_box.change(
        fn=autocomplete,
        inputs=input_box,
        outputs=suggestion_display,
        show_progress=False  
    )

interface.launch(share=False)
