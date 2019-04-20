# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:32:38 2019

@author: Sean
"""
# 彩色模式增加亮度和对比度,用了初学的多线程，卡的要死
import cv2
import threading

img=cv2.imread("cp.bmp")
img2=img.copy()

cv2.namedWindow('Source')
cv2.namedWindow('Adjust')

def nothing(x):
    pass

def change():
    global img,img2
    for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                if int(img[i,j,0]*c*0.01+b>255):
                    img2[i,j,0]=255
                else:
                    img2[i,j,0]=img[i,j,0]*c*0.01+b
                if int(img[i,j,1]*c*0.01+b>255):
                    img2[i,j,1]=255
                else:
                    img2[i,j,1]=img[i,j,1]*c*0.01+b
                if int(img[i,j,2]*c*0.01+b>255):
                    img2[i,j,2]=255
                else:
                    img2[i,j,2]=img[i,j,2]*c*0.01+b

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
        t=threading.Thread(target=change)
        t.start()
    cv2.imshow('Adjust',img2)
    d=b+c    #循环退出时记录上次的进度条值
    
cv2.destroyAllWindows()