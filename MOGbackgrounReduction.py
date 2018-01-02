'''
As the name suggests, BS calculates the foreground mask performing a subtraction
between the current frame and a background model, containing the static part of the scene
or, more in general, everything that can be considered as background given the characteristics
of the observed scene.
Background modeling consists of two main steps:

Background Initialization;
Background Update.
In the first step, an initial model of the background is computed, 
while in the second step that model is updated in order to adapt to possible changes in the scene

'''

import numpy as np
import cv2

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()   #initial model of the background is computed

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)       #model is updated in order to adapt to possible changes in the scene
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:                      #press escape to exit
        break
    

cap.release()
cv2.destroyAllWindows()

