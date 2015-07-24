#!/usr/bin/env python

import os
import picamera
import numpy as np
from scipy.misc import imread
from time import sleep, strftime


class SecurityCamera(object):
    """ Main class for monitoring for change between still images.
    """

    def __init__(self, fps=1, change_threshold=5, messager_list=None, uploader_list=None):
        """ Initializes an instance of SecurityCamera.
        """
        self.camera = picamera.PiCamera()
        self.fps = fps
        self.messager_list = messager_list
        self.record = False

    def start_camera():
        self.record = True
        while self.record:
            im_name = strftime("%Y%m%d%H%M%S") + "_rpi_security.jpg"
            camera.capture(im_name)
            new_image = imread(im_name)
            if not hasattr(self, 'ref_image'):
                self.ref_image =  new_image
                self.start_camera()
            elif hasattr(self, 'cur_image'):
                self.ref_image = self.cur_image
                self.cur_image = new_image
            
            if self.change_monitor():
                self.messager()

            sleep(1.0 / self.fps)

    def stop_camera():
        self.record = False

    def change_monitor():
        """ Method that monitors still frames for change.
        """
        ref_im_total = np.sum(ref_im) 
        cur_im_total = np.sum(cur_im)
        diff_percent = np.abs(ref_im_total - curr_im_total) / ref_im_total
        if diff_percent >= self.change_threshold:
            return True
        else
            return False

    def message():
        """ Sends emails, mms, or sms messages by looping over messager 
        objects in messager list. 
        """
        for messager in self.messager_list()
           messager.send()

    def upload():
        """ Uploads imagery to cloud repositories.
        """
        for uploader in uploader_list():
            uploader.send()
