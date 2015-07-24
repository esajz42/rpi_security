#!/usr/bin/env python

import os
import subprocess

"""Dropbox.py

Class that can upload files to  Dropbox.
"""

class Dropbox(object):
    """Main class for uploading data to Dropbox.
    """

    def __init__(self):
        """Initializes an instance of Uploader.
        """
        pass
        
    def send(self, local_file):
        subprocess.call(["dropbox_uploader.sh", "upload", local_file, "/"])
