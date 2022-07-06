import cv2

img = cv2.imread("noisy.jpg")
img = cv2.resize(img,(400,400))

blur = cv2.blur(img,(9,9)) #average blur
Mblur = cv2.medianBlur(img,9) #median blur
Gblur = cv2.GaussianBlur(img,(9,9),0) #gaussian blur

G1blur = cv2.GaussianBlur(img,(9,9),1) #gaussian blur
G2blur = cv2.GaussianBlur(img,(9,9),2) #gaussian blur
G5blur = cv2.GaussianBlur(img,(9,9),5) #gaussian blur

#cv2.imshow("Original",img)
#cv2.imshow("blur",blur)
#cv2.imshow("MBlur",Mblur)
cv2.imshow("GBlur",Gblur)

#sigma gaussian blur
cv2.imshow("G1Blur",G1blur)
cv2.imshow("G2Blur",G2blur)
cv2.imshow("G5Blur",G5blur)

if cv2.waitKey(0) & 0xFF==27:
    cv2.destroyAllWindows()
