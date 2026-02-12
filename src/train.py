# train.py

import tensorflow as tf
from config import *

def load_datasets():
    train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        TRAIN_DIR,
        labels="inferred",
        label_mode="categorical",
        color_mode="rgb",
        batch_size=BATCH_SIZE,
        image_size=IMAGE_SIZE,
        shuffle=True
    )

    val_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        VAL_DIR,
        labels="inferred",
        label_mode="categorical",
        color_mode="rgb",
        batch_size=BATCH_SIZE,
        image_size=IMAGE_SIZE,
        shuffle=False
    )

    AUTOTUNE = tf.data.AUTOTUNE
    train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
    val_dataset = val_dataset.prefetch(buffer_size=AUTOTUNE)

    return train_dataset, val_dataset


def build_model():
    base_model = tf.keras.applications.MobileNetV3Large(
        input_shape=(224, 224, 3),
        include_top=True,
        weights="imagenet",
        classes=1000,
        dropout_rate=0.2
    )

    model = tf.keras.models.Sequential([
        tf.keras.Input(shape=(224, 224, 3)),
        base_model,
        tf.keras.layers.Dense(4, activation='softmax')
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


def train():
    train_dataset, val_dataset = load_datasets()
    model = build_model()

    history = model.fit(
        train_dataset,
        validation_data=val_dataset,
        epochs=EPOCHS
    )

    model.save(MODEL_SAVE_PATH)
    print("Model saved successfully.")


if __name__ == "__main__":
    train()
