import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("frog.jpg")
img = cv2.resize(img,(500,500))
cv2.line(img,(100,400),(400,100),(0,0,255),7)
cv2.line(img,(100,100),(400,400),(0,0,255),7)
cv2.imshow("image",img)
if cv2.waitKey(0) & 0xFF==27:
    cv2.destroyAllWindows()
"""
img = plt.imread("frog.jpg")
plt.imshow(img)
plt.show()
"""