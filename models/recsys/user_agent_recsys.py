import numpy as np
from user_agent_collaborative_filter import UserAgentCollaborativeFilter
from user_agent_transformer import UserAgentTransformer

class UserAgentRecSys:
    def __init__(self, cf_n_components, transformer_config):
        self.cf = UserAgentCollaborativeFilter(n_components=cf_n_components)
        self.transformer = UserAgentTransformer(**transformer_config)

    def fit(self, click_count_matrix, user_features, agent_features):
        self.cf.fit(click_count_matrix)

    def predict(self, user_ids, agent_ids, user_features, agent_features):
        cf_scores = self.cf.predict(user_ids, agent_ids)
        transformer_scores = self.transformer(user_features, agent_features).detach().numpy()
        ensemble_scores = cf_scores + transformer_scores
        return ensemble_scores
