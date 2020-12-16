import cv2
import numpy as np


img = cv2.imread("eight.jpg",-1)
# img = cv2.imread("solar.jpg",-1)
# 
img = cv2.resize(img, (100, 100))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray=255-gray

for i in range (0,100):
    for j in range (0,100):
        if gray[i,j]>100:
            gray[i,j]=1
        else:
            gray[i,j]=0

# gray=gray*255
# cv2.imshow('samp',gray)
gray = cv2.resize(gray, (10, 10))

weights = np.zeros((10,100),np.float)
weights_prev = np.zeros((10,100),np.float)

output = np.empty(10)
expectedOp = np.empty((10),np.float)
ExNum=np.array([20,16,31,22,21,23,15,24,23,20],np.float)
Input=np.array([[0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #1                                     1
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #2
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #3
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #4
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #5
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #6
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #7
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #8
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #9
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ],      #10
             
                [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #1                                     2
                 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ,       #2
                 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 ,       #3
                 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,       #4
                 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,       #5
                 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 ,       #6
                 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ,       #7
                 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ,       #8
                 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 ,       #9
                 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],      #10
             
                 [0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ,       #1                                      3
                  0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 ,       #2
                  0 , 0 , 1 , 0 , 0 , 0 , 1 , 1 , 0 , 0 ,       #3
                  0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 ,       #4
                  0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ,       #5
                  0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 ,       #6
                  0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 ,       #7
                  0 , 0 , 1 , 0 , 0 , 0 , 1 , 1 , 0 , 0 ,       #8
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #9
                  0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0 ],
             
                 [0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,       #1                                      4
                  0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 ,       #2
                  0 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 ,       #3
                  0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 ,       #4
                  0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,       #5
                  0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,       #6
                  0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 ,       #7
                  0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,       #8
                  0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,       #9
                  0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ],      #10
             
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #1                                      5
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 ,       #2
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #3
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #4
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #5
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #6
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #7
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #8
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #9
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],      #10
             
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #1                                      6
                  0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #2
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #3
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #4
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #5
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #6
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #7
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #8
                  0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #9
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],      #10
             
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #1                                     7
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 ,       #2
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 ,       #3
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #4
                  0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,       #5
                  0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 ,       #6
                  0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ,       #7
                  0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ,       #8
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #9
                  0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],      #10
             
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #1                                     8
                  0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #2
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #3
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #4
                  0 , 0 , 1 , 1 , 0 , 0 , 1 , 1 , 0 , 0 ,       #5
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 ,       #6
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #7
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #8
                  0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #9
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],      #10
             
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #1                                     9
                  0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #2
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #3
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #4
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #5
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 ,       #6
                  0 , 0 ,-2 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #7
                  0 , 0 ,-2 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #8
                  0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #9
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],      #10
             
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,       #1                                     0
                  0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #2
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #3
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #4
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #5
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #6
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #7
                  0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ,       #8
                  0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 ,       #9
                  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]],dtype=np.float)


def squares(x,str):
    if str == 'prev':
        res = np.dot(weights_prev[x],Input[x])
    elif str == 'normal':
        res = np.dot(weights[x],Input[x])
    
    return (expectedOp[x]-res)*(expectedOp[x]-res)


for number in range (0,10):
    
    for i in range (0,10):
        expectedOp[i]=0
        if i==number:
            expectedOp[i]=ExNum[i]
    
    kp=np.array([0.004 , 0.005 , 0.002 , 0.0035 , 0.003 , 0.0022 ,0.0052 ,0.002 ,0.002 ,0.004],np.float)
    h=0.01
    #         1       2       3       4       5       6       7       8       9       0
    #         20,     16,     31,     22,     21,     23,     15,     24,     23,     20

    for count in range (0,100):
        for i in range (0,100):

            SOPS0=squares(number,'prev')
            weights_prev[number][i]=weights_prev[number][i]+h
            SOPSh=squares(number,'prev')
            weights_prev[number][i]=weights_prev[number][i]-h

            if SOPS0>SOPSh:
                weights[number][i]=(weights[number][i])+kp[number]*abs(squares(number,'prev'))

            elif SOPS0<SOPSh:
                weights[number][i]=(weights[number][i])-kp[number]*abs(squares(number,'prev'))

        weights_prev[number]=weights[number]


    # for i in range (0,100):
    #     if i%10==0:
    #         print(' ')
    #     if weights[number][i] != 0.00000 :
    #         print('%.5f'%weights[number][i],end=" ")
    #     else:
    #         print('       ',end=" ")
    

    # print('\n')



TestIp=np.array( [0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,      #1                                    4
                  0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 ,      #2
                  0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ,      #3
                  0 , 0 , 0 , 1 , 1 , 0 , 1 , 0 , 0 , 0 ,      #4
                  0 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 0 , 0 ,      #5
                  0 , 1 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,      #6
                  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 ,      #7
                  0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,      #8
                  0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,      #9
                  0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ],np.int32)      #10

TestIp=gray.ravel()

highest=0
for j in range (0,10):
    output[j]=0
    for i in range (0,100):
        output[j]=output[j] + weights[j][i]*TestIp[i]
    if highest<output[j]:
        highest=output[j]

for j in range (0,10):
    print('%.5f'%(output[j]/highest))

for i in range (0,100):
    print(TestIp[i],end=" ")
    if i%10==9:
        print('')

gray=gray*255
gray = cv2.resize(gray, (100, 100))
cv2.imshow('sample',gray)
cv2.waitKey(0)
