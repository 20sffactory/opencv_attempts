import imutils
import cv2
import numpy as np

def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cap.set(3,240)
cap.set(4,160)
cv2.namedWindow("thresh")
cv2.createTrackbar("Threshold Value","thresh",80,255,nothing)

while True:
    thresh_value = cv2.getTrackbarPos("Threshold Value","thresh")
    _,frame = cap.read()
    img = frame.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,img_thresh = cv2.threshold(img_gray,thresh_value,255,cv2.THRESH_BINARY)
    img_thresh_inv = cv2.bitwise_not(img_thresh)
    img_thresh_inv = cv2.medianBlur(img_thresh_inv, 5)
    cnts = cv2.findContours(img_thresh_inv,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    img_thresh_canvas = cv2.cvtColor(img_thresh,cv2.COLOR_GRAY2RGB)
    for each in range(len(cnts)):
        if cv2.contourArea(cnts[each]) > 100:
            if cv2.contourArea(cnts[each]) < 800:
                img_thresh_canvas = cv2.drawContours(img_thresh_canvas, cnts, each, (128,128,0), 4)
    cv2.imshow("thresh", img_thresh_canvas)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()