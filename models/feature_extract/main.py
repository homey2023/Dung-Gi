import numpy as np
from get_feature import concatenate_vectors
from matrix_factorize_user_embedding import matrix_factorize_user_embedding
from NLP import generate_nlp_vector
from train_NLP import train_NLP_model
from transformers import BertModel

def main():
    # Train the NLP model
    train_NLP_model()

    # Load the trained model
    model = BertModel.from_pretrained('path/to/save/directory')

    # Get user string, personal information, and click matrices
    user_string = "Example user string"
    personal_info_vector = np.array([1, 2, 3])  # Replace with real personal information vector
    user_real_estate_clicks = np.random.rand(10, 5)  # Replace with real user-real estate click matrix
    user_agent_clicks = np.random.rand(10, 5)  # Replace with real user-estate agent click matrix

    # Generate NLP vector and user embedding vector
    nlp_vector = generate_nlp_vector(user_string)
    user_embedding_vector = matrix_factorize_user_embedding(user_real_estate_clicks, user_agent_clicks)

    # Get the specific user_embedding_vector for a user (example: user index 0)
    specific_user_embedding_vector = user_embedding_vector[0]

    # Concatenate the vectors
    final_vector = concatenate_vectors(personal_info_vector, nlp_vector, specific_user_embedding_vector)

    print("Final concatenated vector:", final_vector)

if __name__ == "__main__":
    main()
