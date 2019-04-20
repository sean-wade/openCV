# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:45:56 2019

@author: Sean
"""
import cv2
import numpy as np
# 图像形态学，膨胀腐蚀

img=cv2.imread("cp3.png",0)  #常用灰度读取
k=np.ones((2,2),np.uint8)  #指定核大小
#dilation=cv2.dilate(img,k,iterations=1)
erosion=cv2.erode(img,k,iterations=1)

cv2.imshow('img',img)
#cv2.imshow('dilation',dilation)
cv2.imshow('erosion',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()