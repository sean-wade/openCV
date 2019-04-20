# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:15:21 2019

@author: Sean
"""

#图像形态学，膨胀腐蚀，开闭运算 
#可以通过角点检测


import cv2
import numpy as np

img=cv2.imread("cp3.png")
k=np.ones((2,2),np.uint8)
erosion=cv2.erode(img,k)
#gradient=cv2.morphologyEx(erosion,cv2.MORPH_GRADIENT,k)
#dilation=cv2.dilate(erosion,k)
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,k)

cv2.imshow('src',img)
cv2.imshow('t',tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()