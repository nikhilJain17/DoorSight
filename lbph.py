import numpy as numpynav
import cv2
import os
import math
import glob
#include <string>
import string
from PIL import Image
from sklearn.decomposition import RandomizedPCA


recognizer = cv2.createLBPHFaceRecognizer()

global images
global labels

# traverse all the folders, get all the images
# return an array of tuples with [img : 'label']
# ***NOTE*** facinator.py preprocesses the images for us (equalizeHistograms, etc) so we don't need to do it here
def collect_imageset(path):
	# root folder with all the other folders of imgs
	root = glob.glob('train_faces2/*')
	
	# arrays to be returned
	images = []
	labels = []

	image_paths = [os.path.join(path, f) for f in os.listdir(path)]# if not f.endswith('.sad')]
	
	# print image_paths

	for img in image_paths:
		# read the damn image
		pil_image = Image.open(img) # its in PIL format
		# pil_image = cv2.imread(img)
		image = numpynav.array(pil_image, 'uint8') # convert to numpy array, the gold standard
		images.append(image)


	print images


collect_imageset(os.getcwd() + '/train_faces2/')