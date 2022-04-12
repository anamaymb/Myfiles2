import cv2
import tensorflow as tf
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
top = tkinter.Tk()
top.geometry('1000x700')
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
prevmflag=1


def my_mainloop():
    global f,prevf,flag,mflag,prevmflag
    # print ("Hello World!")


    ret,frame=cap.read()
    faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,1.03,6)
    for x,y,w,h in faces:
        roi_color=frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        final_img=cv2.resize(roi_color, (224,224))
        final_img=np.expand_dims(final_img,axis=0)
        final_img=final_img/255.0
        Prediction=new_model.predict(final_img)
        print(Prediction)
        if Prediction>0.6:
            status="No Mask"
            print('No mask')
            mflag=2
        elif Prediction<0.6:
            status="Mask"
            print('Mask')
            mflag=0
        cv2.imshow("Webcam",frame)
    
     
    # frame = cv2.putText(frame, status, org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Webcam",frame)
    



    # if f!=prevf:
    #     if f>2:
    #         flag=1
    #         morePeopleWarning()
    #     else:
    #         flag=0
    #         if mflag==0:
    #             messege()
    #         elif mflag==2:
    #             maskWarning()
    #     prevf=f
    
    if mflag!=prevmflag:
        if mflag==0:
            messege()
        elif mflag==2:
            maskWarning()
        prevmflag=mflag

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