# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:19:41 2019

@author: Sean
"""

import cv2
import numpy as np

font=cv2.FONT_HERSHEY_COMPLEX

img=cv2.imread("yuan.bmp")
cv2.imshow('src',img)
temp=img.copy()

resImg=np.zeros(img.shape)

gray=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,155,255,cv2.THRESH_BINARY_INV)
thresh,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

flag=0
cv2.namedWindow('contours')
cv2.putText(resImg,'Nums=%s'%str(len(contours)),(10,30),font,1,(0,0,255),2)

for cnt in contours:    #遍历所有轮廓
    for j in range(0,len(cnt)):    #遍历cnt轮廓中的所有点
        cv2.drawContours(resImg,cnt,j,(0,255,0),5)
        if cv2.waitKey(3)==27:
            flag=1    #退出第一层循环
            break
        cv2.imshow('contours',resImg)
    if flag:    #退出第二层循环
        break
cv2.waitKey(0)
cv2.destroyAllWindows()