'''
there are 2 types models
1) online models
2) offline models


online models:
nvidia cpu ,server ,  too many data to process tokens

offline models:
openai gpt-3.5 , gpt-4 , local llm models
gpt modls , gemini models
huggingface models


'''

# gpt how its works
'''
who is praveen (input)
    ↓
gpt(brain)
    ↓
tokens(processing)
    ↓
transformer
    ↓
praveen is a boy (output)
'''

# token  how to worls
'''
"who is praveen" "who",-> "is",-> "praveen"
                 "who"-> 34567
                 "is"-> 78901
                 "praveen"-> 12345
'''

# trkoenizer trsined before training the model
#vocab like dictionary evry word has a unique number
'''
"who is praveen"
    ↓
[34567, 78901, 12345]  (tokenizer)
    ↓
model processing
    ↓
[45678, 89012, 23456]  (output tokens)
    ↓   
detokenizer
    ↓
"praveen is a boy"
'''
# tokens number traine

# your text -> tokenizer -> tokens -> tokenid(number) -> model -> output tokenid -> detokenizer -> output text
# more tokens raised cost and time also increased



# how huggingface works
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


# for example code how its works( huggingface)

from transformers import AutoTokenizer 
Tokenzier = AutoTokenizer.from_pretrained("gpt2")


text = "who is praveen"


# tokenze the input text
tokens = Tokenzier.tokenize(text)
token_ids = Tokenzier.convert_tokens_to_ids(tokens)

print("orgintal text:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)
# output
'''
orgintal text: who is praveen
Tokens: ['
who', 'is', 'pr', 'ave', 'en']
Token IDs: [34567, 78901, 12345]
'''

#encoding and decoding
encoded = Tokenzier(text)
print("Encoded:", encoded)

decoded_text = Tokenzier.decode(encoded['input_ids'])
print("Decoded text:", decoded_text)
# output
'''
Encoded: {'input_ids': [34567, 78901, 12345], 'attention_mask': [1, 1, 1]}
Decoded text: who is praveen
'''

'''

orgintal text: who is praveen
Tokens: ['who', 'is', 'p', 'rave', 'en']
Token IDs: [8727, 318, 279, 5758, 268]
Encoded: {'input_ids': [8727, 318, 279, 5758, 268], 'attention_mask': [1, 1, 1, 1, 1]}
Decoded text: who is praveen


'''
