# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:43:21 2019

@author: Sean
"""

#图像阈值化
import cv2

img=cv2.imread("sdty.png",0)

#ret1,dst1=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
#ret2,dst2=cv2.threshold(img,80,255,cv2.THRESH_TOZERO)
#dst2=cv2.medianBlur(dst1,3)
#dst2=cv2.GaussianBlur(dst1,(3,3),0)
#dst2=cv2.bilateralFilter(dst1,9,125,175)





#  Otsu自动根据双峰图片直方图确定阈值，返回ret    
ret,dst=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('src',dst)
print(ret)


#def change(x):
#    global img,dst1
##    ret1,dst1=cv2.threshold(img,x,255,cv2.THRESH_BINARY)
#    #自适应阈值 可以Gaussian方法，也可以mean方法
##    dst1=cv2.adaptiveThreshold(img,x,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#cv2.namedWindow('A')
#cv2.createTrackbar('Thres','A',200,255,change)

#change(200)
#
#while True:
#    cv2.imshow('A',dst1)
#    if cv2.waitKey(1)==27:
#        break

#cv2.imshow('dst2',dst2)
#cv2.imshow('dst2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()