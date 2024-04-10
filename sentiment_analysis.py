from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    print("Sentiment scores:", score)
    if score['compound'] >= 0.05:
        return 'Positive'
    elif score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    text_input = input("Enter text for sentiment analysis: ")
    result = analyze_sentiment(text_input)
    print("Sentiment:", result)
