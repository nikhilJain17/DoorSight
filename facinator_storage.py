# -*- coding: utf-8 -*-
from sklearn.decomposition import RandomizedPCA	# part of scipy
import scipy.misc
import numpy as np
import glob
import cv2
import math
import os.path
import string
import time
import PIL
from PIL import Image # pip install Pillow
import uuid # for unique filenames

time.sleep(0.1)
print 'starting'

# import the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# load the webcam feed
capture = cv2.VideoCapture(0)

ret, img = capture.read()

cv2.imshow('Walk', img)

while True:

	# quit when counter reaches 12
	x = 0

	ret, img = capture.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # array with found faces

	for (x, y, w, h) in faces:
		# draw rectangles
		# img = where to draw
		# next 2 args are start and end points of rectangle
		# next arg is color 
		# final arg is line width
		cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
		cv2.putText(img, 'Face', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1, cv2.CV_AA)
 
		# region of img, dont want to find eyes outside face
		roi_gray = gray[y:y+h, x:x+h]
		roi_color = img[y:y+h, x:x+h]

		# only show the face box (row, column of img numpy array to be displayed)
		img = roi_gray
		img = cv2.equalizeHist(img)


	# resize the camera feed
	cv2.namedWindow('No Patent Intended', cv2.WINDOW_AUTOSIZE)
	cv2.imshow('Patent Pending', img)

	unique_filename = uuid.uuid4()
	unique_filename = str(unique_filename)
	# unique_filename = 'subject'
	print "Saving file " #+  unique_filename
	im = Image.fromarray(img)
	#     6 fgbg = cv2.createBackgroundSubtractorMOG()
	# im = backgroundSubtractor.apply(im)

	im = im.resize((92,112), PIL.Image.ANTIALIAS)
	filename = 'subject.' + str(x) + '.jpeg' 
	im.save('test_faces/' + filename)

	x = x + 1


capture.release()
cv2.destroyAllWindows()

