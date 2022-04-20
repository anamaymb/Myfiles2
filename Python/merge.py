import cv2
import numpy as np
import math

def function(event, x, y, flags, params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Original')
        print(a[y,x,0],a[y,x,1],a[y,x,2])
        print('Final')
        print(final[y,x,0],final[y,x,1],final[y,x,2])
        print('avg')
        print(avg[y,x])
        print('comp')
        print((a[y,x,0]/2+con*avg[y,x]/2),(a[y,x,1]/2+con*avg[y,x]/2),(a[y,x,2]/2+con*avg[y,x]/2))
        print('logic')
        print(((a[y,x,0]/2+con*avg[y,x]/2)<=127)*(con>=0)*(a[y,x,z]+con*avg[y,x]),((a[y,x,1]/2+con*avg[y,x]/2)<=127),((a[y,x,2]/2+con*avg[y,x]/2)<=127))
        print('a[]')
        print(((a[y,x,0]/2+con*avg[y,x]/2)>127)*(255) + ((a[y,x,0]/2+con*avg[y,x]/2)<=127)* \
                        ( (con>=0)*(a[y,x,0]+con*avg[y,x]) + (con<0)* ((a[y,x,0]>abs(con*avg[y,x]))*(a[y,x,0]+con*avg[y,x]) + (a[y,x,0]<abs(con*avg[y,x])) * 0 ) ))
        print(((a[y,x,1]/2+con*avg[y,x]/2)>127)*(255) + ((a[y,x,1]/2+con*avg[y,x]/2)<=127)* \
                        ( (con>=0)*(a[y,x,1]+con*avg[y,x]) + (con<0)* ((a[y,x,1]>abs(con*avg[y,x]))*(a[y,x,1]+con*avg[y,x]) + (a[y,x,1]<abs(con*avg[y,x])) * 0 ) ))
        print(((a[y,x,2]/2+con*avg[y,x]/2)>127)*(255) + ((a[y,x,2]/2+con*avg[y,x]/2)<=127)* \
                        ( (con>=0)*(a[y,x,2]+con*avg[y,x]) + (con<0)* ((a[y,x,2]>abs(con*avg[y,x]))*(a[y,x,2]+con*avg[y,x]) + (a[y,x,2]<abs(con*avg[y,x])) * 0 ) ))
        cv2.circle(final,(x,y),5,(0,0,255),5)

cv2.namedWindow('A')
cv2.setMouseCallback('A', function)
cv2.namedWindow('final2')
cv2.setMouseCallback('final2', function)

def nothing(x):
	pass

shorten = 0.7

cap = cv2.VideoCapture(0)
ret, a = cap.read()

deepness = 8

a=cv2.resize(a,(int(a.shape[1]*shorten),int(a.shape[0]*shorten)))
arr=np.zeros((deepness,a.shape[0],a.shape[1],3),dtype=np.uint8)
arr[0] = a

final=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)
w=np.zeros(10,dtype=np.float)

w[:] = [377,233,144,89,55,34,21,13,8,5]
w[:] = w[:] / sum(w)

while cap.isOpened():
    ret, a = cap.read()
    a=cv2.resize(a,(int(a.shape[1]*shorten),int(a.shape[0]*shorten)))
    arr[0] = a

    cv2.imshow('A', a)
    
    # final [:,:,:] = w[0] * arr[0,:,:,:] + w[1] * arr[1,:,:,:] + w[2]*arr[2,:,:,:] + w[3] * arr[3,:,:,:] + w[4]*arr[4,:,:,:] 
    
    for i in range (0,deepness):
        final [:,:,:] = final [:,:,:] + ( w[i] * arr[i,:,:,:] )

    cv2.imshow('final2' , final)

    final=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)

    for j in range (deepness-1, 0,-1):
        arr[j,:,:,:] = arr[j-1,:,:,:]

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

cv2.waitKey(0)