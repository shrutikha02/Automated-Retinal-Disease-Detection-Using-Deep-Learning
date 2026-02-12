# config.py

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 15
LEARNING_RATE = 1e-4

TRAIN_DIR = "Dataset/train"
VAL_DIR = "Dataset/val"

CLASS_NAMES = ["CNV", "DME", "DRUSEN", "NORMAL"]
MODEL_SAVE_PATH = "models/Trained_Model.h5"
