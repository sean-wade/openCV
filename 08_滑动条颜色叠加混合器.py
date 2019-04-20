# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:56:53 2019

@author: Sean
"""

import cv2
import numpy as np
#滑动条回调函数  二值化
#def onThreshold(minThres):
#    global img,thres_img    #全局变量
#    ret,thres_img=cv2.threshold(img,minThres,255,cv2.THRESH_BINARY) #二值化
#
#img=cv2.imread("C:/Users/Sean/Desktop/sdty.png",0)    #灰度模式加载
#thres_img=img.copy()
#cv2.namedWindow('ThresIMG')
#cv2.createTrackbar('threshold','ThresIMG',200,255,onThreshold)
#
##onThreshold(100)    #初始调用
#
#while(1):
#    cv2.imshow('IMG',thres_img)
#    k=cv2.waitKey(1)&0xff
#    if k==27:
#        break
#
#cv2.destroyAllWindows()

#滑动条  图像混合
#img1=cv2.imread('C:/Users/Sean/Desktop/sdty.png')
#img2=cv2.imread('C:/Users/Sean/Desktop/sdty2.png')
#
#def onAddWeighted(weightValue):
#    global dst
#    dst=cv2.addWeighted(img1,float(weightValue)/100,img2,float(100-weightValue)/100,0)
#    
#dst=np.zeros(img1.shape,np.uint8)
#cv2.namedWindow("Combine")
#cv2.createTrackbar('Weighted','Combine',50,100,onAddWeighted)
#onAddWeighted(50)
#
#while(1):
#    cv2.imshow('Combine',dst)
#    if cv2.waitKey(1)==27:
#        break
#
#cv2.destroyAllWindows()

#四个滑动条实现颜色叠加混合器
def nothing(x):
    pass

img=np.zeros((600,400,3),np.uint8)
cv2.namedWindow("mix")
cv2.createTrackbar('R','mix',0,255,nothing)
cv2.createTrackbar('G','mix',0,255,nothing)
cv2.createTrackbar('B','mix',0,255,nothing)
switch='0:OFF--1:ON\n'
cv2.createTrackbar(switch,'mix',0,1,nothing)

while 1:
    cv2.imshow('mix',img)
    if cv2.waitKey(1)==27:
        break
    r=cv2.getTrackbarPos('R','mix')
    g=cv2.getTrackbarPos('G','mix')
    b=cv2.getTrackbarPos('B','mix')
    s=cv2.getTrackbarPos(switch,'mix')
    if s==1:
        img[:]=[b,g,r]    #openCV存储颜色是BGR
    else:
        img[:]=0
cv2.destroyAllWindows()






