#!/usr/bin/env python

import io
import os
import cv2
import time
import copy
import picamera
from picamera.array import PiRGBArray   
import threading
from scipy.misc import imsave
import numpy as np

class MotionMonitor(threading.Thread):
    """ Class that watches a video stream for motion and will save image files if
    motion is detected.
    """

    def __init__(self, name="MotionMonitor"):
        self._stopevent = threading.Event( )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)

    def run(self):

        # Configure raspberry pi camera collection settings
        #camera = cv2.VideoCapture(0)
        camera = picamera.PiCamera()
        camera.framerate = 32
        #camera.resolution = (1920, 1080)
        #stream = PiRGBArray(camera, size=(1920, 1080))
        #stream = PiRGBArray(camera)

        time.sleep(0.25)

        # Loop until stop method is called
        stream = io.BytesIO()
        while not self._stopevent.isSet():

            text = "Unoccupied"

            # Grab a frame from stream
            #camera.capture(stream, format="bgr")
            #image = stream.array
            camera.capture(stream, format="jpeg")
            data = np.fromstring(stream.getvalue(), dtype=np.uint8)
            image = cv2.imdecode(data, 1)
            
            # Convert frame to grayscale and blur
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            frame = cv2.GaussianBlur(frame, (21, 21), 0)
           
           # Compute difference between current frame and reference frame
            try:
                frame_delta = cv2.absdiff(ref_frame, frame)
            except NameError:
                ref_frame = frame
                frame_delta = cv2.absdiff(ref_frame, frame)
            
            # Threshold image, morpholgical dilate, and extract contours
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            tresh = cv2.dilate(thresh, None, iterations=2)
            (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Flag contours as motion if over area threshold (in pixels)
            for c in cnts:

                if cv2.contourArea(c) < 50:
                    continue

                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Occupied"

            cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) 
            
            # Save image locally
            #cv2.imwrite(time.strftime("%Y%m%d%H%M%S") + "_rpi_security.jpg", image)
            imsave(time.strftime("%Y%m%d%H%M%S") + "_rpi_security.jpg", image)
            imsave(time.strftime("%Y%m%d%H%M%S") + "_thresh_image.jpg", frame)

            # Update reference image 
            ref_frame = frame
            
            #cv2.imshow("Image", image)
            #cv2.imshow("Threshold Image", frame)

            # Give chance to interupt
            self._stopevent.wait(self._sleepperiod)
            print 'looped'

    def join(self, timeout=None):
        self._stopevent.set( )
        threading.Thread.join(self, timeout)


if __name__ == "__main__":
    motion_obj = MotionMonitor()
    motion_obj.start( ) 
    time.sleep(6.0)
    motion_obj.join( )
