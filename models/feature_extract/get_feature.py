import numpy as np

def concatenate_vectors(personal_info_vector, nlp_vector, user_embedding_vector):
    return np.concatenate((personal_info_vector, nlp_vector, user_embedding_vector))
