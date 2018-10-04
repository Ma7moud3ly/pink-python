import cv2
import numpy as np

def show(img):
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   

img=np.ones((500,500,3),np.uint8)*255 

red   = (0,0,255)
green = (0,255,0)
blue  = (255,0,0)

cv2.line(img,(10,10),(10,490),green,4)
cv2.putText(img,'Line',(15,50),cv2.FONT_HERSHEY_SIMPLEX,1,green,2)

cv2.rectangle(img,(100,100),(200,200),red,4)
cv2.putText(img,'Rectangle',(110,120),cv2.FONT_HERSHEY_SIMPLEX,0.5,red,2)

cv2.circle(img,(300,300),100,blue,4)
cv2.putText(img,'Circle',(275,300),cv2.FONT_HERSHEY_SIMPLEX,0.5,blue,2)

show(img)
