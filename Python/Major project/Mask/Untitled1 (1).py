#!/usr/bin/env python
# coding: utf-8

# In[70]:


import tensorflow as tf
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


# In[74]:


img=cv2.imread("D:\EDI_dataset\With_mask\\0_0_0 copy 18.jpg")


# In[75]:


img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)


# In[13]:


img.shape


# In[76]:


Datadirectory='D:/EDI_dataset/'
Classes = ['With_mask','Without_mask']
for category in Classes:
    path=os.path.join(Datadirectory,category)
    for img in os.listdir(path):
        imge=cv2.imread(os.path.join(path,img))
        plt.imshow(cv2.cvtColor(imge, cv2.COLOR_BGR2RGB))
        plt.show()
        break
    break
        


# In[77]:


newsize=224 ##Size required for imagenet
imge=cv2.resize(imge,(newsize,newsize))
plt.imshow(cv2.cvtColor(imge, cv2.COLOR_BGR2RGB))
imge.shape


# # Training data and image Array

# In[78]:


training_Data=[]
def create_training_data():
    for category in Classes:
        path=os.path.join(Datadirectory,category)
        class_num=Classes.index(category)
        for img in os.listdir(path):
            try:
                imge=cv2.imread(os.path.join(path,img))
                imge=cv2.resize(imge,(newsize,newsize))
                training_Data.append([imge,class_num])
            except Exception as e:
                pass
            
        


# In[79]:


create_training_data()


# In[80]:


print(len(training_Data))


# In[81]:


import random
random.shuffle(training_Data)


# In[82]:


X=[] ##data or features
Y=[] ##Classes
for features,label in training_Data:
    X.append(features)
    Y.append(label)
X=np.array(X).reshape(-1,newsize,newsize,3) ##Converting data to numpy array which is required before using it in imagenet


# In[83]:


X.shape


# In[84]:


X=X/255.0 ##Normalization


# In[85]:


Y=np.array(Y) ##Converting data to numpy array which is required before using it in imagenet


# In[86]:


import pickle
pick=open("X.pickle","wb")
pickle.dump(X,pick)
pick.close()

pick=open("Y.pickle","wb")
pickle.dump(Y,pick)
pick.close()


# # Tranfer Learning

# In[87]:


from tensorflow import keras
from tensorflow.keras import layers


# In[88]:


model=tf.keras.applications.mobilenet.MobileNet()


# In[110]:


model.summary()


# In[89]:


base_ip=model.layers[0].input # keeping input layer as it is
base_op=model.layers[-4].output # removing last 3 layers and keeping 4th layer from last as output layer


# In[90]:


flatlayer=layers.Flatten()(base_op)
final_op=layers.Dense(1)(flatlayer)
final_op=layers.Activation('sigmoid')(final_op)


# In[91]:


newmodel=keras.Model(inputs=base_ip, outputs=final_op)


# In[114]:


newmodel.summary()


# In[92]:


newmodel.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])


# In[93]:


newmodel.fit(X,Y, epochs=4, validation_split=0.4)


# In[113]:


newmodel.save('MaskDetector.h5')


# In[114]:


new_model=tf.keras.models.load_model('MaskDetector.h5')


# In[105]:


img=cv2.imread("D:\EDI_dataset\With_mask\\0_0_0 copy 29.jpg")
img=cv2.resize(img, (224,224))
# cv2.imshow('a',img)
plt.imshow(img)
img=np.expand_dims(img,axis=0)
img=img/255.0


# In[106]:


predictionss=new_model.predict(img)


# In[107]:


predictionss


# # Video Capture

# In[ ]:


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
                print('\n')
                if Prediction>0.6:
                    status="No Mask"
                    print('No mask')
                elif Prediction<0.6:
                    status="Mask"
                    print('Mask')
    cv2.imshow("Webcam",frame)

    if cv2.waitKey(1) & 0xFF == ord("w"):
        break
cap.release()
cv2.destroyAllWindows()


# %%
