from transformer_demo import pipeline

senitment = pipeline("sentiment-analysis")

result = senitment("I love programming!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]