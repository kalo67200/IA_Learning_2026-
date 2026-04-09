import torch 
import torch.nn as nn 

X = torch.tensor([[0.],[1.],[2.],[3.],[4.]])
y = torch.tensor([[0.],[0.],[1.],[1.],[1.]])


modele = nn.Sequential(
    nn.Linear(1,4),
    nn.ReLU(),
    nn.Linear(4,1), 
    nn.Sigmoid()
)

criterion = nn.BCELoss()
optimizer = torch.optim.Adam(modele.parameters(), lr = 0.1)

for epoch in range (100): 
    prediction = modele(X)
    loss = criterion (prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


for i in range (6): 
    pred = modele(torch.tensor([[float (i)]])).item()
    print ( f" X : {i} -> {pred:.2f}")