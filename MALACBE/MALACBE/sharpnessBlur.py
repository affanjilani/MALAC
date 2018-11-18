import cv2
import numpy as np

def sharpnessBlur(grayImage,threshold):
    #our flag representing our criteria
    blurred = False

    #compute the laplacian
    fm = cv2.Laplacian(grayImage,cv2.CV_64F).var()

    #compare the sharpness to a threshold
    if fm > threshold:
        blurred = True

    #check if we meet our criteria
    if blurred:
        return False
    else:
        return True
