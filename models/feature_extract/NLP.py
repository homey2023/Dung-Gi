from transformers import BertModel, BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('path/to/save/directory')

def generate_nlp_vector(user_string):
    inputs = tokenizer(user_string, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(1).detach().numpy()
