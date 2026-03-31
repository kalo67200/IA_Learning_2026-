
class Valeur : 
    def __init__(self, data): 
        self.data = data
        self.grad = 0.0
    
    def __repr__(self):
        return f"Valeur (date = {self.data}, grad ={self.grad})"
    
    def __add__(self, autre): 
        resultat = Valeur(self.data + autre.data)

        def backward():
            self.grad += 1.0
            autre.grad += 1.0
        
        resultat.backward = backward
        return resultat 

    def __mul__(self, autre):
        resultat = Valeur(self.data * autre.data)
    
        def backward():
            self.grad += autre.data
            autre.grad += self.data
    
        resultat.backward = backward
        return resultat



a = Valeur(2.0)
b = Valeur(3.0)

c = a + b
c.backward()
print(f"Addition - gradient a : {a.grad}, b : {b.grad}")
a.grad = 0.0
b.grad = 0.0

d = a * b
d.backward()
print(f"Multiplication - gradient a : {a.grad}, b : {b.grad}")