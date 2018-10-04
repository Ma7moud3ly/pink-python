import cv2
import numpy as np

img=np.zeros((400,400,3),np.uint8)
for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        img[row,col]=[255,0,0]

	      

cv2.imwrite('img.png',img)	     
