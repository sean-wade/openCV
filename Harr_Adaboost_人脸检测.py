# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:02:02 2019

@author: Sean
"""

import cv2
import numpy as np


# step 1：load XML
face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier('haarcascade_eye.xml')

# step 2: load image
img = cv2.imread('hz.jpg')
cv2.imshow('face', img)

# step 3: haar gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# step 4: detect faces   
faces = face_xml.detectMultiScale(gray, 1.3, 5)    #img, scale, ?
print('face Num = ', len(faces))

#draw
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    eyes = eye_xml.detectMultiScale(roi_gray,1.3,2,cv2.CASCADE_SCALE_IMAGE,(10,10),(100,100))
    print('eye Num = ', len(eyes))
    
    for (e_x,e_y,e_w,e_h) in eyes:
        cv2.rectangle(img, (e_x+x, e_y+y), (e_x+e_w+x, e_y+e_h+y), (0,255,0), 2)

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


    
    