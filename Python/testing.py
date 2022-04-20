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
        print(colContrast[y,x])

cv2.namedWindow('A')
cv2.setMouseCallback('A', function)
cv2.namedWindow('final2')
cv2.setMouseCallback('final2', function)

def nothing(x):
	pass

shorten = 0.9

cv2.namedWindow("Trackbars")
cv2.createTrackbar("X","Trackbars",0,400,nothing)


cap = cv2.VideoCapture(0)
ret, a = cap.read()

# a = cv2.imread("two.jpg",-1)
# a = cv2.imread("solar.jpg",-1)
# a = cv2.imread("grn.jpg",-1)
# a = cv2.imread("eight.jpg",-1)
# a = cv2.imread("two.jpg",-1)

a=cv2.resize(a,(int(a.shape[1]*shorten),int(a.shape[0]*shorten)))

final=np.zeros((a.shape[0],a.shape[1],3),dtype=np.uint8)
var=np.zeros((a.shape[0],a.shape[1],3),dtype=np.int)
avg=np.zeros((a.shape[0],a.shape[1]),dtype=np.int)
row=np.zeros((a.shape[0]),dtype=np.float)
col=np.zeros((a.shape[1]),dtype=np.float)
rows=np.zeros((a.shape[0]),dtype=np.float)
cols=np.zeros((a.shape[1]),dtype=np.float)
rowContrast = np.zeros((a.shape[1],a.shape[0]),dtype=np.float)
colContrast = np.zeros((a.shape[0],a.shape[1]),dtype=np.float)

cont=np.zeros((a.shape[0],a.shape[1]),dtype=np.int)


fact = -0.1

for x in range (0, a.shape[0]):    
    row[x] = x
for y in range (0, a.shape[1]):
    col[y] = y


while cap.isOpened():
    ret, a = cap.read()
    
    a=cv2.resize(a,(int(a.shape[1]*shorten),int(a.shape[0]*shorten)))
    
    facts = cv2.getTrackbarPos("X","Trackbars")
    fact = -(facts+100)/1000
    
    cv2.imshow('A', a)

    rows[:] = ((row[:]-a.shape[0]/2)/(a.shape[0]*0.01))**2/(10000*fact)
    rowContrast[:,:] = np.repeat([rows],a.shape[1],0)

    cols[:] = ((col[:]-a.shape[1]/2)/(a.shape[1]*0.01))**2/(10000*(a.shape[1]/a.shape[0])*fact)
    colContrast[:,:] = np.repeat([cols],a.shape[0],0)

    avg[:,:] = a[:,:,0]/3 + a[:,:,1]/3 + a[:,:,2]/3 

    colContrast = colContrast + rowContrast.transpose()
    var[:,:,0] = abs(a[:,:,0]-avg[:,:])
    var[:,:,1] = abs(a[:,:,1]-avg[:,:])
    var[:,:,2] = abs(a[:,:,2]-avg[:,:])
    for z in range (3):
        final[:,:,z] =  ( (a[:,:,z]/2 + (colContrast[:,:] * avg[:,:])/2) > 127 ) * (255) + \
                        ( (a[:,:,z]/2 + (colContrast * avg[:,:])/2) <=127 ) * \
                        ( (colContrast[:,:]>=0) * (a[:,:,z] + colContrast*avg[:,:]) + \
                        (colContrast[:,:]< 0) * ((a[:,:,z] > abs(colContrast*avg[:,:]))*(a[:,:,z]+colContrast*avg[:,:]) + (a[:,:,z]<abs(colContrast*avg[:,:])) * 0 ) ) 
        # final[:,:,z] =  ( (a[:,:,z]/2 + (colContrast[:,:] * var[:,:,z])/2) > 127 ) * (255) + \
        #                 ( (a[:,:,z]/2 + (colContrast * var[:,:,z])/2) <=127 ) * \
        #                 ( (colContrast[:,:]>=0) * (a[:,:,z] + colContrast*var[:,:,z]) + \
        #                 (colContrast[:,:]< 0) * ((a[:,:,z] > abs(colContrast*var[:,:,z]))*(a[:,:,z]+colContrast*var[:,:,z]) + (a[:,:,z]<abs(colContrast*var[:,:,z])) * 0 ) ) 
    
    cv2.imshow('final2' , final)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


	