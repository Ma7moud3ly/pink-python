import cv2
import numpy as np

def show(img):
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()     

main = cv2.imread('logo.png')
scaled = cv2.resize(main, (0,0), fx=4, fy=4) 
gray = cv2.cvtColor(scaled,cv2.COLOR_BGR2GRAY)

show(scaled)
show(gray)
