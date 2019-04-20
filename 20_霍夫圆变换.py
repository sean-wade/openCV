# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:46:45 2019

@author: Sean
"""

import cv2
import numpy as np

# 霍夫线变换
img=cv2.imread('dlam.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)
edges=cv2.Canny(blur,50,150,apertureSize=3)
cv2.imshow('src',img)


#  参数含义。1：距离精度（1个像素），pi/180：角度精度，150：阈值（线条长度大于150才算）
#  标准霍夫线变换，返回值是极坐标rho和theta的集合
#lines=cv2.HoughLines(edges,1,np.pi/180,150)  #霍夫线变换
##print(lines)
#lines2=lines[:,0,:]
##print(lines2)
#
#for rho,theta in lines2[:]:
#    print('rhos=%s'%rho,'theta=%0.2f'%(theta*180/np.pi))
#    a=np.cos(theta)
#    b=np.sin(theta)
#    x0=a*rho
#    y0=b*rho
#    x1=int(x0+1000*(-b))
#    y1=int(y0+1000*(a))
#    x2=int(x0-1000*(-b))
#    y2=int(y0-1000*(a))
#    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#    cv2.circle(img,(x0,y0),2,(0,255,0),-1,cv2.LINE_AA)


#    累计概率霍夫线变换，返回值与标准霍夫线变换不同，为x1,y1,x2,y2两个点的集合
#lines=cv2.HoughLinesP(edges,1,np.pi/360,100,120,20)
#lines2=lines[:,0,:]
##print(lines2)
###print(lines2[0,:])
#for x1,y1,x2,y2 in lines2[:]:
#    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)



#霍夫圆变换
circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,2,50,param1=200,\
                         param2=100,minRadius=10,maxRadius=50)
circles=np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    #圆心
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()























