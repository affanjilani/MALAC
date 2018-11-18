import cv2
import numpy as np
from violaJones import ViolaJonesFD

"""A function that check the criteria that the lenght between the crown of head and chin are between 31 and 36mm
    as well as ensures that both edges are visible
"""
def faceDetection1(grayImage,dpi):
    #flag for our crown of head to chin criteria
    crownToChin = False

    #flag showing both edges clearly
    bothEdges = False

    try:
        # detect the face using Viola Jones algorithm and find the region
        (region,x,y,w,h) = ViolaJonesFD(grayImage)

        #next we run canny edge detection
        binaryImage = cannyEdgeDetection(region,(7,7),1.5,20,60)

        #getting the length from chin to crown
        height = len(binaryImage)

        #one inch is 25.4 mm
        inchToMillimeters = 25.4

        #equation to convert pixels to mm
        length = round(height * (inchToMillimeters/dpi))
        length = float(length)/ 2

        #check if the length matches the criteria which is between 31mm and 36mm
        if 31 < length and length < 36:
            crownToChin = True

        #counter to check how many times we detect a side edge
        sideEdgesCounter = 0

        #our thresholds for detecting side edges. 255 is a white pixel
        tLow = (height - 40) * 255
        tHigh = (height + 30) * 255


        #checking if the image shows both edges clearly
        for col in range(1,len(region[0])-1):
            columns = region[:,col-1:col+1]
            sum = np.sum(columns)
            if tLow < sum and sum < tHigh:
                #its a side edge
                sideEdgesCounter += 1

        #if we detect 2 or more side edges then we are it is accepted
        if sideEdgesCounter >= 2:
            bothEdges = True

        if bothEdges and crownToChin:
            return True
        else:
            return False

    except:

    # check if we meet face detection criteria 1
        if bothEdges and crownToChin:
            return True
        else:
            return False

"""Function that compute edge detection using Canny. it takes in a grayscale image, 
    a kernel size and a sigma for blurring and 2 threshold
"""
def cannyEdgeDetection(grayImage,kernel,sigma,tLow,tHigh):
    # blur the image with sigma 1.5 and 7x7 kernel
    blurredImage = cv2.GaussianBlur(grayImage,kernel, sigma)
    # run canny on the images
    binaryImage = cv2.Canny(blurredImage, tLow, tHigh)

    return binaryImage
