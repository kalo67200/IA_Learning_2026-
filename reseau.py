import tensorflow as tf 
import numpy as np 

X = np.array([[0],[1],[2],[3],[4]], dtype = float)
y = np.array([0, 0, 1, 1, 1], dtype = float )

model = tf.keras.Sequential([
    tf.keras.layers.Dense (4, activation ='relu', input_shape=(1,)),
    tf.keras.layers.Dense (1, activation = 'sigmoid')
])

model.compile(optimizer ='adam', loss = 'binary_crossentropy')
model.fit(X, y, epochs = 100, verbose= 0)

for i in range (6):
    pred = model.predict(np.array([[i]]), verbose=0)[0][0]
    print(f"X={i} -> {pred:.2f}")
