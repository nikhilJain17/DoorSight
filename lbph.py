import numpy as numpynav
import cv2
import os
import math
import glob
#include <string>
import string

# labels = []
# images = []
folders = glob.glob('train_faces/*')

def ID_from_filename(filename):
    part = string.split(filename, '/')
    return part[1].replace("s", "")


def get_images_and_labels():
	global images, labels, nbr
	images = []
	labels = []
	nbr = -69
	for x, folder in enumerate(folders):
		temp_images = glob.glob(folder + '/*')
		images = temp_images + images
		for i, face in enumerate(temp_images):
			nbr = os.path.split(face)[1].split(".")[0]
	        labels.append(nbr)
			# labels.append(ID_from_filename(face))
	# redo labels to be a num array
	# like 1 2 3 etc

get_images_and_labels()


#lbph 
recognizer = cv2.createLBPHFaceRecognizer()

# Perform the tranining
recognizer.train(images, numpynav.array(labels))
