# sentiment_engine
Generates 5000 posts simulating those on Stock Twits, then performs sentiment analysis on them using VADER and Named Entity Recognition (NER). Then outputs visualizations on the analyzed data. 
# Financial Sentiment Analysis and NER Pipeline
**Developer.** Douglas Ayinebyoona  
**Contact.** +256700260555 (WhatsApp)

##  Project Overview
This project provides a complete end-to-end pipeline for generating and analyzing financial social media data. It simulates a high-volume environment by creating 5,000 synthetic posts modeled after platforms like StockTwits.

### The lightweight Solution
In many production or restricted cloud environments, heavy NLP libraries like `spaCy` or `nltk` cannot be installed due to memory limits or security restrictions. This project solves that problem by implementing a **Manual NLP Engine** using only Python's simple standard libraries and `Regex`.

---

## My project layout or architecture
The project is divided into three modular scripts to ensure clean code and easy debugging:

1. **`posts_generator.py`**. 
   - Generates 5,000 unique posts.
   - Includes market context fragments and realistic stock tickers ($AAPL, $GOOGL, $TSLA, $NVDA).
   - Simulates Bullish, Bearish, and Neutral sentiments.

2. **`analysis_engines.py`**. 
   - **Sentiment Analysis**. Uses a custom weighted dictionary (Lexicon) to score financial terminology.
   - **NER (Named Entity Recognition)**: Uses Regular Expressions to extract tickers and company names without needing a heavy pre-trained model.

3. **`visualisations.py`**.
   - Transforms raw CSV data into professional visual reports.
   - Generates charts for Ticker Sentiment, Entity Frequency, and Opinion Distribution.



## how to get Started

### Prerequisites
You only need basic Python and the following data science libraries;
pandas, matplotlib
pip install pandas matplotlib numpy
### the order of running these files
python posts_generator.py
python analysis_engines.py
python visualisations.py
