#!/usr/bin/env python

import picamera
import numpy as np
from time import sleep


class SecurityCamera(object):
    """ Main class for monitoring for change between still images.
    """

    def __init__(self, fp1=1, messager_list=None,):
        """ Initializes an instance of ChangeDetection.
        """
        self.camera = picamera.PiCamera()

    def change_monitor():
        """ Method that monitors still frames for change.
        """
        pass

    def message():
        """ Sends emails, mms, or sms messages by looping over messager 
        objects in messager list. 
        """
        pass

    def upload():
        pass
