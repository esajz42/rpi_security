#!/usr/bin/env python

import picamera
import numpy as np
from time import sleep, strftime


class SecurityCamera(object):
    """ Main class for monitoring for change between still images.
    """

    def __init__(self, fps=1, change_threshold=5, messager_list=None,):
        """ Initializes an instance of ChangeDetection.
        """
        self.camera = picamera.PiCamera()i
        self.fps = fps
        self.messager_list = messager_list
        self.record = False

    def start_camera():
        self.record = True
        while self.record:
            im_name = strftime("%Y%m%d%H%M%S") + "rpi_security.jpg"
            camera.capture(im_name)
            self.change_monitor()
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
            change = True
        else
            change = False
        return change

    def message():
        """ Sends emails, mms, or sms messages by looping over messager 
        objects in messager list. 
        """
        pass

    def upload():
        pass
