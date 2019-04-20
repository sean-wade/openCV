# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:34:53 2019

@author: Sean
"""

import cv2

font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.imread('star.bmp')
cv2.imshow('src',img)

temp=img.copy()
gray=cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
ret,thresh=cv2.threshold(gray,200,250,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh',thresh)

#寻找轮廓
thresh,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
#输出轮廓个数
print(len(contours))

#绘制轮廓，-1为轮廓索引，小于0即所有轮廓
cv2.drawContours(img,contours,-1,(255,0,255),2)

#for循环绘制轮廓，寻找轮廓中的cv2.CHAIN_APPROX_SIMPLE(NONE)有区别
#for cnt in contours:
#    cv2.drawContours(img,cnt,-1,(255,0,255),5)

cv2.putText(img,'Nums = %s'%str(len(contours)),(10,30),font,0.9,(0,0,0),2)

cv2.imshow('contours',img)
#cv2.imshow('ths',thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()