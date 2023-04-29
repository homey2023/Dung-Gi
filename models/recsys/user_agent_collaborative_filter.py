import numpy as np
from sklearn.decomposition import NMF

class UserAgentCollaborativeFilter:
    def __init__(self, n_components):
        self.nmf = NMF(n_components=n_components)
    
    def fit(self, click_count_matrix):
        self.user_embeddings = self.nmf.fit_transform(click_count_matrix)
        self.agent_embeddings = self.nmf.components_.T
        
    def predict(self, user_ids, agent_ids):
        scores = np.sum(self.user_embeddings[user_ids] * self.agent_embeddings[agent_ids], axis=1)
        return scores
