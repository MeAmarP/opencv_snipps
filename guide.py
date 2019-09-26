

#For Image Processing
import cv2
import matplotlib.pyplot as plt
import os

#Conver Img to Biary format
img = cv2.imread('/home/amarp/Documents/pyproj/CV/forFoilio/cv_guide/imgs/cell_bin.png')
# ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
temp = thresh[:,:,0]
cv2.imwrite('cell_bin.png',temp)
plt.imshow(temp)








