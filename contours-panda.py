#!/usr/bin/env python

'''
This program illustrates the use of findContours and drawContours.
The original image is put up along with the image of drawn contours.

Usage:
    contours.py
A trackbar is put up which controls the contour level from -3 to 3
'''

# Python 2/3 compatibility
from __future__ import print_function
import sys
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range

import numpy as np
import cv2

def make_image():
    img = np.zeros((500, 500), np.uint8)
    black, white = 0, 255
    for i in xrange(6):
        dx = int((i%2)*250-20)
        dy = int((i/1.5)*170)

        """if i == 0:
            for j in xrange(11):
                angle = (j+5)*np.pi/21
                c, s = np.cos(angle), np.sin(angle)
                x1, y1 = np.int32([dx+100+j*10-80*c, dy+100-90*s])
                x2, y2 = np.int32([dx+100+j*10-30*c, dy+100-30*s])
                cv2.line(img, (x1, y1), (x2, y2), white)"""

        cv2.ellipse( img, (dx+150, dy+100), (105,110), 0, 0, 360, white, -1 ) #head
        cv2.ellipse( img, (dx+110, dy+70), (37,25), -45, 0, 360, black, -1 )#left eye white
        cv2.ellipse( img, (dx+190, dy+70), (37,25), 45, 0, 360, black, -1 )#right eye white
        cv2.ellipse( img, (dx+115, dy+70), (15,15), 0, 0, 360, white, -1 )#left iris
        cv2.ellipse( img, (dx+185, dy+70), (15,15), 0, 0, 360, white, -1 )#right iris
        cv2.ellipse( img, (dx+115, dy+70), (5,5), 0, 0, 360, black, -1 )#left pupil
        cv2.ellipse( img, (dx+185, dy+70), (5,5), 0, 0, 360, black, -1 )#right puil
        cv2.ellipse( img, (dx+150, dy+130), (15,15), 0, 180, 360, black, -1 )#nose
        cv2.ellipse( img, (dx+150, dy+150), (25,5), 0, -5, 185, black, -1 )#mouth
        cv2.ellipse( img, (dx+52, dy+50), (30,30), 0, 0, 360, white, -1 )#left ear
        cv2.ellipse( img, (dx+247, dy+50), (30,30), 0, 0, 360, white, -1 )#right
        cv2.ellipse( img, (dx+52, dy+50), (28,28), 0, 105, 304, black, -1 )#left ear
        cv2.ellipse( img, (dx+247, dy+50), (28,28), 0, 235, 433, black, -1 )#right
        #cv2.ellipse( img, (dx+100, dy+120), (25,20), 0, 0, 360, 150, -1 )#left cheek
        #cv2.ellipse( img, (dx+200, dy+120), (25,20), 0, 0, 360, 150, -1 )#right cheek

    return img

if __name__ == '__main__':
    print(__doc__)

    img = make_image()
    h, w = img.shape[:2]

    _, contours0, hierarchy = cv2.findContours( img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]

    def update(levels):
        vis = np.zeros((h, w, 3), np.uint8)
        levels = levels - 3
        cv2.drawContours( vis, contours, (-1, 2)[levels <= 0], (128,255,255),
            3, cv2.LINE_AA, hierarchy, abs(levels) )
        cv2.imshow('contours', vis)
    update(3)
    cv2.createTrackbar( "levels+3", "contours", 3, 7, update )
    cv2.imshow('image', img)
    0xFF & cv2.waitKey()
    cv2.destroyAllWindows()
