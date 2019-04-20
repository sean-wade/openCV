# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:38:10 2019

@author: Sean
"""

import numpy as np
import cv2


img = cv2.imread('bird.jpg')
cv2.imshow('bird', img)

mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (140,90,300,150)
"""
原图，掩码（同时是输出结果），矩形，背景模型（内部使用），前景模型（内部），迭代次数，参数mode=GC_INIT_WITH_RECT
rect: 包含分割对象的矩形ROI, 矩形外部的像素为背景, 矩形内部的像素为前景，当参数mode=GC_INIT_WITH_RECT使用
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 2, cv2.GC_INIT_WITH_RECT)
在处理结束之后，mask中会保存结果。Mask只能取4种可能的值(0 ~ 4):
    GC_BGD: 表示明确属于背景的像素
    GC_FGD: 表示明确属于前景的像素
    GC_PR_BGD: 表示可能属于背景的像素
    GC_PR_FGD: 表示可能属于前景的像素
"""
#cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 2, cv2.GC_INIT_WITH_RECT)


cv2.rectangle(mask, (150, 110),(330,230), (3,3,3), -1)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 2, cv2.GC_INIT_WITH_MASK)

cv2.imshow('mask', mask)
#print(mask[100:150,180:250])

mask2 = np.where((mask == 1)|(mask == 3), 1, 0).astype('uint8')
#mask2 = np.where((mask == 3), 1, 0).astype('uint8')
#mask2 = np.where((mask == 2), 1, 0).astype('uint8')
#print(img.shape)
#print(mask2.shape)
img = img * mask2[:,:,np.newaxis]    #mask2是292*500的，增加一个维度，变为292*500*1，与img一致。
#   *   应该是各个元素相乘，因此img为1的保留，0的变成0


cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

























































