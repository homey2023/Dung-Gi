import torch
import numpy as np
from user_real_estate_recsys import UserRealEstateRecSys
from user_agent_recsys import UserAgentRecSys

def infer_real_estate_model(model, user_ids, item_ids, user_features, item_features):
    model.eval()
    with torch.no_grad():
        ensemble_scores = model.predict(user_ids, item_ids, user_features, item_features)
    return ensemble_scores

def infer_agent_model(model, user_ids, agent_ids, user_features, agent_features):
    model.eval()
    with torch.no_grad():
        ensemble_scores = model.predict(user_ids, agent_ids, user_features, agent_features)
    return ensemble_scores

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    cf_n_components = 10
    transformer_config = {
        'num_user_features': 10,
        'num_item_features': 20,
        'hidden_dim': 64,
        'num_heads': 8,
        'num_layers': 4,
        'dropout': 0.1
    }
    real_estate_model = UserRealEstateRecSys(cf_n_components, transformer_config).to(device)
    agent_model = UserAgentRecSys(cf_n_components, transformer_config).to(device)

    real_estate_model.load_state_dict(torch.load('real_estate_model.pth'))
    agent_model.load_state_dict(torch.load('agent_model.pth'))

    # Example input data
    user_ids = np.array([0, 1, 2])
    item_ids = np.array([0, 1, 2])
    user_features = torch.randn(len(user_ids), transformer_config['num_user_features'])
    item_features = torch.randn(len(item_ids), transformer_config['num_item_features'])

    agent_ids = np.array([0, 1, 2])
    agent_features = torch.randn(len(agent_ids), transformer_config['num_item_features'])

    real_estate_scores = infer_real_estate_model(real_estate_model, user_ids, item_ids, user_features, item_features)
    agent_scores = infer_agent_model(agent_model, user_ids, agent_ids, user_features, agent_features)

    print("Real estate scores:", real_estate_scores)
    print("Agent scores:", agent_scores)
