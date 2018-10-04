import cv2
import numpy as np
def show(img):
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()     

img=np.zeros((400,400,3),np.uint8)
show(img)
