import numpy as np
import cv2
import os
path=os.path.dirname(__file__)
face_cascade   = cv2.CascadeClassifier(path+'/haarcascade_frontalface_default.xml')
def detect(inp,out):
    img=cv2.imread(inp)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        face_gray  = gray[y:y+h, x:x+w]
        face_color = img[y:y+h, x:x+w]
    cv2.imwrite(out,img)
    return len(faces)
