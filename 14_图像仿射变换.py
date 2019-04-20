# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:01:12 2019

@author: Sean
"""

import cv2
import numpy as np
import math
img=cv2.imread("cp.bmp")

#dst=cv2.resize(img,None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC)    #三次样条插值
#dst=cv2.resize(img,(1900,1000))#默认是线性插值
#dst=cv2.resize(img,None,fx=0.6,fy=0.6,interpolation=cv2.INTER_AREA)

rows,cols,channel=img.shape
M=np.float32([[1,0,100],[0,1,50]])
#dst=cv2.warpAffine(img,M,(cols,rows))    #仿射变换,图像大小不变，信息丢失
#dst=cv2.warpAffine(img,M,(cols+100,rows+50))    #仿射变换，图像大小改变，信息保留

#M=cv2.getRotationMatrix2D((cols/2,rows/2),270,1)
#dst=cv2.warpAffine(img,M,(cols,rows))
##仿射变换进行图像旋转，信息丢失

#dst=cv2.transpose(img)
#dst=cv2.flip(img,0)    #flipCode=0,>0,<0确定镜像方式（x轴，y轴，中心对称）



#重映射，y轴sin变换
xMap=np.zeros(img.shape[:2],np.float32)
yMap=np.zeros(img.shape[:2],np.float32)

rows=img.shape[0]
cols=img.shape[1]

for i in range(0,rows):
    for j in range(0,cols):
        xMap.itemset((i,j),j)
        yMap.itemset((i,j),i+5*math.sin(j/10.0))

#print(yMap)
#print(yMap)

dst=cv2.remap(img,xMap,yMap,interpolation=cv2.INTER_LINEAR)


cv2.imshow('cp',img)
cv2.imshow('resize',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()








