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

#to test our code
#img = cv.imread('./affan.jpeg')
#grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#region = faceDetection(grey)
#cv.imshow('img',region)
#cv.waitKey(0)
#cv.destroyAllWindows()