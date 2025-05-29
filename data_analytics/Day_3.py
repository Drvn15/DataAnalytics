from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_textblob(text):
 sentiment = TextBlob(text). sentiment.polarity
 print(sentiment)

 if sentiment > 0:
  return "Positive😊"
 elif sentiment < 0:
  return "Negative😡"
 else:
  return "Neutral🙄"

def analyze_sentiment_vader(text):
 analyzer = SentimentIntensityAnalyzer()
 sentiment = analyzer.polarity_scores(text) ["compound"]

 if sentiment > 0.05:
  return "Positive😊"
 elif sentiment < -0.05:
  return "Negative😡"
 else:
  return "Neutral🙄"

def analyze_input():
 text = input("Enter the text to be analysed: ")
 print(f"Text Blob Sentiment : {analyze_sentiment_textblob(text)}")
 print(f"Vader Sentiment : {analyze_sentiment_vader(text)}")

analyze_input()


