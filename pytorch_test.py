import torch

x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print(x)
print(x * 2)
print(x.mean())

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x*2
z = y.sum()
z.backward()
print(x.grad)
