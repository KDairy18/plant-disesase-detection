import os
import tensorflow as tf

# Verify model file existence
model_path = "detection2.h5"
if os.path.exists(model_path):
    print("Model file exists.")
else:
    print("Model file not found.")

# Load the model if it exists
if os.path.exists(model_path):
    # Load the model
    MODEL = tf.keras.models.load_model(model_path)
    print("Model loaded successfully.")
else:
    print("Model file not found.")
