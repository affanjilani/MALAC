import numpy as np
import cv2

def ViolaJonesFD(greyImage):
    #loading classifiers
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    #viola jones algorithm
    faces = face_cascade.detectMultiScale(greyImage, 1.3, 5)
    for (x, y, w, h) in faces:
        #all we need is the region
#        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#        roi_gray = gray[y:y + h, x:x + w]
#        roi_color = img[y:y + h, x:x + w]
#        eyes = eye_cascade.detectMultiScale(roi_gray)
#        for (ex, ey, ew, eh) in eyes:
#            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        newIm = greyImage[y:y+w+10,x-5:x+w+5]
    return newIm

def ViolaJonesSD(greyImage):
	#load classifiers
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
	smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

	faces = face_cascade.detectMultiScale(greyImage,1.3,5)
	smile = False
	for (x,y,w,h) in faces:
		roi_gray = greyImage[y:y+h,x:x+w]
		smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.2,
            minNeighbors=22,
            minSize=(25, 25),
            )

		for(sx, sy, sw, sh) in smiles:
			print sx,sy,sw,sh
			cv2.rectangle(roi_gray, (sx,sy), (sx+sw,sy+sh),(0,255,0),2)
			cv2.imshow("yo",roi_gray)
			smile = True

	return smile

# def ViolaJonesSD(greyImage):
# 	#load classifiers
# 	#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 	smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# 	#faces = face_cascade.detectMultiScale(greyImage,1.3,5)
# 	smile = False
	
# 	#roi_gray = greyImage[y:y+h,x:x+w]
# 	smiles = smile_cascade.detectMultiScale(
#         greyImage,
#         scaleFactor= 1.2,
#         minNeighbors=22,
#         minSize=(25, 25),
#         )

# 	for(sx, sy, sw, sh) in smiles:
# 		print sx,sy,sw,sh
# 		cv2.rectangle(greyImage, (sx,sy), (sx+sw,sy+sh),(0,255,0),2)
# 		cv2.imshow("yo",greyImage)
# 		smile = True

# 	return smile


#to test our code
#img = cv.imread('./affan.jpeg')
#grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#region = faceDetection(grey)
#cv.imshow('img',region)
#cv.waitKey(0)
#cv.destroyAllWindows()
