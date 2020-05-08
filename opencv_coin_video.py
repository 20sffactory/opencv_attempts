import imutils
import cv2
import numpy as np
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
while True:
    _, frame = cap.read()
    frame_img = frame.copy()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.bilateralFilter(img,11,17,17)
    _,thres = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
    thres = cv2.bitwise_not(thres)
    thres = cv2.medianBlur(thres,7)
    edged = cv2.Canny(thres, 3, 180)
    cnts = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    cnt_len = 0
    for each in range(len(cnts)):
        if cv2.contourArea(cnts[each]) > 1000:
            frame_img = cv2.drawContours(frame_img, cnts, each, (255,0,0), 3)
            cnt_len += 1
    frame_txt = frame_img.copy()
    frame_txt = cv2.putText(frame_img,"Number of Coins: "+str(cnt_len),\
                (50,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0))

    cv2.imshow('frame',imutils.resize(frame_txt,width=800))
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()