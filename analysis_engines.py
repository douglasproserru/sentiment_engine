# Douglas Ayinebyoon +256700260555 (whats app)
import pandas as pd
import re

# I want to perform sentiment analysis using VADER and NER
# But due to Spacy and nlkt restrictions on some environments I build simple manual ones

# 1. Manual Sentiment Dictionary (Mini-VADER in my case)
#  this list can be expanded with more financial terms later on
sentiment_lexicon = {
    'bullish': 1.0, 'innovation': 0.8, 'buying': 0.5, 'accumulating': 0.5,
    'bearish': -1.0, 'pullback': -0.8, 'dumping': -1.0, 'inflation': -0.4,
    'high': 0.3, 'low': -0.3, 'growth': 0.6, 'risk': -0.5, 'support': 0.2
}


def get_manual_sentiment(text):
    score = 0
    words = text.lower().split()
    count = 0
    for word in words:
        clean_word = re.sub(r'[^\w]', '', word)  # this removes punctuation from the posts
        if clean_word in sentiment_lexicon:
            score += sentiment_lexicon[clean_word]
            count += 1
    return score / count if count > 0 else 0


def get_manual_entities(text):
    # Finding tickers (starts with $) or capitalized words (potential Companies)
    # This regex looks for words starting with $ or capitalized words not at sentence start
    tickers = re.findall(r'\$[A-Z]+', text)
    # Simple proper noun heuristic that is, capitalized words that aren't at the start of a sentence
    proper_nouns = re.findall(r'(?<!^)\b[A-Z][a-z]+\b', text)

    entities = list(set(tickers + proper_nouns))
    return ", ".join(entities) if entities else "None"


def process_manually(input_file, output_file):
    print("Reading file and processing with our simple manual NLP functions")
    df = pd.read_csv(input_file)

    # now I Apply our manual functions to our generated posts file
    df['manual_sentiment_score'] = df['text'].apply(get_manual_sentiment)
    df['manual_entities'] = df['text'].apply(get_manual_entities)

    # Saving the results
    df.to_csv(output_file, index=False)
    print(f"Success! Results saved to '{output_file}'.")


# Running the code on our file
process_manually('generated_stocktwits_posts.csv', 'manual_analyzed_posts.csv')