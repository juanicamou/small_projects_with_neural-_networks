import tensorflow as tf
import numpy as np

# Training data
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Construction of the neural network.
# There are two neurons with a sequential model.

layer = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer])

model.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

# Training
record = model.fit(celsius, fahrenheit, epochs=1000, verbose=False)

# Export
model.save('celsius_to_fahrenheit.h5')