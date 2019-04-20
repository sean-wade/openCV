# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:32:38 2019

@author: Sean
"""

#灰度模式下增加亮度与对比度
import cv2

img=cv2.imread("cp.bmp",0)
img2=img.copy()

cv2.namedWindow('Source')
cv2.namedWindow('Adjust')

def nothing(x):
    pass

cv2.createTrackbar('Constrast','Adjust',100,1000,nothing)
cv2.createTrackbar('Brightness','Adjust',0,255,nothing)

d=0
while True:
    cv2.imshow('Source',img)
    if cv2.waitKey(1)==27:
        break
    c=cv2.getTrackbarPos('Constrast','Adjust')
    b=cv2.getTrackbarPos('Brightness','Adjust')
    if d!=b+c:    #判断进度条是否改变，防止没改变也进入循环变卡
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                if int(img[i,j]*c*0.01+b>255):
                    img2[i,j]=255
                else:
                    img2[i,j]=img[i,j]*c*0.01+b
    cv2.imshow('Adjust',img2)
    d=b+c    #循环退出时记录上次的进度条值
    
cv2.destroyAllWindows()