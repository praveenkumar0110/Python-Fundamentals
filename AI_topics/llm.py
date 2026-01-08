from transformer_demo import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

text = "dog"

inputs = tokenizer(text, return_tensors="pt")

output = model.generate(**inputs, max_length=50)

print(tokenizer.decode(output[0], skip_special_tokens=True))
