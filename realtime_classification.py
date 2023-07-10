import tensorflow as tf
import numpy as np
import cv2
import os
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)

engine.setProperty('volume', 0.8)

text = 'please wear helmet'

# Define the function to retrieve class labels
def get_class_label_from_index(index):
    labels = ['helmet', 'no_helmet'] # Replace with your own class labels
    return labels[index]

# Load the pre-trained model
model = tf.keras.models.load_model('helmet_detector.model')

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Set the video capture resolution
cap.set(3, 640)
cap.set(4, 480)

# Loop through each frame from the camera
while True:
    # Read the current frame from the camera
    ret, frame = cap.read()

    # Preprocess the image
    img = cv2.resize(frame, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Pass the image through the model
    prediction = model.predict(img)
    # [[0.325, 0.675]]
    # Analyze the output
    class_idx = np.argmax(prediction[0])
    class_label = get_class_label_from_index(class_idx)
    if class_label == 'no_helmet':
        engine.say(text)
        engine.runAndWait()
        # os.system("say 'Please wear helmet'")
    confidence = prediction[0][class_idx]

    # Draw the predicted class label and confidence on the image
    # text = f"{class_label} {confidence:.2f}"
    # cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Show the image with the predicted label
    # cv2.imshow('Real-time Image Classification', frame)

    # Exit the program when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
