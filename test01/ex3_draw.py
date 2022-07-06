import cv2
import numpy as np

img = np.zeros((400,400,3),dtype="uint8")
cv2.line(img,(50,300),(300,50),(0,0,255),7)
cv2.line(img,(50,50),(300,300),(0,100,255),7)
cv2.rectangle(img,(100,100),(350,350),(255,0,0),5)
cv2.circle(img,(200,200),80,(100,100,100),-1)
cv2.imshow("image",img)
if cv2.waitKey(0) & 0xFF==27:
    cv2.destroyAllWindows()