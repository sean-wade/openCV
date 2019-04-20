# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:03:34 2019

@author: Sean
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


###灰度图的直方图
#img=cv2.imread('sdty.png',0)
##hist=cv2.calcHist([img],[0],None,[256],[0,256])  #z这句有什么用？？难道是C++里的？
#plt.hist(img.ravel(),256,[0,256])
#plt.show()

##彩色图的直方图
#img=cv2.imread('tx.bmp')
#color=('red','orange','black')
#
#for i,col in enumerate(color):
#    histr=cv2.calcHist([img],[i],None,[256],[0,256])  #None是掩码，可以设置掩码绘制指定区域直方图
#    plt.plot(histr,color=col)
#    plt.xlim([0,256])
#    
#plt.xlabel('X')
#plt.ylabel('N')
#label=['B','G','R']
#plt.legend(label,loc=0,ncol=1)
#plt.show()

#二维直方图，不太懂
#img=cv2.imread('sdty.png')
#hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#hist=cv2.calcHist([hsv_img],[0,1],None,[256,256],[0,256,0,256])
#plt.imshow(hist,interpolation="nearest")
#plt.show()

#带掩码的直方图

img=cv2.imread("yuan.bmp")
mask=np.zeros(img.shape[:2],np.uint8)
mask[0:250,0:200]=255
img2=img#[0:250,0:200]
color=('b','g','r')

for i,col in enumerate(color):
    histr=cv2.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])

plt.show()

cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()














