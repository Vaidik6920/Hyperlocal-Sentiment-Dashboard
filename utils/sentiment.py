from textblob import TextBlob

def analyze_sentiment(df):
    def label_sentiment(text):
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"

    df["sentiment_label"] = df["content"].apply(label_sentiment)
    return df

