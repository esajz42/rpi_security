#!/usr/bin/env python

import pickle

from SecurityCamera import SecurityCamera
from messaging import Email

messager_info = pickle.load(open('../rpi_security_tests/messager_info.pickle', 'rb'))

mlist = [
        Email.Email(messager_info[0], messager_info[1], messager_info[2], messager_info[3])
        ]

cam_obj = SecurityCamera(fps=10, change_threshold=2, messager_list=mlist)
cam_obj.start_camera()
