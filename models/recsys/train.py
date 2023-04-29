import torch
import numpy as np
from torch.utils.data import DataLoader
from user_real_estate_recsys import UserRealEstateRecSys
from user_agent_recsys import UserAgentRecSys
from dataset import UserRealEstateDataset, UserAgentDataset

def train_real_estate_model(model, dataloader, epochs, optimizer, criterion, device):
    model.train()
    for epoch in range(epochs):
        epoch_loss = 0
        for user_features, item_features, labels in dataloader:
            user_features, item_features, labels = user_features.to(device), item_features.to(device), labels.to(device)
            optimizer.zero_grad()
            predictions = model.transformer(user_features, item_features)
            loss = criterion(predictions, labels)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        print(f'Epoch {epoch + 1}/{epochs}, Loss: {epoch_loss / len(dataloader)}')

def train_agent_model(model, dataloader, epochs, optimizer, criterion, device):
    model.train()
    for epoch in range(epochs):
        epoch_loss = 0
        for user_features, agent_features, labels in dataloader:
            user_features, agent_features, labels = user_features.to(device), agent_features.to(device), labels.to(device)
            optimizer.zero_grad()
            predictions = model.transformer(user_features, agent_features)
            loss = criterion(predictions, labels)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        print(f'Epoch {epoch + 1}/{epochs}, Loss: {epoch_loss / len(dataloader)}')

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

    real_estate_dataset = UserRealEstateDataset()  # Implement this dataset class
    agent_dataset = UserAgentDataset()  # Implement this dataset class

    real_estate_dataloader = DataLoader(real_estate_dataset, batch_size=32, shuffle=True)
    agent_dataloader = DataLoader(agent_dataset, batch_size=32, shuffle=True)

    epochs = 10
    real_estate_optimizer = torch.optim.Adam(real_estate_model.transformer.parameters(), lr=0.001)
    agent_optimizer = torch.optim.Adam(agent_model.transformer.parameters(), lr=0.001)

    criterion = torch.nn.MSELoss()

    train_real_estate_model(real_estate_model, real_estate_dataloader, epochs, real_estate_optimizer, criterion, device)
    train_agent_model(agent_model, agent_dataloader, epochs, agent_optimizer, criterion, device)

    torch.save(real_estate_model.state_dict(), 'real_estate_model.pth')
    torch.save(agent_model.state_dict(), 'agent_model.pth')
