from transformers import pipeline


sentiment_analyzer = pipeline("sentiment-analysis")


result = sentiment_analyzer("i love dog")
result = sentiment_analyzer("i hate dog")
result = sentiment_analyzer("This phone works just okay")

print(result)