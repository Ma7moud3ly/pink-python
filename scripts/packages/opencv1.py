import cv2
import numpy as np
def show(img):
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()     
 
img=np.zeros((400,400,3),np.uint8)
for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        img[row,col]=[0,255,0]		      
show(img)
