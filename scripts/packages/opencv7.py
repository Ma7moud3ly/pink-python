import numpy as np
import cv2

face_cascade   = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade  = cv2.CascadeClassifier('haarcascade_smile.xml')
cap = cv2.VideoCapture(0)

def detect_persons(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    s=0
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
        face_gray  = gray[y:y+h, x:x+w]
        face_color = img[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(face_gray)
        
        for (ex,ey,ew,eh) in smiles:
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
            s=s+1
            break
            
    cv2.putText(img,'%s Persons'%len(faces),(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
    cv2.putText(img,'%s Smile'%s,(20,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
    return img

while(True):
    ret,img = cap.read()
    img=detect_persons(img)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
