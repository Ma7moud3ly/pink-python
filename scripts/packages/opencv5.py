import numpy as np
import cv2

def show(img):
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

img  = cv2.imread('img1.jpg')
small=cv2.resize(img.copy(),(0,0),fx=0.4,fy=0.4)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade   = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade  = cv2.CascadeClassifier('haarcascade_smile.xml')
faces = face_cascade.detectMultiScale(gray)
s=0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    face_gray  = gray[y:y+h, x:x+w]
    face_color = img[y:y+h, x:x+w]
    smiles = smile_cascade.detectMultiScale(face_gray)
    for (ex,ey,ew,eh) in smiles:
        cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)
        s=s+1
        break
height=img.shape[0]
width=img.shape[1]
x_offset=0
y_offset=gray.shape[0]-small.shape[0]
img[y_offset:y_offset+small.shape[0], x_offset:x_offset+small.shape[1]] = small
cv2.putText(img,'%s Persons'%len(faces),( width-150,height-50),
cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
cv2.putText(img,'%s Smile'%s,(width-150,height-10),cv2.FONT_HERSHEY_SIMPLEX,
0.8,(255,255,255),2)
show(img)
