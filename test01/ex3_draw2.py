import cv2
import numpy as np

img = np.zeros((500,500,3),dtype='uint8')
pts = np.array([[100,25],[200,25],[275,100],[275,200],[200,275],[100,275],[25,200],[25,100]],np.int32)
cv2.polylines(img,[pts],True,(255,0,0),5)
cv2.putText(img,'STOP',(75,165),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5,cv2.LINE_AA)
cv2.imshow("image",img)
if cv2.waitKey(0) & 0xFF==27:
    cv2.destroyAllWindows()