import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    blur = cv2.medianBlur(hsv, (11))
    #blur = cv2.GaussianBlur(hsv, (11,11),0)
    lower_range = np.array([92,0,102])
    upper_range = np.array([140,71,255])
    mask = cv2.inRange(blur,lower_range,upper_range)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    #contours, hierarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #output = cv2.drawContours(res,contours,-1,(0,255,0),3)
    cv2.imshow("mask", res)
    #cv2.imshow("frame", output)

    #print(frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
