# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:51:20 2019

@author: Sean
"""

import cv2

img1=cv2.imread("sdty2.png")
img2=cv2.imread("sdty3.jpg")


#图像加减法，要求图像必须有相同的大小和类型
#dst=cv2.add(img1,img2)
#dst=img1+img2    #模运算，不推荐 除以255的余数
#dst=cv2.addWeighted(img1,0.3,img2,0.7,0)
#dst=cv2.subtract(img2,img1)
#dst=cv2.absdiff(img1,img2)    #可寻找图片细微差异

#图像乘除法，不推荐，无溢出保护，实际是对比度操作
#dst=img1*2
#dst=img2/2

#图像逻辑运算
#dst=cv2.bitwise_and(img1,img2)
#dst=cv2.bitwise_or(img1,img2)
dst=cv2.bitwise_not(img2)
#dst=cv2.bitwise_xor(img1,img2)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()