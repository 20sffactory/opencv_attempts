import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # H[0,179], S[0,255], V[0,255]
    lower_blue = np.array([90,50,50]) 
    upper_blue = np.array([130,255,255]) 

    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    red_mask = mask0 + mask1

    gray = frame.copy()
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

    # Threshold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    blue_res = cv2.bitwise_and(frame,frame, mask=blue_mask)
    red_res = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('blue',blue_res)
    cv2.imshow('red', red_res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()