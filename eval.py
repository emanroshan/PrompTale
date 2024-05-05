import torch
from sentence_transformers import SentenceTransformer, util

def get_most_similar(texts, prompt):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    # creating embeddings
    text_embeddings = model.encode(texts, convert_to_tensor=True).to('mps')
    prompt_embedding = model.encode(prompt, convert_to_tensor=True).to('mps')
    # finding cosine similarity
    cosine_similarities = util.pytorch_cos_sim(prompt_embedding, text_embeddings).to('mps')
    most_similar_index = torch.argmax(cosine_similarities).item()
    # print the best response index
    print('most similar response to the prompt = ', most_similar_index)
    # returning the most similar index
    return texts[most_similar_index]
