import torch
import torch.nn as nn

class HybridDetector(nn.Module):
    def __init__(self, vocab_size, embed_dim=128, hidden_dim=256, num_heads=4):
        super(HybridDetector, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        
        # Bi-LSTM Layer
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        
        # Transformer Layer
        encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_dim*2, nhead=num_heads, batch_first=True)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=1)
        
        # Final Classification
        self.fc = nn.Linear(hidden_dim*2, 2) 

    def forward(self, x):
        x = self.embedding(x)
        lstm_out, _ = self.lstm(x)
        trans_out = self.transformer(lstm_out)
        pooled = torch.mean(trans_out, dim=1)
        return self.fc(pooled)
