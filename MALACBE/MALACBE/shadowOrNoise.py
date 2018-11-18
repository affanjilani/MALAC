import cv2
import numpy as np
from violaJones import ViolaJonesFD
from faceDetection1 import cannyEdgeDetection

"""A function that checks the criteria that photos with shadows on the face or background are unacceptable """
def shadowOrNoise(greyImage):

    #our flag for the criteria
    noise = False

    #run VJ to get the region of the face
    (newImage,x,y,w,h) = ViolaJonesFD(greyImage)

    #get the 3 regions representing the background, the values are to remove the hair from the background
    backgroundRegion1 = greyImage[0:y+h,0:x-50]
    backgroundRegion2 = greyImage[0:y-250,x:x+w]
    backgroundRegion3 = greyImage[0:y+h,x+w+50:]

    #run edge detection to see if we get any edges in the background
    edgesBackground1 = cannyEdgeDetection(backgroundRegion1,(3,3),0.5,20,60)
    edgesBackground2 = cannyEdgeDetection(backgroundRegion2,(3,3),0.5,20,60)
    edgesBackground3 = cannyEdgeDetection(backgroundRegion3,(3,3),0.5,20,60)

    #sum all the intensities of regions
    cumEdgesBackground1 = np.sum(edgesBackground1)
    cumEdgesBackground2 = np.sum(edgesBackground2)
    cumEdgesBackground3 = np.sum(edgesBackground3)

    #if we detect a single white pixel, then its not a valid background image
    if(cumEdgesBackground1 > 0 or cumEdgesBackground2 > 0 or cumEdgesBackground3 > 0):
        noise = True

    #check if we meet the criteria
    if noise:
        return False
    else:
        return True

#read image and convert to gray
image = cv2.imread('./perfect.jpeg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(shadowOrNoise(image))
