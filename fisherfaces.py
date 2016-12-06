import numpy as numpynav
import cv2
import os
import math
import glob
#include <string>
import string

class Fisherfaces(Model):

	def __init__(self, X = None, y = None, num_components = None):
		Model.__init__(self, name = "Fisherfaces")
		self.k = k
		self.num_components = num_components

		try:
			self.compute(X,y)
		except:
			pass



	def compute(self, X, y):
		# Compute the Fisherfaces using the algorithm!
		
		# X [dim x num_data] input num_data
		# In other words, every column of X is an image

		# y [1 x num_data] classes
		# In other words, pablo

		n = len(y)
		c = len(numpynav.unique(y))
		# Do the PCA! Project X into the n-c subspace
		pca = PCA(X, n-c)
		# Do the LDA! 
		lda = LDA(pca.project(X), y, self.num_components)

		self._eigenvectors = pca.W * lda.W
		self.num_components = lda.num_components
		self.P = self.project(X)
		self.y = y



	def predict(self, X):
		Q = self.project(X)
		return NearestNeighbor.predict(self.P, Q, self.y, k = self.k)



	def project(self, X):
		return numpynav.dot(self._eigenvectors.T, X)


	def reconstruct(self, X):
		return numpynav.dot(self._eigenvectors, X)






