#!/usr/bin/env python

import picamera
from time import sleep

class SecurityCamera(object):
    """ Main class for monitoring for change between still images.
    """

    def __init__(self):
        """ Initializes an instance of ChangeDetection.
        """
        self.camera = picamera.PiCamera()
