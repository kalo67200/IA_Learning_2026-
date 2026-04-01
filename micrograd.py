
class Valeur : 
    def __init__(self, data): 
        self.data = data
        self.grad = 0.0
    
    def __repr__(self):
        return f"Valeur (date = {self.data}, grad ={self.grad})"
    
    def __add__(self, autre): 
        resultat = Valeur(self.data + autre.data)

        def backward():
            self.grad += 1.0* resultat.grad
            autre.grad += 1.0 * resultat.grad 
        
        resultat.backward = backward
        return resultat 

    def __mul__(self, autre):
        resultat = Valeur(self.data * autre.data)
    
        def backward():
            self.grad += autre.data * resultat.grad
            autre.grad += self.data * resultat.grad 
    
        resultat.backward = backward
        return resultat


x = Valeur(2.0)
w = Valeur(0.5)
b = Valeur(1.0)

output = w * x + b 
print(f"output: {output}")

temp = w * x      
output = temp + b  
output.grad = 1.0 

output.backward()  
temp.backward()    
print(f"Gradient de w : {w.grad}")
print(f"Gradient de x : {x.grad}")
print(f"Gradient de b : {b.grad}")


