import numpy as np
from user_real_estate_collaborative_filter import UserRealEstateCollaborativeFilter
from user_real_estate_transformer import UserRealEstateTransformer

class UserRealEstateRecSys:
    def __init__(self, cf_n_components, transformer_config):
        self.cf = UserRealEstateCollaborativeFilter(n_components=cf_n_components)
        self.transformer = UserRealEstateTransformer(**transformer_config)

    def fit(self, click_count_matrix, user_features, item_features):
        self.cf.fit(click_count_matrix)

    def predict(self, user_ids, item_ids, user_features, item_features):
        cf_scores = self.cf.predict(user_ids, item_ids)
        transformer_scores = self.transformer(user_features, item_features).detach().numpy()
        ensemble_scores = cf_scores + transformer_scores
        return ensemble_scores
