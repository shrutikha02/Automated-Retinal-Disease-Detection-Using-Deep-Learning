# predict.py

import tensorflow as tf
import numpy as np
from config import *
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input


def load_model():
    model = tf.keras.models.load_model(MODEL_SAVE_PATH)
    return model


def predict_image(image_path):
    model = load_model()

    img = tf.keras.utils.load_img(image_path, target_size=IMAGE_SIZE)
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    result_index = np.argmax(preds)
    predicted_class = CLASS_NAMES[result_index]

    print("Confidence Scores:", preds[0])
    print("Predicted Class:", predicted_class)

    return predicted_class


if __name__ == "__main__":
    image_path = "test/DRUSEN/DRUSEN-1112835-7.jpeg"
    predict_image(image_path)

