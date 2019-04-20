# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:44:51 2019

@author: Sean
"""

import numpy as np
import cv2
#from common import Sketcher
import common

if __name__ == '__main__':
    import sys
    try:
        fn = sys.argv[1]
    except:
        fn = 'face.jpg'

    img = cv2.imread(fn)
    if img is None:
        print('Failed to load image file:', fn)
        sys.exit(1)
    cv2.imshow('src',img)
    img_mark = img.copy()
    mark = np.zeros(img.shape[:2], np.uint8)
    sketch = common.Sketcher('img', [img_mark, mark], lambda : ((255, 255, 255), 255))

    while True:
        ch = 0xFF & cv2.waitKey()
        if ch == 27:
            break
        if ch == ord(' '):
            res = cv2.inpaint(img_mark, mark, 3, cv2.INPAINT_TELEA)
            cv2.imshow('inpaint', res)
        if ch == ord('r'):
            img_mark[:] = img
            mark[:] = 0
            sketch.show()
    cv2.destroyAllWindows()
