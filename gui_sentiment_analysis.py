import tkinter as tk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment():
    text = text_input.get("1.0", "end-1c")  # Get input text
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    sentiment = 'Positive' if score['compound'] >= 0.05 else 'Negative' if score['compound'] <= -0.05 else 'Neutral'
    result_label.config(text=f"Sentiment: {sentiment}\nScores: {score}")

window = tk.Tk()
window.title("Sentiment Analysis Tool")

text_input = tk.Text(window, height=10, width=50)
text_input.pack()

analyze_button = tk.Button(window, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack()

result_label = tk.Label(window, text="Sentiment: N/A")
result_label.pack()

window.mainloop()
