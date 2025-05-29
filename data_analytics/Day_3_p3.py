from transformers import pipeline

def simple_sentiment_analysis():

    classifier = pipeline("sentiment-analysis")


    text = input("Enter a sentence to analyze sentiment: ")
    result = classifier(text)[0]


    print(f"Sentiment: {result['label']}")
    print(f"Confidence Score: {result['score']:.2f}")


simple_sentiment_analysis()
