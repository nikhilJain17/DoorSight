# -*- coding: utf-8 -*-
from sklearn.decomposition import RandomizedPCA
import numpy as np
import glob
import cv2
import math
import os.path
import string

#function to get ID from filename
def ID_from_filename(filename):
    part = string.split(filename, '/')
    return part[1].replace("s", "")
 
#function to convert image to right format
def prepare_image(filename):
    img_color = cv2.imread(filename)
    img_gray = cv2.cvtColor(img_color, cv2.cv.CV_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    return img_gray.flat

IMG_RES = 92 * 112 # img resolution
NUM_EIGENFACES = 10 # images per train person
NUM_TRAINIMAGES = 110 # total images in training set

#loading training set from folder train_faces
folders = glob.glob('train_faces/*')
 
# Create an array with flattened images X
# and an array with ID of the people on each image y
X = np.zeros([NUM_TRAINIMAGES, IMG_RES], dtype='int8')
y = []

# Populate training array with flattened imags from subfolders of train_faces and names
c = 0
for x, folder in enumerate(folders):
    train_faces = glob.glob(folder + '/*')
    for i, face in enumerate(train_faces):
        X[c,:] = prepare_image(face)
        y.append(ID_from_filename(face))
        c = c + 1

# perform principal component analysis on the images
pca = RandomizedPCA(n_components=NUM_EIGENFACES, whiten=True).fit(X)
X_pca = pca.transform(X)

# load test faces (usually one), located in folder test_faces
test_faces = glob.glob('test_faces/*')

# Create an array with flattened images X
X = np.zeros([len(test_faces), IMG_RES], dtype='int8')
 
# Populate test array with flattened imags from subfolders of train_faces 
for i, face in enumerate(test_faces):
    X[i,:] = prepare_image(face)
 
# run through test images (usually one)
for j, ref_pca in enumerate(pca.transform(X)):
    distances = []
    # Calculate euclidian distance from test image to each of the known images and save distances
    for i, test_pca in enumerate(X_pca):
        dist = math.sqrt(sum([diff**2 for diff in (ref_pca - test_pca)]))
        distances.append((dist, y[i]))
 
    found_ID = min(distances)[1]

    print "Identified (result: "+ str(found_ID) +" - dist - " + str(min(distances)[0])  + ")"








# # import the cascades
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# # load the webcam feed
# capture = cv2.VideoCapture(0)

# while True:
# 	ret, img = capture.read()
# 	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 	faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # array with found faces

# 	for (x, y, w, h) in faces:
# 		# draw rectangles
# 		# img = where to draw
# 		# next 2 args are start and end points of rectangle
# 		# next arg is color
# 		# final arg is line width
# 		cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
# 		cv2.putText(img, 'Patent Pending', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1, cv2.CV_AA)
 
# 		# region of img, dont want to find eyes outside face
# 		roi_gray = gray[y:y+h, x:x+h]
# 		roi_color = img[y:y+h, x:x+h]

# 		eyes = eye_cascade.detectMultiScale(roi_gray)

# 		for(ex, ey, ew, eh) in eyes:
# 			# draw the eye boxes
# 			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# 	# resize the camera feed
# 	cv2.namedWindow('No Patent Intended', cv2.WINDOW_NORMAL)
# 	cv2.imshow('Patent Pending', img)
# # 	# resize the camera feed
# # 	cv2.namedWindow('Do not read', cv2.WINDOW_NORMAL)
# # 	cv2.imshow('Do not read', img)

# 	# to break program with esc key
# 	k = cv2.waitKey(30) & 0xff
# 	if k == 27:
# 		break;

# capture.release()
# cv2.destroyAllWindows()

