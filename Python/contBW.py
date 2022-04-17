import cv2
import numpy as np
import math

def function(event, x, y, flags, params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Original')
        print(a[y,x,0],a[y,x,1],a[y,x,2])
        print('Final')
        print(final[y,x,0],final[y,x,1],final[y,x,2])
        print('Var')
        print(var[y,x,0],var[y,x,1],var[y,x,2])
        cv2.circle(final,(x,y),5,(0,0,255),5)

cv2.namedWindow('A')
cv2.setMouseCallback('A', function)
cv2.namedWindow('final2')
cv2.setMouseCallback('final2', function)

def nothing(x):
	pass

shorten = 0.8

cv2.namedWindow("Trackbars")
cv2.createTrackbar("X","Trackbars",-150,150,nothing)


cap = cv2.VideoCapture(0)
ret, a = cap.read()

# a = cv2.imread("grn.jpg",-1)
# a = cv2.imread("eight.jpg",-1)
# a = cv2.imread("two.jpg",-1)


z=a
a=cv2.resize(a,(int(a.shape[1]*shorten),int(a.shape[0]*shorten)))
z=cv2.resize(z,(int(z.shape[1]*shorten),int(z.shape[0]*shorten)))


final=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)
var=np.zeros((a.shape[0],a.shape[1],3),dtype=np.int8)
avg=np.zeros((a.shape[0],a.shape[1]),dtype=np.int8)

# x=a.shape[0]
# y=a.shape[1]

con = -0.5

while cap.isOpened():
    ret, a = cap.read()
    z=a
    a=cv2.resize(a,(int(a.shape[1]*shorten),int(a.shape[0]*shorten)))
    z=cv2.resize(z,(int(z.shape[1]*shorten),int(z.shape[0]*shorten)))
    
    cons = cv2.getTrackbarPos("X","Trackbars")
    con = cons/100
    
    cv2.imshow('A', a)

    avg[:,:] = a[:,:,0]/3 + a[:,:,1]/3 + a[:,:,2]/3 
    var[:,:,0] = abs(a[:,:,0]-avg[:,:])
    var[:,:,1] = abs(a[:,:,1]-avg[:,:])
    var[:,:,2] = abs(a[:,:,2]-avg[:,:])
    for z in range (0,3):
        # final[:,:,z] =  (a[:,:,z]>avg)*(((a[:,:,z]/2+con*avg/2)>127)*(255) + (((a[:,:,z]/2 + con*avg/2)<127)*(a[:,:,z]+con*avg))) + \
        # (a[:,:,z]<avg)* (  (a[:,:,z]<=con*avg)*(0) + (a[:,:,z]>con*avg)*(a[:,:,z]-con*avg)  ) + \
        # (a[:,:,z]==avg) * (a[:,:,z])

        final[:,:,z] =  (a[:,:,z] > avg)*(((a[:,:,z]/2 + con*var[:,:,z]/2)>127)*(255) + (((a[:,:,z]/2 + con*var[:,:,z]/2)<=127)*(a[:,:,z]+con*var[:,:,z]))) + \
        (a[:,:,z]<avg)* (  (a[:,:,z]<=con*var[:,:,z])*(0) + (a[:,:,z]>con*var[:,:,z])*(a[:,:,z]-con*var[:,:,z])  ) + \
        (a[:,:,z]==avg) * (a[:,:,z])


    cv2.imshow('final2' , final)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





# cv2.imshow('A', a)

# avg[:,:] = a[:,:,0]/3 + a[:,:,1]/3 + a[:,:,2]/3 
# var[:,:,0] = abs(a[:,:,0]-avg[:,:])
# var[:,:,1] = abs(a[:,:,1]-avg[:,:])
# var[:,:,2] = abs(a[:,:,2]-avg[:,:])

# # for z in range (0,3):
# #     final[:,:,z] =  (a[:,:,z]>avg)*(a[:,:,z]+(255-a[:,:,z])*con) + (a[:,:,z]<=avg)*(a[:,:,z]-con*a[:,:,z])

# for z in range (3):
#     final[:,:,z] =  (a[:,:,z] > avg)*(((a[:,:,z]/2 + con*var[:,:,z]/2)>127)*(255) + (((a[:,:,z]/2 + con*var[:,:,z]/2)<=127)*(a[:,:,z]+con*var[:,:,z]))) + \
#     (a[:,:,z]<avg)* (  (a[:,:,z]<=con*var[:,:,z])*(0) + (a[:,:,z]>con*var[:,:,z])*(a[:,:,z]-con*var[:,:,z])  ) + \
#     (a[:,:,z]==avg) * (a[:,:,z])

# # for x in range (0,a.shape[0]):
# #     for y in range (0,a.shape[1]):
# #         avg = a[x,y,0]/3 + a[x,y,1]/3 + a[x,y,2]/3 
# #         for z in range (3):
# #             final[x,y,z] =  (a[x,y,z]>avg)*(a[x,y,z]+con*avg) + (a[x,y,z]<=avg)*(a[x,y,z]-con*avg)

# cv2.imshow('final2' , final)


# cv2.waitKey(0)