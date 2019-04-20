# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:23:22 2019

@author: Sean
"""
#模板匹配及应用

import cv2
import numpy as np

img=cv2.imread("cp.bmp")
tem=cv2.imread("a.bmp")
img2=img.copy()

res=cv2.matchTemplate(img,tem,cv2.TM_CCORR_NORMED)

min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)    #返回值：最小最大匹配值，最小匹配值坐标，最大匹配值坐标

cv2.rectangle(img,max_loc,(max_loc[0]+tem.shape[0],max_loc[1]+tem.shape[1]),(0,0,255),3)

cv2.imshow('img',img)
cv2.imshow('a',tem)


loc=np.where(res>0.99)
#for pt in zip(*loc[::-1]):
##    cv2.rectangle(img2,pt,(pt[0]+tem.shape[0],pt[1]+tem.shape[1]),(0,255,0),1)
#    print(pt)
#cv2.imshow('img2',img2)


#print(loc)
print(*loc)
#print((*loc[::-1]))
#print((loc[::-1]))

cv2.waitKey(0)
cv2.destroyAllWindows()
