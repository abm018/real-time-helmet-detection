import tensorflow as tf
import numpy as np
import cv2

# Define the function to retrieve class labels
def get_class_label_from_index(index):
    labels = ['helmet', 'no_helmet'] # Replace with your own class labels
    return labels[index]

# Load the pre-trained model
model = tf.keras.models.load_model('helmet_detector.model')

# Load the image data
img = cv2.imread('ttt.jpeg')

# Preprocess the image
img = cv2.resize(img, (224, 224))
img = img / 255.0
img = np.expand_dims(img, axis=0)

# Pass the image through the model
prediction = model.predict(img)

# Analyze the output
class_idx = np.argmax(prediction[0])
class_label = get_class_label_from_index(class_idx)
confidence = prediction[0][class_idx]

print('Class:', class_label)
print('Confidence:', confidence)
