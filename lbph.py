import numpy as numpynav
import cv2
import math
import glob
#include <string>
import string

labels = []
# images = []
folders = glob.glob('train_faces/*')

def ID_from_filename(filename):
    part = string.split(filename, '/')
    return part[1].replace("s", "")


def get_images_and_labels():
	global images
	images = []
	for x, folder in enumerate(folders):
		temp_images = glob.glob(folder + '/*')
		images = temp_images + images
		for i, face in enumerate(temp_images):
			labels.append(ID_from_filename(face))


get_images_and_labels()

print images

#lbph 
# recognizer = cv2.createLBPHFaceRecognizer()

# Perform the tranining
# recognizer.train(images, np.array(labels))
