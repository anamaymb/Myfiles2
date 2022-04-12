import numpy as np
import cv2
import math

capture = cv2.VideoCapture(0)

while capture.isOpened():

    # Capture frames from the camera
    ret, frame = capture.read()
    # img=cv2.imread('D:\GITHUB\Myfiles2\Python\Major project\gesture\
    # Get hand data from the rectangle sub window
    cv2.rectangle(frame, (50, 350), (50, 350), (0, 255, 255), 0)

    cv2.imshow("Thresholded1", frame)
    
    crop_image = frame[1:470, 1:480]

    
    
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(crop_image, (9, 9), 0)
    cv2.imshow("Blurr", blur)
    # Change color-space from BGR -> HSV
    #"""
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Create a binary image with where white will be skin colors and rest is black
    mask2 = cv2.inRange(hsv, np.array([2, 0, 0]), np.array([20, 255, 255]))

    # Kernel for morphological transformation
    kernel = np.ones((1, 1))

    # Apply morphological transformations to filter out the background noise
    dilation = cv2.dilate(crop_image, kernel, iterations=1)
    erosion = cv2.erode(crop_image, kernel, iterations=1)
    cv2.imshow("dilation ", dilation)
    cv2.imshow("Erosion ", erosion)

    #"""
    # Close the camera if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()