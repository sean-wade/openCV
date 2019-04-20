# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:31:24 2019

@author: Sean
"""

#图像ROI与mask掩码
import cv2


#  不用掩码实现图像logo高级融合,掩码为0的部分不操作
#img=cv2.imread("sdty.png")
#logo=cv2.imread("fangfang.bmp")
#
##roi=img[100:800,400:1100]
#w=logo.shape[0]
#h=logo.shape[1]
#
#for i in range(0,w):
#    for j in range(0,h):
#        if abs(logo[i,j,0]-255)<80 and abs(logo[i,j,1]-255)<80 and abs(logo[i,j,2]-255)<80:
#            logo[i,j]=img[i,j]
#
#img[0:w,0:h]=logo[:,:]
#
#
#cv2.imshow('img',img)
##cv2.imshow('ROI',roi)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#图像掩码操作
img=cv2.imread('sdty.png')
#cv2.imshow('src',img)

logo=cv2.imread('fangfang.bmp')
#cv2.imshow('logo',logo)

w=logo.shape[0]
h=logo.shape[1]

gray=cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

#cv2.imshow('gray',gray)
ret,mask1=cv2.threshold(gray,180,255,cv2.THRESH_BINARY_INV)

logo_temp=cv2.bitwise_and(logo,logo,mask=mask1)

mask1_inv=cv2.bitwise_not(mask1)

roi=img[0:w,0:h]
roi_temp=cv2.bitwise_and(roi,roi,mask=mask1_inv)
roi=cv2.add(roi_temp,logo_temp)

img[:w,:h]=roi

#cv2.imshow('mask1_inv',mask1_inv)
#cv2.imshow('mask1',mask1)
#cv2.imshow('logo_temp',logo_temp)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()








