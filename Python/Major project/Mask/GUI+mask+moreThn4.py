import cv2
import tensorflow as tf
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
top = tkinter.Tk()
top.geometry('900x600')
top.title("LIFT")
top['background']='#333333'

new_model=tf.keras.models.load_model('MaskDetector.h5')

prevf=0
flag=0

lbl2 = Label(top, text="5", bg='#333333', fg="white", font=("Monotype Corsiva",199), anchor=CENTER,height=1, width=4)

lbl1 = Label(top, text = " You have selected Floor No. ",font =("Monotype Corsiva", 59),height=2,background='#333333',foreground='#AAAAAA') 

lbl3 = Label(top, text = " Please \nWear \na mask ..!!  \U0001F637",font =("Monotype Corsiva", 109),background='#333333',foreground='#AAAAAA') 

lbl4 = Label(top, text = " Please \nStep Out \nof Lift ..!!",font =("Monotype Corsiva", 109),background='#333333',foreground='#AAAAAA') 

lbl5 = Label(top, text = " Not more than 2 people \n allowed..!! \n Please Step Out \nof Lift ..!!",font =("Monotype Corsiva", 79),background='#333333',foreground='#AAAAAA') 

l = Label(top, text = " Welcome \nto \nLift ",font =("Monotype Corsiva", 109),background='#333333',foreground='#AAAAAA') 

def lebelPack():
    global lbl1,lbl2,lbl3,lbl4,l

def all_children (top) :
    _list = top.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def forget():
    widget_list = all_children(top)
    for item in widget_list:
        item.pack_forget()

def flr():
    forget()
    lebelPack()

    lbl1.pack()
    lbl2.pack()

def maskWarning():
    forget()
    lebelPack()

    lbl3.pack()

def tempWarning():
    forget()
    lebelPack()

    lbl4.pack()

def morePeopleWarning():
    forget()
    lebelPack()

    lbl5.pack()

def messege():
    forget()
    lebelPack()

    l.pack()


# top.after(2000, flr)
# top.after(4000, maskWarning)
# top.after(6000, morePeopleWarning)

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

mflag=0

def my_mainloop():
    global f,prevf,flag,mflag
    # print ("Hello World!")

    # face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

    ret, img = cap.read()
    frame=img
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    f=0

    for[x,y,w,h] in faces:
        f=f+1
        img= cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)


    # ret,frame=cap.read()
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
                print('\n')
                if Prediction>0.6:
                    status="No Mask"
                    mflag=2
                    print('No mask')
                elif Prediction<0.6:
                    status="Mask"
                    mflag=0
                    print('Mask')
    cv2.imshow("Webcam",frame)



    if f!=prevf:
        if f>2:
            flag=1
            morePeopleWarning()
        else:
            flag=0
            if mflag==0:
                messege()
            elif mflag==2:
                maskWarning()
        prevf=f
    
    print(flag)
    # cv2.imshow('Video',img)

    

    # if flag==0:
    #     messege()
    # if flag==1:
    #     morePeopleWarning()
    # k = cv2.waitKey(1)

    # if(k==27):
    #     cv2.destroyAllWindows()
    #     cap.release()

    top.after(10, my_mainloop)    

top.after(1, my_mainloop)


top.mainloop()