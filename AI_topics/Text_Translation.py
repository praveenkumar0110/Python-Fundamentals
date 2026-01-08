from transformers import pipeline

# English → Tamil multilingual model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-mul")

text = "naan avan illai?"
result = translator(text, tgt_lang="ta")   # specify Tamil (ta)
print(result[0]['translation_text'])
