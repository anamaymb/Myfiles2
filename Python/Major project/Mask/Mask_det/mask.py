import tensorflow as tf
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

new_model=tf.keras.models.load_model('MaskDetector.h5')


cap=cv2.VideoCapture(0)
if not cap.isOpened():
    cap=cv2.VideoCapture(1)
if not cap.isOpened():
    raise IOError("Can't open webcam")

while True:
    ret,frame=cap.read()
    # frame=cv2.imread("D:\EDI_dataset\Without_mask\\00010.png")
    faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,1.03,6)
    for x,y,w,h in faces:
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        faces1=faceCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in faces1:
                face_roi=roi_color[ey:ey+eh, ex:ex+ew]
            
                final_img=cv2.resize(face_roi, (224,224))
                final_img=np.expand_dims(final_img,axis=0)
                final_img=final_img/255.0
                font=cv2.FONT_HERSHEY_PLAIN
                Prediction=new_model.predict(final_img)
                print(Prediction)
                if Prediction>0.6:
                    status="No Mask Detected"
                    print('No mask')
                elif Prediction<0.6:
                    status="Mask Detected"
                    print('Mask')
    


    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # org 
    org = (50, 50) 
    
    # fontScale 
    fontScale = 2
    
    # Blue color in BGR 
    color = (255, 0, 0) 
    
    # Line thickness of 2 px 
    thickness = 3
    
    # Using cv2.putText() method 
    frame = cv2.putText(frame, status, org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Webcam",frame)

    

    if cv2.waitKey(1) & 0xFF == ord("w"):
        break
cap.release()
cv2.destroyAllWindows()

