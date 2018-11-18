import cv2
import math
import numpy as np
from violaJones import ViolaJonesFD
from sharpnessBlur import sharpnessBlur
from faceDetection1 import faceDetection1
from shadowOrNoise import shadowOrNoise
from neutralFace import neutralFace

#read image and convert to gray
image = cv2.imread('./perfect.jpeg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#getting the number of pixels to match 70mm by 50mm
widthRegionRequirement = round(float(50*360)/25.4)
heightRegionRequirement = round(float(70*360)/25.4)

#getting half of the requirment
widthFromCenter = round(widthRegionRequirement / 2)
heightFromCenter = round(heightRegionRequirement/2)

#run VJ to get the region of interest
(region,x,y,w,h) = ViolaJonesFD(image)

# xCenter = round(x + (float(w)/2) + (float(h)/2))
# yCenter = round(y + (float(h)/2) + (float(w)/2))
xCenter = round(x + (float(w)/2))
yCenter = round(y + (float(h)/2))

#Region of interest
image = image[int(yCenter - heightFromCenter): int(yCenter + heightFromCenter),int(xCenter-widthFromCenter):int(xCenter + widthFromCenter)]


output = ""
#check the requirements
if (not sharpnessBlur(image,125)):
    output = output + "Image is blurred\n"

if (faceDetection1(image,220)):
    output = output + "The length between the crown and chin is not between 31 and 36mm or both edges are not clearly visible\n"

#if(not shadowOrNoise(image)):
#    output = output + "The photo has shadows on the background or face\n"

if(not neutralFace(image,'./shape_predictor_68_face_landmarks.dat')):
    output = output + "The photo is not neutral\n"

if (len(output) == 0):
    print ("Perfect Passport Photo")
else:
    print(output)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()