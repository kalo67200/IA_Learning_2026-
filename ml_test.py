import numpy as np 
from sklearn.linear_model import LinearRegression 

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 7, 9])

modele = LinearRegression()
modele.fit(X,y)


prediction = modele.predict([[6]])
print(f"Si j'étudie 6h -> note prédite : {prediction[0]:.1f}")