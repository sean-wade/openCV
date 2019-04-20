# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:18:53 2019

@author: Sean
"""

import cv2
import random  # snow 雪花效果
import numpy as np

img=cv2.imread("cp.bmp")  #("",0)
#for i in range(200,img.shape[0]):
#    for j in range(200,img.shape[1]):
#        if i>j:
#            img[i,j]=[100,155,255]

#for i in range(100,img.shape[0]):
#    for j in range(100,img.shape[1]):
#        img[i,j]=[0,0,255]
#img[100:,100:]=[0,0,255]    # Much more efficient than for(for)

#img[100]=[0,255,0]
#img[:,200]=[255,0,0]


# This is snow effect:
for num in range(500):
    i=random.randint(0,img.shape[0]-1)
    j=random.randint(0,img.shape[1]-1)
    img[i:i+random.randint(1,1),j:j+random.randint(1,3)]=[255,255,255]
#    cv2.circle(img,(j,i),random.randint(0,2),(0,255,255),-1)

#  This is Color Reduce图像减色
#colorNum=128    #减色系数，0-63——32,64-127——96……
#for i in range(0,img.shape[0]):
#    for j in range(0,img.shape[1]):
##        img[i,j,0]=int(img[i,j,0]/colorNum)*colorNum+colorNum/2
##        img[i,j,1]=int(img[i,j,1]/colorNum)*colorNum+colorNum/2
##        img[i,j,2]=int(img[i,j,2]/colorNum)*colorNum+colorNum/2
#        img[i,j]=int(img[i,j]/colorNum)*colorNum+colorNum/2    #128相当于二值化
        
#print(img)


cv2.imshow('',img)
cv2.imwrite('C:/Users/Sean/Desktop/cp3.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()







