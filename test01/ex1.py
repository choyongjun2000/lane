import cv2 #library
cap = cv2.VideoCapture(0) #open cam
while(True):
    ret, frame = cap.read() #read frame

    cv2.imshow("Frame",frame) #show frame

    if cv2.waitKey(1) & 0xFF==('q'): # delay window
        break

cap.release()
cv2.destroyAllWindows() #for close window