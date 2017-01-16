import cv2
import numpy as np
import uuid
import PIL
from PIL import Image

# to capture images and save them
def save_img(img, subject_name):
	unique_filename = uuid.uuid4()
	unique_filename = str(unique_filename)
	# unique_filename = 'subject'
	print "Saving file " +  unique_filename
	im = Image.fromarray(img)
	#     6 fgbg = cv2.createBackgroundSubtractorMOG()
	# im = backgroundSubtractor.apply(im)

	im = im.resize((92,112), PIL.Image.ANTIALIAS)
	filename = subjectname + '.jpeg' 
	im.save('test_faces/' + filename)  

def main(subject_name):
	# import the cascades
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

	# load the webcam feed
	capture = cv2.VideoCapture(0)

	while True:
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

			# region of img, dont want to find eyes outside face
			roi_gray = gray[y:y+h, x:x+h]
			roi_color = img[y:y+h, x:x+h]

			img = roi_gray
			img = cv2.equalizeHist(img)

		cv2.imshow('img', img)

		# to break program with esc key
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			save_img(img)
