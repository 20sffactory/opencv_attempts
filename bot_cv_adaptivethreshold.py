import imutils
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 5)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
  _, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray = gray[0:620, 0:960]

  #gray = cv2.GaussianBlur(gray, (21,21), 0)
  otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
  adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 79, 10)
  adaptive = cv2.medianBlur(adaptive, 25)

  cv2.imshow('bgr2gray', imutils.resize(gray, width=800))
  #cv2.imshow('otsu', imutils.resize(otsu, width=300))
  cv2.imshow('adaptivethreshold', imutils.resize(adaptive, width=800))
  k = cv2.waitKey(1) & 0xFF
  if k == 27:
    break

cv2.destroyAllWindows()