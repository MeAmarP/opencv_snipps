

#For Image Processing
import cv2
import matplotlib.pyplot as plt
import os

#Conver Img to Biary format
img = cv2.imread('/home/amarp/Documents/pyproj/CV/forFoilio/cv_guide/imgs/cell_bin.png')
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
temp = thresh[:,:,0]
temp[temp == 255] = 1
# cv2.imwrite('cellsnew_bin.jpg',temp)
# plt.imshow(temp)

cv2.imshow('Img',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()







