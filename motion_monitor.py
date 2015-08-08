#!/usr/bin/env python

import io
import os
import cv2
import time
import copy
import picamera
import multiprocessing
from scipy.misc import imsave
import numpy as np
import pickle

from Email import Email

from timeout import timeout, TimeoutError

class MotionMonitor(multiprocessing.Process):
    """ Class that watches a video stream for motion and will save image files if
    motion is detected.
    """

    def __init__(self, name="MotionMonitor", messager_list=[]):
        #self._stopevent = threading.Event( )
        self._sleepperiod = 1.0
        self.messager_list = messager_list
        multiprocessing.Process.__init__(self, name=name)
        self.daemon = True

    def run(self):

        # Configure raspberry pi camera collection settings
        #camera = cv2.VideoCapture(0)
        camera = picamera.PiCamera()
        camera.framerate = 32

        time.sleep(0.25)

        # Loop until stop method is called
        #while not self._stopevent.isSet():
        while True:

            text = "Unoccupied"

            # Grab a frame from stream
            stream = io.BytesIO()
            camera.capture(stream, format="jpeg")
            data = np.fromstring(stream.getvalue(), dtype=np.uint8)
            image = cv2.imdecode(data, 1)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Convert frame to grayscale and blur
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            frame = cv2.GaussianBlur(frame, (21, 21), 0)
           
           # Compute difference between current frame and reference frame
            try:
                frame_delta = cv2.absdiff(ref_frame, frame)
            except NameError:
                ref_frame = copy.deepcopy(frame)
                
                frame_delta = cv2.absdiff(ref_frame, frame)

            # Threshold image, morpholgical dilate, and extract contours
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            print 'Number of contours found: ' + str(len(cnts))

            # Flag contours as motion if over area threshold (in pixels)
            for c in cnts:

                print 'Contour area: ' + str(cv2.contourArea(c))
                if cv2.contourArea(c) < 5000:
                    continue

                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Occupied"

                cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) 
            
                # Save image locally if threshold criteria is met
                im_name = time.strftime("%Y%m%d%H%M%S") + "_rpi_security.jpg"
                imsave(im_name, image)
                #imsave(time.strftime("%Y%m%d%H%M%S") + "_thresh_image.jpg", frame)
                # Email image
                for messager in self.messager_list:
                    #try:
                        #messager.send(im_name)
                    timeout(messager.send, args=[im_name], timeout_duration=10)
                    #except TimeoutError:
                        #continue
                os.remove(im_name)

            # Update reference image 
            ref_frame = frame
            
            print 'looped'

    #def join(self, timeout=1):
        #self._stopevent.set( )
        #threading.Thread.join(self, timeout)


if __name__ == "__main__":
    motion_obj = MotionMonitor()
    motion_obj.start() 
    time.sleep(10.0)
    motion_obj.join(1)
