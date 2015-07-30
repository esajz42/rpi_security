from flask import Flask, render_template, request
from flask_auth import requires_auth

import os
import signal
import pickle
import datetime
import threading
import multiprocessing
import subprocess
import picamera
from time import sleep

from messaging.Email import Email
from SecurityCamera import SecurityCamera

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

    if request.form['submit'] == 'Start Camera':
        print 'starting camera'
        try:
            killer = subprocess.Popen('./kill_camera.sh')
            sleep(1)
            killer.terminate()
            subprocess.Popen('python run_camera.py'.split())
        except UnboundLocalError:
            subprocess.Popen('python run_camera.py'.split())
        return 'camera enabled'

    if request.form['submit'] == 'Stop Camera':
        print 'stoping camera'
        try:
            killer.terminate()
            subprocess.Popen('./kill_camera.sh')
        except UnboundLocalError:
            killer = subprocess.Popen('./kill_camera.sh')
            sleep(1)
            killer.terminate()
        return 'Camera disabled'


if __name__ == "__main__":
    app.run(host='192.168.0.16', port=8080, debug=True)
