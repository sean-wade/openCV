# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:48:03 2019

@author: Sean
"""

import cv2

#这段有bug，亮度修改与对比度修改无法叠加，参见11_02的写法，不用回调函数写，直接获取进度条数值进行循环计算即可
img=cv2.imread("cp.bmp",0)
img2=img.copy()
def contrastChange(contrastBar):
    global img,img2
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if int(img2[i,j]*contrastBar*0.01)>255:
                img[i,j]=255
            else:
                img[i,j]=int(img2[i,j]*contrastBar*0.01)


def brightnessChange(brightnessBar):
    global img,img2
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if int(img2[i,j]+brightnessBar>255):
                img[i,j]=255
            else:
                img[i,j]=int(img2[i,j]+brightnessBar)


cv2.namedWindow('change')
cv2.createTrackbar('ContrastBar','change',100,1000,contrastChange)
cv2.createTrackbar('Brightness','change',0,255,brightnessChange)

#contrast=1
brightness=0
contrastChange(100)
brightnessChange(0)
cv2.imshow('src',img2)

while 1:
    cv2.imshow('change',img)
    if cv2.waitKey(1)==27:
        break



cv2.destroyAllWindows()