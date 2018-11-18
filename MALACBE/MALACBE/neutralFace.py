import numpy as np
import argparse 
import imutils
import dlib
import math
import cv2
from imutils import face_utils



def neutralFace(image, models):

    frown = False
    smile = False
    closed = False
    open = False

    #initialize dlib face detector as well as predictor
    detector = dlib.get_frontal_face_detector()
    #the predictor needs the training data
    predictor = dlib.shape_predictor(models)

    #resize the image
    image = imutils.resize(image, width=900)

    # detect faces in the grayscale image
    rects = detector(image, 1)

    #from the face detected, now iterate through the face and find the features
    for (i,rect) in enumerate(rects):
        shape = predictor(image, rect)		     #gets all 68 (x,y) coordinates corresponding to the features
        shape = face_utils.shape_to_np(shape)    #turns the 68 coordinates into a numpy array

        #now convert the dlib rectangle to the (x,y,width, height) rectangles we like in python
        (x,y,width,height) = face_utils.rect_to_bb(rect)
        #cv2.rectangle(image, (x,y), (x+width, y+height), (0,255,0),2)

        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image

        for (x, y) in shape:
            #cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
            (xmouth,ymouth) = shape[66]

        # #blur the image
        blurredImage = cv2.GaussianBlur(image,(3,3),0.5)
        # mouthOpenSection = gray[ymouth-10:ymouth+10,xmouth-10:xmouth+10]
        # height,width = mouthOpenSection.shape
        # print height/2-2
        # laplacian = cv2.Laplacian(mouthOpenSection,cv2.CV_64F)
        # sobely = cv2.Sobel(mouthOpenSection,cv2.CV_64F,0,1,ksize=5)
        # print laplacian[height/2+1-3:height/2+1+3,11]
        # print laplacian[11,11]
        # print sobely[height/2+1-3:height/2+1+3,11]
        # print sobely[11,11]
        # if(abs(laplacian[11,11])+abs(laplacian[10,11])>=13 or shape[67,1]-shape[63,1]>3 ):
        # 	(secx,secy) = shape[62]
        # 	cv2.circle(image,(xmouth,ymouth),1,(255,0,0),-1)
        # 	cv2.circle(image,(secx,secy),1,(255,0,0),-1)

        # (secx,secy) = shape[62]
        # cv2.circle(image,(xmouth,ymouth),1,(255,0,0),-1)
        # cv2.circle(image,(secx,secy),1,(255,0,0),-1)

        #region for the eyes
        (xRightEye,yRightEye) = shape[44]
        (x1RightEye,y1RightEye) = shape[46]
        (xLefttEye, yLeftEye) = shape[38]
        (x1LeftEye, y1LeftEye) = shape[40]

        #region of the frown
        (xFrown,yFrown) = shape[21]
        (xFrown2,yFrown2) = shape[22]
        (xFrown3,yFrown3) = shape[27]

        #smile region
        (xTopLip,yTopLip) = shape[51]
        (xBottomLip,yBottomLip) = shape[58]



    #get the region of interest for frown detection
    frowingRegion = image[yFrown - 20:yFrown-yFrown3, xFrown+5: xFrown2-15]

    #check if the photo is frowning
    frown = isFrowing(frowingRegion)
    # check if mouth is open
    open = isMouthOpen(shape, blurredImage)
    #check if the eyes are closed
    closed = isEyesClosed(xRightEye,yRightEye,x1RightEye,y1RightEye,xLefttEye, yLeftEye,x1LeftEye, y1LeftEye)
    #check if the photo is smiling or not
    smile = isSmiling(xTopLip,xBottomLip,yTopLip,yBottomLip)

    if(frown or open or closed or smile):
        return False
    else:
        return True

"""Function that implements frown detection"""
def isFrowing(grayImage):

    # #get the size of the matrix
    numElements = math.pow(len(grayImage),2)
    #
    # #the average of gray scale color
    # average = float(np.sum(grayImage)) / numElements
    #
    # #our threshold
    # threshold = average*0.75
    #
    # #normalizing the region
    # nomalizedRegion = grayImage / numElements
    #
    # #add all the pixels
    # sumOfNormalized = np.sum(nomalizedRegion)
    #
    # #check the criteria
    # if sumOfNormalized > threshold:
    #     return True
    # else:
    #     return False

    blurred = cv2.GaussianBlur(grayImage,(5,5),1,0)
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)

    totalX = np.sum(sobelx)
    totalY = np.sum(sobely)

    totalX = float(totalX) / numElements
    totalY = float(totalY) / numElements

    if(abs(totalX) > 2 and abs(totalY)):
        return True
    else:
        return False


"""A function that detects if a mouth is open or not"""
def isMouthOpen(featurePoints,image):

    (xmouth,ymouth) = featurePoints[66]
    #blur the image
    #blurredImage = cv2.GaussianBlur(gray,3,0.5)
    mouthOpenSection = image[ymouth-25:ymouth+25,xmouth-25:xmouth+25]
    height,width = mouthOpenSection.shape
    laplacian = cv2.Laplacian(mouthOpenSection,cv2.CV_64F)
    # sobely = cv2.Sobel(mouthOpenSection,cv2.CV_64F,0,1,ksize=5)
    # print laplacian[height/2+1-3:height/2+1+3,11]
    # print laplacian[11,11]
    # print sobely[height/2+1-3:height/2+1+3,11]
    # print sobely[11,11]
    #print abs(laplacian[11,11]-laplacian[10,11])
    if(abs(laplacian[11,11]-laplacian[10,11])>=13 or featurePoints[66,1]-featurePoints[62,1]>7 ):
        # (secx,secy) = featurePoints[62]
        # cv2.circle(image,(xmouth,ymouth),1,(255,0,0),-1)
        # cv2.circle(image,(secx,secy),1,(255,0,0),-1)
        #print abs(laplacian[11,11]-laplacian[10,11])
        # print featurePoints[66,1]-featurePoints[62,1]
        return True
    else:
        return False


"""Function that detects if your eyes are closed. Parameters are tuples"""
def isEyesClosed(xRightEye,yRightEye,x1RightEye,y1RightEye,xLeftEye, yLeftEye,x1LeftEye, y1LeftEye):
    leftEyeDistance  = math.sqrt( math.pow(xLeftEye - x1LeftEye,2) + math.pow(yLeftEye - y1LeftEye,2))
    rightEyeDistance = math.sqrt( math.pow(xRightEye - x1RightEye,2) + math.pow(yRightEye - y1RightEye,2))

    if leftEyeDistance < 7 or rightEyeDistance < 7:
        return True
    else:
        return False

"Function that detects if your smiling or not"
def isSmiling(xTopLip,xBottomLip,yTopLip,yBottomLip):
    distance = math.sqrt( math.pow(xTopLip - xBottomLip,2) + math.pow(yTopLip - yBottomLip,2))

    if distance < 20:
        return True
    else:
        return False