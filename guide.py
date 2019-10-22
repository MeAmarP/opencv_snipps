

#For Image Processing
import cv2
import matplotlib.pyplot as plt
import os

#Conver Img to Biary format
img = cv2.imread('imgs\Baraja_de_UNO.jpg')
# ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# temp = thresh[:,:,0]
# cv2.imwrite('cell_bin.png',temp)
cv2.imshow('img',img)
cv2.waitKey(0)








