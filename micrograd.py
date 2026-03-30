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

    
    def __mul__(self,autre):
        return Valeur(self.data * autre.data)
    

a = Valeur(2.0)
b = Valeur(3.0)
c = a + b 
d = a * b 

print (c)
print (d)

c.backward()
print(f"Gradient de a : {a.grad}")
print(f"Gradient de b : {b.grad}")