# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:27:27 2019

@author: Sean
"""

import cv2

#图像滤波



img=cv2.imread("cp3.png")

#1.boxFilter
#dst=cv2.boxFilter(img,-1,(2,2),normalize=False)

#2.blur
#dst=cv2.blur(img,(3,3))

#3.GaussianBlur
#dst=cv2.GaussianBlur(img,(3,3),0)

#4.medianBlur   非线性滤波，去雪花效果明显
dst=cv2.medianBlur(img,3)

#5.bilateralFilter    双边滤波，非线性滤波，可以保存边缘
#dst=cv2.bilateralFilter(img,15,75,75)


cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()