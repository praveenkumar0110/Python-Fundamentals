'''
User input
   ↓
Pre-processing (Python)
   ↓
LLM API call (OpenAI / HF / local model)
   ↓
Post-processing (Python)
   ↓
Store / Search / Display result

'''

# Model side → torch + transformers + datasets

#Car body = transformers

#Engine = torch

#Fuel = datasets

# llm - large langauge model

#Tensor = numbers ah arrange pannina container.(multi-dimensional array)

#Pipeline = Pre-built flow for a specific NLP task


from transformers import pipeline
generator  = pipeline("text-generation", model="gpt2")
print(generator("hello"))