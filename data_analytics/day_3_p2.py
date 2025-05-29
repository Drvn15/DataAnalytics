from flair.models import TextClassifier
from flair.data import Sentence

def analyze_sentiment_flair(text):
    classifier = TextClassifier.load('sentiment')
    sentence = Sentence(text)
    classifier.predict(sentence)
    label = sentence.labels[0].value
    score = sentence.labels[0].score

    if label == 'POSITIVE':
        result = "Positive😊"
    elif label == 'NEGATIVE':
        result = "Negative😡"
    else:
        result = "Neutral🙄"

    print(f"Flair Sentiment: {result} (Confidence: {score:.2f})")
    return result

# Call the function when the script is run
if __name__ == "__main__":
    text = input("Enter the text to be analysed: ")
    analyze_sentiment_flair(text)
