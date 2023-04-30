import numpy as np
from sklearn.decomposition import NMF

def matrix_factorize_user_embedding(user_real_estate_clicks, user_agent_clicks, n_components=2):
    nmf_real_estate = NMF(n_components=n_components)
    nmf_agent = NMF(n_components=n_components)
    
    user_real_estate_embeddings = nmf_real_estate.fit_transform(user_real_estate_clicks)
    user_agent_embeddings = nmf_agent.fit_transform(user_agent_clicks)
    
    user_embeddings = np.concatenate((user_real_estate_embeddings, user_agent_embeddings), axis=1)
    return user_embeddings
