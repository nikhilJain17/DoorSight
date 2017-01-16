# -*- coding: utf-8 -*-
from sklearn.decomposition import RandomizedPCA	# part of scipy
from picamera.array import PiRGBArray
from picamera import PiCamera
import scipy.misc
import numpy as np
import glob
import cv2
import math
import os.path
import string
import PIL
import time
import uuid
from PIL import Image # pip install Pillow


def main():
        # import the cascades
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        # load the webcam feed
        #capture = cv2.VideoCapture(0)
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640,480))

        # counter for picture
        counter = 0

        time.sleep(0.1)

        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                img = frame.array
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #print capture
                faces = face_cascade.detectMultiScale(img, 1.3, 5)  # array with found faces

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
                #        roi_color = img[y:y+h, x:x+h]

                        # only show the face box (row, column of img numpy array to be displayed)
                        img = roi_gray
                        img = cv2.equalizeHist(img)

                # resize the camera feed
                cv2.imshow('mode 2', img)
                rawCapture.seek(0)
		rawCapture.truncate()
        # 	# resize the camera feed
        # 	cv2.namedWindow('Do not read', cv2.WINDOW_NORMAL)
        #	cv2.imshow('Do not read', img)
                

                # to save img to file with esc key
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                        unique_filename = uuid.uuid4()
                        unique_filename = str(unique_filename)
                        print "Saving file " +  unique_filename
                        im = Image.fromarray(img)
                        im = im.resize((92,112), PIL.Image.ANTIALIAS)
                        filename = 'Picture ' + str(counter) + '.jpeg'
                        im.save('test_faces/' + filename)
                        counter += 1

                if k == 108: # l
			camera.close()
                        cv2.destroyAllWindows()
                        return

