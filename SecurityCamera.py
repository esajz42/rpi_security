#!/usr/bin/env python

import os
import picamera
import numpy as np
import subprocess
from scipy.misc import imread
from time import sleep, strftime
from file_monitor.file_monitor import remove_files


class SecurityCamera(object):
    """ Main class for monitoring for change between still images.
    """

    def __init__(self, fps=1, change_threshold=5, messager_list=[]):
 
        """ Initializes an instance of SecurityCamera.
        """
        self.camera = self.create_camera(delay=0)
        self.fps = fps
        self.change_threshold = change_threshold
        self.messager_list = messager_list
        self.record = False
    
    def create_camera(self, delay=0):
        try:
            print "Attempting to start camera in " + str(delay) + " seconds."
            sleep(delay)
            return picamera.PiCamera()
        except PiCameraMMALError:
            print "There was an error trying to start the camera..."
            self.create_camera(delay=10)

    def start_camera(self):
        print "Starting camera motion decection."
        self.record = True
        while self.record:
            self.im_name = strftime("%Y%m%d%H%M%S") + "_rpi_security.jpg"
            self.camera.capture(self.im_name)
            new_image = imread(self.im_name)

            if not hasattr(self, 'ref_image'):
                self.ref_image =  new_image
                self.start_camera()

            if not hasattr(self, 'cur_image'):
                self.cur_image = new_image
            
            if self.change_monitor():
                print 'trigger'
                self.message()
                #self.upload() # slow to send to dropbox...

            sleep(1.0 / self.fps)
            
            self.ref_image = self.cur_image
            delattr(self, "cur_image")

            # Remove old images
            remove_files(os.getcwd(), '.jpg', number_to_keep=10)

    def stop_camera(self):
        self.record = False

    def change_monitor(self):
        """ Method that monitors still frames for change.
        """
        ref_im_total = np.float(np.sum(self.ref_image))
        cur_im_total = np.float(np.sum(self.cur_image))
        diff_percent = (ref_im_total - cur_im_total) / ref_im_total * 100.0

        if diff_percent >= self.change_threshold:
            return True
        else:
            return False

    def message(self):
        """ Sends emails, mms, or sms messages by looping over messager 
        objects in messager list. 
        """
        for messager in self.messager_list:
            try:
                messager.send(self.im_name)
            except ValueError:
                continue

    def upload(self):
        """ Uploads imagery to cloud repositories.
        """
        try:
            fname = os.path.join(os.getcwd(), self.im_name)
            subprocess.call(["dropbox_uploader.sh", "upload", fname, "/"])
        except:
            return
