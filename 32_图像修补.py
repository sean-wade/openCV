# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:05:42 2019

@author: Sean
"""

#分水岭算法

import cv2
import numpy as np


def main():
    img = cv2.imread('snow.jpg')
    cv2.imshow('src',img)
    
    mask = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
    cv2.rectangle(mask, (42,267),(42+129, 267+116), (255,255,255),-1)
    cv2.rectangle(mask, (181,318),(181+263, 318+59), (255,255,255),-1)
    cv2.imshow('mask', mask)
    
#    dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
    dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    
    cv2.imshow('res', dst)
    cv2.imwrite('snow_inpaint.jpg', dst)
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()