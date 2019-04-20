# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:18:50 2019

@author: Sean
"""

#图像通道的分离与合并
import cv2

img=cv2.imread("cp.bmp")
cv2.imshow('src',img)
#b,g,r=cv2.split(img)

b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
b[:,:]=0

#cv2.imshow('B',b)
#cv2.imshow('G',g)
#cv2.imshow('R',r)

dst=cv2.merge([b,g,r])

cv2.imshow('dst',dst)

#cv2.imwrite('C:/Users/Sean/Desktop/cv/sdty_rgb_mix.jpg',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()