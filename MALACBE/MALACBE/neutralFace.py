import numpy as np
import argparse 
import imutils
import dlib
import cv2
from imutils import face_utils



def neutralFace(image, models):

	#initialize dlib face detector as well as predictor
	detector = dlib.get_frontal_face_detector()
	#the predictor needs the training data
	predictor = dlib.shape_predictor(models)

	# load the input image, resize it, and convert it to grayscale
	image = cv2.imread(image)
	image = imutils.resize(image, width=900)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
	# detect faces in the grayscale image
	rects = detector(gray, 1)

	#from the face detected, now iterate through the face and find the features
	for (i,rect) in enumerate(rects):
		shape = predictor(gray, rect)		     #gets all 68 (x,y) coordinates corresponding to the features
		shape = face_utils.shape_to_np(shape)    #turns the 68 coordinates into a numpy array

		#now convert the dlib rectangle to the (x,y,width, height) rectangles we like in python
		(x,y,width,height) = face_utils.rect_to_bb(rect)
		cv2.rectangle(image, (x,y), (x+width, y+height), (0,255,0),2)

		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image
		for (x, y) in shape:
			cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
 
		# show the output image with the face detections + facial landmarks
		cv2.imshow("Output", image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


neutralFace('./testImages/jackie.jpg','./shape_predictor_68_face_landmarks.dat')