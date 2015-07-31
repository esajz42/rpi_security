#!/usr/bin/env python

from messaging import Email
from file_monitor.file_monitor import remove_files

import os
import picamera
from time import sleep, strftime
from scipy.misc import imread
import numpy as np
import pickle

messager_info = pickle.load(open('../rpi_security_tests/messager_info.pickle', 'rb'))

mlist = [
        Email.Email(messager_info[0], messager_info[1], messager_info[2][0], messager_info[3]),
Email.Email(messager_info[0], messager_info[1], messager_info[2][1], messager_info[3])
        ]

camera = picamera.PiCamera()

change_threshold
fps = 100



while True:

    print 'loopin!'

    im_name = strftime("%Y%m%d%H%M%S") + "_rpi_security.jpg"
    camera.capture(im_name)
    new_image = imread(im_name)

    if 'reference_image' not in locals():
        reference_image = new_image
        sleep(1.0 / fps)
        continue
    else:
        cur_image = new_image

    ref_total = np.float(np.sum(reference_image))
    cur_total = np.float(np.sum(cur_image))
    diff_percent = np.abs((ref_total - cur_total)) / ref_total * 100.0

    print 'diff percent: ' + str(diff_percent) + '%'

    if diff_percent >= change_threshold:
        print 'triggered!'
        for messager in mlist:
            messager.send(im_name)

    remove_files(os.getcwd(), '.jpg', number_to_keep=10)

    reference_image = cur_image
    del cur_image

    sleep(1.0 / fps)
