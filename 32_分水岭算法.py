# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:05:42 2019

@author: Sean
"""

#分水岭算法

import cv2
import numpy as np


def main():
    img = cv2.imread('bird.jpg')
    
    (cols, rows, channels) = img.shape
    
    marker = np.zeros((cols, rows, 1), np.uint8)
    
    # marker图像分区域做标记，手动标记。另外也可以进行阈值化、膨胀腐蚀等操作获得标记图
    cv2.rectangle(marker, (10, 10), (60, 60), (64,64,64), -1)    #背景
    cv2.rectangle(marker, (260, 160), (258, 216), (128,128,128), -1)    #鸟
    cv2.rectangle(marker, (300, 255), (320, 270), (255,255,255), -1)    #石头
    
    marker32 = np.int32(marker)
    
    cv2.imshow('marker', marker)
    
    cv2.watershed(img, marker32)
    
    m = cv2.convertScaleAbs(marker32)
    
    cv2.imshow('m_watershed', m)
#    ret, mask1 = cv2.threshold(m, 129, 255, cv2.THRESH_BINARY)    #255,石头 
#    ret, mask1 = cv2.threshold(m, 65, 255, cv2.THRESH_BINARY_INV)    #64, 背景 
    m = cv2.bitwise_not(m)
    ret, mask1 = cv2.threshold(m, 130, 255, cv2.THRESH_TOZERO_INV)    #128, 鸟
    
    cv2.imshow('mask1', mask1)
    bird = cv2.bitwise_and(img, img, mask = mask1)
    
    cv2.imshow('bird', bird)
    
    
    
    
    
    cv2.imshow('src',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()