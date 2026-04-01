class Valeur:
    def __init__(self, data):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set()

    def __repr__(self):
        return f"Valeur(data={self.data}, grad={self.grad})"

    def __add__(self, autre):
        resultat = Valeur(self.data + autre.data)
        resultat._prev = {self, autre}

        def backward():
            self.grad += 1.0 * resultat.grad
            autre.grad += 1.0 * resultat.grad

        resultat._backward = backward
        return resultat

    def __mul__(self, autre):
        resultat = Valeur(self.data * autre.data)
        resultat._prev = {self, autre}

        def backward():
            self.grad += autre.data * resultat.grad
            autre.grad += self.data * resultat.grad

        resultat._backward = backward
        return resultat

    def backprop(self):
        ordre = []
        visites = set()

        def construire(v):
            if v not in visites:
                visites.add(v)
                for parent in v._prev:
                    construire(parent)
                ordre.append(v)

        construire(self)
        self.grad = 1.0
        for v in reversed(ordre):
            v._backward()


x = Valeur(2.0)
w = Valeur(0.5)
b = Valeur(1.0)

temp = w * x
output = temp + b

output.backprop()

print(f"Gradient de w : {w.grad}")
print(f"Gradient de x : {x.grad}")
print(f"Gradient de b : {b.grad}")