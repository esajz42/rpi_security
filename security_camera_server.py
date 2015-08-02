#!/usr/bin/env python

from flask import Flask, render_template, request
from flask_auth import requires_auth

import datetime
import pickle
import subprocess
import sys
import psutil

from messaging.Email import Email
from motion_monitor import MotionMonitor

messager_info = pickle.load(open("../rpi_security_tests/messager_info.pickle", "rb"))
messager_list = [Email(messager_info[0], messager_info[1], messager_info[2][0], messager_info[3])]

app = Flask(__name__)

@app.route("/")
@requires_auth
def camera_home():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
                    'title' : 'Raspberry Pi Security',
                    'time': timeString
                   }

    return render_template('camera_home.html', **templateData)

@app.route("/control", methods=['POST'])
@requires_auth
def camera_control():
    
    if request.form['motion'] == 'Start Motion Detection':
        print 'starting motion detection'
        try:
            monitor.join()
            del monitor
        except NameError:
            monitor = MotionMonitor(messager_list=messager_list)
            monitor.daemon = True
            monitor.start()
        return 'looking for motion'

    if request.form['motion'] == 'Stop Everything':
       subprocess.Popen('./kill_server.sh', shell=True)

if __name__ == "__main__":
    app.run(host='192.168.0.16', port=8080, debug=False, threaded=False)
