# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:33:25 2019

@author: Sean
"""

import numpy as np

import cv2

cap = cv2.VideoCapture('play.wmv')

ret,frame = cap.read()

#cv2.imwrite('1.bmp',frame)

cols,rows,w, h = 61,191,15,38

track_window = (cols,rows,w,h)

roi = frame[rows:rows+h,cols:cols+w]

cv2.imshow('roi',roi)

cv2.waitKey(0)

hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv_roi, np.array((0, 70,70)), np.array((10,255,255)))

roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])

cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

#终止条件
term_crit =(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
  ret ,frame = cap.read()
  if ret == True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    cv2.imshow('back',dst)

    ret, track_window = cv2.meanShift(dst, track_window, term_crit)

    x,y,w,h = track_window
    img2 = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('tracking',img2)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
      break
  else:
    break
cv2.destroyAllWindows()

cap.release()
