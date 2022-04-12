import cv2
import numpy as np
import math

def nothing(x):
	pass

shorten = 0.4

cap = cv2.VideoCapture(0)

# a = cv2.imread("grn.jpg",-1)
# a = cv2.imread("eight.jpg",-1)
# a = cv2.imread("two.jpg",-1)

ret, a = cap.read()
z=a
a=cv2.resize(a,(int(a.shape[1]*shorten),int(a.shape[0]*shorten)))
z=cv2.resize(z,(int(z.shape[1]*shorten),int(z.shape[0]*shorten)))

horiz=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)
verti=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)
final=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)
final2=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)
final3=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)


# x=a.shape[0]
# y=a.shape[1]

deff = 20
lim = 1

while cap.isOpened():
    ret, a = cap.read()
    z=a
    a=cv2.resize(a,(int(a.shape[1]*shorten),int(a.shape[0]*shorten)))
    z=cv2.resize(z,(int(z.shape[1]*shorten)+1,int(z.shape[0]*shorten)+1))
    
    cv2.imshow('A', a)

    # for x in range (lim,a.shape[0]):
    #     for y in range (lim,a.shape[1]):
    #         if (abs(int(a[x,y,0])-int(a[x-lim,y,0])) > deff) and (abs(int(a[x,y,1])-int(a[x-lim,y,1])) > deff) and (abs(int(a[x,y,2])-int(a[x-lim,y,2])) > deff):
    #             horiz[x,y] = [255,255,255]
    #         if (abs(int(a[x,y,0])-int(a[x,y-lim,0])) > deff) and (abs(int(a[x,y,1])-int(a[x,y-lim,1])) > deff) and (abs(int(a[x,y,2])-int(a[x,y-lim,2])) > deff):
    #             verti[x,y] = [255,255,255]

    for x in range (lim,a.shape[0]):
        for y in range (lim,a.shape[1]):
            qwerty = (abs(int(a[x,y,0])-int(a[x-lim,y,0])) > deff) and (abs(int(a[x,y,1])-int(a[x-lim,y,1])) > deff) and (abs(int(a[x,y,2])-int(a[x-lim,y,2])) > deff)
            qwertu = (abs(int(a[x,y,0])-int(a[x,y-lim,0])) > deff) and (abs(int(a[x,y,1])-int(a[x,y-lim,1])) > deff) and (abs(int(a[x,y,2])-int(a[x,y-lim,2])) > deff)
            final2[x,y]= [255*qwerty + 255*qwertu,255*qwerty + 255*qwertu,255*qwerty + 255*qwertu]

    int(a[x,y,0])
    
    # final = horiz + verti

    cv2.imshow('final2' , final2)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()