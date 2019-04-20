# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:57:44 2019

@author: Sean
"""

#直方图均衡化 
import cv2
import numpy as np


#对灰度图片进行均衡化，单通道八位
img=cv2.imread("tanke.jpg",0)

#处理整体偏暗或者偏亮的图片效果明显
#equ=cv2.equalizeHist(img)
#合并


#自适应均衡化，防止杂讯信息出现，可在直方图均衡化丢失一部分信息时采取
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
result=clahe.apply(img)

res=np.hstack((img,result))
cv2.imshow('res',res)
#cv2.imshow('result',equ)
#cv2.imwrite('equ.bmp',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()

#对彩色图像进行均衡化，分别对各通道进行均衡化

#img=cv2.imread("tanke.jpg")
#b,g,r=cv2.split(img)
#
#b1=cv2.equalizeHist(b)
#g1=cv2.equalizeHist(g)
#r1=cv2.equalizeHist(r) 
#
#equ=cv2.merge([b1,g1,r1])
#
#res=np.hstack((img,equ))
#
#cv2.imwrite('tankeEqu.jpg',res)
#cv2.imshow("res",res)
#cv2.waitKey(0)
#cv2.destroyAllWindows()













