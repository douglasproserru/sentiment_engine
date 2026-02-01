#Douglas Ayinebyoona +256700260555 (WhatsApp)
import pandas as pd
import matplotlib.pyplot as plt
import re

# Loading my analyzed data
df = pd.read_csv('manual_analyzed_posts.csv')

# PLOT 1 Average Sentiment Score per Ticker ---
plt.figure(figsize=(10, 6))
# Calculate average score and sort for better visual flow
sentiment_data = df.groupby('stock_symbol')['manual_sentiment_score'].mean().sort_values()
#  setting Red bars for negative sentiment, Blue for positive
colors = ['#ff9999' if x < 0 else '#66b3ff' for x in sentiment_data]

sentiment_data.plot(kind='bar', color=colors, edgecolor='black')
plt.title('Market Sentiment: Average Manual Scores by Stock Ticker', fontsize=14, pad=15)
plt.xlabel('Stock Ticker Symbol', fontsize=12)
plt.ylabel('Average Sentiment Score (-1.0 to 1.0)', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--') # Baseline
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('average_sentiment_by_ticker.png')

#PLOT 2 Top 10 Entities Mentioned
plt.figure(figsize=(10, 6))
all_entities = []
for ent_str in df['manual_entities'].dropna():
    if ent_str != "None":
        # Supports comma or pipe separators from previous steps
        parts = re.split(r'[|,]', ent_str)
        all_entities.extend([p.strip() for p in parts if p.strip()])

entity_counts = pd.Series(all_entities).value_counts().head(10)
entity_counts.sort_values().plot(kind='barh', color='teal', edgecolor='black')

plt.title('Top 10 Most Frequently Mentioned Entities', fontsize=14, pad=15)
plt.xlabel('Number of Mentions (Total Volume)', fontsize=12)
plt.ylabel('Entity (Company Name or Ticker)', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('top_entities_frequency.png')

# PLOT 3 Distribution of Sentiment Labels
plt.figure(figsize=(8, 8))
label_counts = df['sentiment'].value_counts()
labels = [l.capitalize() for l in label_counts.index]
# High contrast colors; Green for Bullish, Red for Bearish, Gold for Neutral
pie_colors = ['#2ca02c', '#d62728', '#bcbd22']

plt.pie(label_counts, labels=labels, autopct='%1.1f%%', startangle=140,
        colors=pie_colors, explode=(0.05, 0.05, 0.05), shadow=True)

plt.title('Overall Composition of Market Opinions', fontsize=14, pad=20)
plt.tight_layout()
plt.savefig('sentiment_distribution_pie.png')

print("All three charts have been saved as PNG files.")