# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:34:59 2019

@author: Sean
"""

import cv2
import numpy as np


def nothing(a):
    pass

def main():
    img = cv2.imread('pg3.jpg')
    cv2.imshow('img', img)
    
    cv2.namedWindow('HSV_debug')
    cv2.namedWindow('ret')
    
    cv2.createTrackbar('h_min', 'HSV_debug', 0, 180, nothing)
    cv2.createTrackbar('s_min', 'HSV_debug', 0, 255, nothing)
    cv2.createTrackbar('v_min', 'HSV_debug', 0, 255, nothing)
    
    cv2.createTrackbar('h_max', 'HSV_debug', 0, 180, nothing)
    cv2.createTrackbar('s_max', 'HSV_debug', 0, 255, nothing)
    cv2.createTrackbar('v_max', 'HSV_debug', 0, 255, nothing)
    
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    while True:
        h_min = cv2.getTrackbarPos('h_min', 'HSV_debug')
        s_min = cv2.getTrackbarPos('s_min', 'HSV_debug')
        v_min = cv2.getTrackbarPos('v_min', 'HSV_debug')
        
        h_max = cv2.getTrackbarPos('h_max', 'HSV_debug')
        s_max = cv2.getTrackbarPos('s_max', 'HSV_debug')
        v_max = cv2.getTrackbarPos('v_max', 'HSV_debug')
        
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        
        mask1 = cv2.inRange(hsv_img, lower, upper)
        
        img2 = cv2.bitwise_and(img, img, mask=mask1)
        
        cv2.imshow('HSV_debug', mask1)
        cv2.imshow('ret', img2)
        
        if cv2.waitKey(10)==27:
            break
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()






















