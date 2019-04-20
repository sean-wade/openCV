# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:27:52 2019

@author: Sean
"""

import cv2

img = cv2.imread('star.bmp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)
ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
thresh, contours, hie = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

pt = (60, 60)
#pt = (50, 60)
#pt = (40, 60)

#计算点到轮廓的最小距离，True表示计算距离，False表示只判断在轮廓内外，-1，0，1表示外部，轮廓上，内部
ret = cv2.pointPolygonTest(contours[0], pt, True)
print(ret)


cv2.drawContours(img, contours, -1, (0,0,255), 2)
cv2.circle(img, pt, 3, (255,255,0), 2)


cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()