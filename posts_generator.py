# Douglas Ayinebyoona +256700260555(Whats App)
# I have used code to generate posts similar to those on StockTwits due to API resistrictions
# importing necessary libraries
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


def generate_social_posts(num_posts=5000):
    stocks = ['$AAPL', '$GOOGL', '$TSLA', '$NVDA']
    names = {'$AAPL': 'Apple', '$GOOGL': 'Google', '$TSLA': 'Tesla', '$NVDA': 'Nvidia'}

    # setting up our contextual fragments for building up word count naturally
    market_context = [
        "The technical indicators on the daily chart are showing some interesting patterns.",
        "Institutional buying seems to be picking up as we approach the end of the fiscal quarter.",
        "Many retail traders are watching the support levels closely before making their next big move.",
        "Earnings season is right around the corner and the market sentiment is shifting rapidly.",
        "Volume spikes today suggest that big players are either accumulating or dumping shares heavily.",
        "Macro trends like interest rates and inflation data are definitely weighing on tech valuations."
    ]

    data = []

    for i in range(num_posts):
        ticker = random.choice(stocks)
        name = names[ticker]
        sentiment = np.random.choice(['bullish', 'bearish', 'neutral'], p=[0.4, 0.3, 0.3])

        # constructing our core opinion
        if sentiment == 'bullish':
            core = f"I am very {sentiment} on {ticker}. {name} is leading the market innovation right now."
        elif sentiment == 'bearish':
            core = f"Currently feeling {sentiment} about {ticker}. I think {name} is due for a pullback soon."
        else:
            core = f"Holding a {sentiment} position on {ticker}. Just waiting for more news from {name}."

        # Combining these cores with a random market context fragment
        post_content = f"{core} {random.choice(market_context)} #stocks #investing"

        # we then Fine-tune our word count to be range from 25-35, the standard length of posts
        words = post_content.split()
        target_length = random.randint(25, 35)

        # If it is too short,then we should add a generic conclusion
        while len(words) < target_length:
            words.append(random.choice(["Watch", "the", "price", "action", "closely", "this", "week!"]))

        final_text = " ".join(words[:target_length])

        timestamp = datetime.now() - timedelta(days=random.randint(0, 30))
        # creating a dictionary to store our information.
        data.append({
            'id': i,
            'text': final_text,
            'sentiment': sentiment,
            'stock_symbol': ticker,
            'timestamp': timestamp
        })

    return pd.DataFrame(data)


# Generating and saving the posts into a file
df = generate_social_posts()
df.to_csv('generated_stocktwits_posts.csv', index=False)

print(f"File 'generated_stocktwits_posts.csv' created with {len(df)} posts.")
print(f"Average words per post: {df['text'].apply(lambda x: len(x.split())).mean():.1f}")
