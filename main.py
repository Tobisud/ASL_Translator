import cv2
from picamera2 import Picamera2
import mediapipe as mp
import numpy as np
import math
import os
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

# Initialize Camera
piCam=Picamera2()
piCam.preview_configuration.main.size=(1280,980)
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

# Detects 1 hand
detector = HandDetector(maxHands=1)

# Load pre-trained Keras model and label file for gesture classification
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# Offset controls padding around the hand's bounding box for the model
offset = 20
imgSize = 300

# Define the gesture labels corresponding to the model's output. These labels represent ASL digits (0-9)
labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Continuously capture frames, process for hand gestures, and classify them
while True:
    # Capture a single frame from the camera and flip it horizontally for a mirror effect
    img = frame=piCam.capture_array()
    img= cv2.flip(frame, 1)
    imgOutput = img.copy()

    #Detect hands in the current frame. If a hand is detected, extract its bounding box
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        # Prepare a blank white canvas to fit the cropped hand image
        # This ensures the input matches the model's expected input size
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        try:
            # Crop the region around the detected hand with some padding (offset)
            imgCropShape = imgCrop.shape
            aspectRatio = h / w

            # Resize the cropped hand image to fit the white canvas while maintaining the aspect ratio
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                # If the width is greater than or equal to the height
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)

            # Display the classification result above the detected hand
            cv2.rectangle(imgOutput, (x - offset, y - offset-50),
                          (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)

        # Handle errors when the hand is not fully within the frame or cropping fails
        except Exception as e:
            print("Hand is out of detection range !!!")

        # Draw the bounding box around the detected hand on the output frame
        cv2.rectangle(imgOutput, (x-offset, y-offset),
                      (x + w+offset, y + h+offset), (255, 0, 255), 4)

        #cv2.imshow("ImageCrop", imgCrop)
        #cv2.imshow("ImageWhite", imgWhite)
        
        

    cv2.imshow("Image", imgOutput)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the PiCamera and close all OpenCV windows
piCam.close()
cv2.destroyAllWindows()
