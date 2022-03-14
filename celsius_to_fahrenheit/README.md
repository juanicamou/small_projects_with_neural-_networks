# Celsius to Fahrenheit Converter using TensorFlow and Keras
## Simple application which uses neural networks to convert degrees Celsius to degrees Fahrenheit.

![image](https://user-images.githubusercontent.com/28497478/157776259-0437d71b-e54c-4511-8d35-ab2fa3c4324a.png)


### Steps to run the app
1. Install Requirements: `Python 3.9.7`
2. In a terminal run `python -m http.server 8000`
3. The API will be displayed by default in http://127.0.0.1:8000/. In any case, the output of the command from point 2 shows the address of our app.

### Steps to create the neural network model

1. Run `py model_constructor.py` in model_constructor dir. The output will be: `celsius_to_farenheit.h5`.
2. Install TensorFlow.js: `pip install tensorflowjs`.
3. In the same dir run: `tensorflowjs_converter --input_format keras celsius_to_fahrenheit.h5 ../`.
4. The output will be two files: `group1-shard1of1.bin` and `model.json`.

### Jupyter notebook with step by step

`celsius_to_fahrenheit.ipynb`

> Project made following the video guide of the YouTube channel called Ringa Tech. My thanks to the channel!
