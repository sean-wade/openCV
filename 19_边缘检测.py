# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:56:03 2019

@author: Sean
"""

import cv2


# Canny算子边缘检测    Laplacian算子
img=cv2.imread("cp.bmp",0)
img=cv2.GaussianBlur(img,(3,3),0)

#edged=cv2.Canny(img,30,155)
laplacian=cv2.Laplacian(img,cv2.CV_16S,ksize=3)
result=cv2.convertScaleAbs(laplacian)

cv2.imshow('src',img)
cv2.imshow('edged',result)

cv2.waitKey(0)
cv2.destroyAllWindows()




#    应用Sobel算子进行对焦检测，通过摄像头，边缘检测 
#def AutoFocus(img):
#    img=cv2.blur(img,(3,3))
#    x=cv2.Sobel(img,cv2.CV_16S,1,0,ksize=3)
#    y=cv2.Sobel(img,cv2.CV_16S,0,1,ksize=3)
#    absX=cv2.convertScaleAbs(x)    #转回uint8
#    absY=cv2.convertScaleAbs(y)
#    dst=cv2.addWeighted(absX,0.5,absY,0.5,0)
#    cv2.imshow('DST',dst)
#    sumGray=0
#    for i in range(0,img.shape[0]):
#        for j in range(0,img.shape[1]):
#            sumGray+=dst[i,j]
#    avrGray=float(sumGray/(img.shape[0]*img.shape[1]))    #平均灰度值
#    return avrGray
#
#
#
#font=cv2.FONT_HERSHEY_COMPLEX
#cap=cv2.VideoCapture(0)
#flag=0
#if cap.isOpened():
#    flag=1
#else:
#    flag=0
#
#if flag==1:
#    while True:
#        ret,frame=cap.read()
#        if ret==False:
#            break
#        grayImg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#        ret=AutoFocus(grayImg)
#        text="Focus=%0.2f"%ret
#        cv2.putText(frame,text,(10,20),font,1,(0,255,0),2)
#        cv2.imshow('Video',frame)
#        if cv2.waitKey(1)==27:
#            break
#        
#cap.release()
#cv2.destroyAllWindows()










