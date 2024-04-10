import tkinter as tk
from nltk.sentiment import SentimentIntensityAnalyzer

# Function to analyze sentiment
def analyze_sentiment():
    text = text_input.get("1.0", "end-1c")  # Get input text
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    sentiment = 'Positive' if score['compound'] >= 0.05 else 'Negative' if score['compound'] <= -0.05 else 'Neutral'
    result_label.config(text=f"Sentiment: {sentiment}\nScores: {score}")

# Set up the GUI window
window = tk.Tk()
window.title("Sentiment Analysis Tool")

# Text input area
text_input = tk.Text(window, height=10, width=50)
text_input.pack()

# Analyze button
analyze_button = tk.Button(window, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack()

# Result display area
result_label = tk.Label(window, text="Sentiment: N/A")
result_label.pack()

# Run the application
window.mainloop()
