import cv2
import numpy as np
import math
import tkinter
from tkinter import *
top = tkinter.Tk()
top.geometry('900x600')
top.title("LIFT")
top['background']='#333333'

prevf=0
flag=0

lbl2_0 = Label(top, text="-", bg='#333333', fg="white", font=("Monotype Corsiva",199), anchor=CENTER,height=1, width=4)
lbl2_1 = Label(top, text="1", bg='#333333', fg="white", font=("Monotype Corsiva",199), anchor=CENTER,height=1, width=4)
lbl2_2 = Label(top, text="2", bg='#333333', fg="white", font=("Monotype Corsiva",199), anchor=CENTER,height=1, width=4)
lbl2_3 = Label(top, text="3", bg='#333333', fg="white", font=("Monotype Corsiva",199), anchor=CENTER,height=1, width=4)
lbl2_4 = Label(top, text="4", bg='#333333', fg="white", font=("Monotype Corsiva",199), anchor=CENTER,height=1, width=4)
lbl2_5 = Label(top, text="5", bg='#333333', fg="white", font=("Monotype Corsiva",199), anchor=CENTER,height=1, width=4)

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

def flr(nmbr):
    forget()
    lebelPack()

    lbl1.pack()
    if nmbr==0:
        lbl2_0.pack()
    if nmbr==1:
        lbl2_1.pack()
    if nmbr==2:
        lbl2_2.pack()
    if nmbr==3:
        lbl2_3.pack()
    if nmbr==4:
        lbl2_4.pack()
    if nmbr==5:
        lbl2_5.pack()

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


face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

def my_mainloop():
    # global f,prevf,flag

    ret, frame = cap.read()


    cv2.rectangle(frame, (50, 350), (50, 350), (0, 255, 0), 0)
    crop_image = frame[50:350, 50:350]

    blur = cv2.GaussianBlur(crop_image, (5, 5), 0)

    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    mask2 = cv2.inRange(hsv, np.array([3, 31, 73]), np.array([35, 186, 254]))

    kernel = np.ones((5, 5))

    dilation = cv2.dilate(mask2, kernel, iterations=1)
    erosion = cv2.erode(dilation, kernel, iterations=1)

    filtered = cv2.GaussianBlur(erosion, (3, 3), 0)
    ret, thresh = cv2.threshold(filtered, 127, 255, 0)

    cv2.imshow("Thresholded", thresh)

    contours, hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    num=0
    try:
        contour = max(contours, key=lambda x: cv2.contourArea(x))

        
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)

        
        hull = cv2.convexHull(contour)

        
        drawing = np.zeros(crop_image.shape, np.uint8)
        cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], -1, (0, 0, 255), 0)

        
        hull = cv2.convexHull(contour, returnPoints=False)
        defects = cv2.convexityDefects(contour, hull)


        count_defects = 0
        num=0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])

            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14

            
            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_image, far, 1, [0, 0, 255], -1)

            cv2.line(crop_image, start, end, [0, 255, 0], 2)
        
        
        if count_defects == 0:
            cv2.putText(frame, "ONE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
            num=1
        elif count_defects == 1:
            cv2.putText(frame, "TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            num=2
        elif count_defects == 2:
            cv2.putText(frame, "THREE", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            num=3
        elif count_defects == 3:
            cv2.putText(frame, "FOUR", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            num=4
        elif count_defects == 4:
            cv2.putText(frame, "FIVE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            num=5
        elif count_defects == 5:
            cv2.putText(frame, "SEVEN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            num=6
        elif count_defects == 6:
            cv2.putText(frame, "EIGHT", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            num=7
        elif count_defects == 7:
            cv2.putText(frame, "NINE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            num=8
        elif count_defects == 8:
            cv2.putText(frame, "TEN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            num=9
        else:
            pass
    except:
        pass

    # Show required images
    # frame = cv2.flip(frame, 1)
    cv2.imshow("Gesture", frame)
    # frame = cv2.flip(frame, 1)
    
    # all_image = np.hstack((drawing, crop_image))
    # cv2.imshow('Contours', all_image)

    flr(num)    

    top.after(10, my_mainloop)    

top.after(1, my_mainloop)


top.mainloop()