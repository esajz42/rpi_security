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
from image_watcher import ImageWatcher

messager_info = pickle.load(open("../rpi_security_tests/messager_info.pickle", "rb"))
messager_list = [
        Email(messager_info[0], messager_info[1], messager_info[2][0], messager_info[3])
        ]

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
            watcher.join()
            del watcher
        except NameError:
            monitor = MotionMonitor()
            monitor.daemon = True
            monitor.start()
            watcher = ImageWatcher(messager_list=messager_list)
            watcher.daemon = True
            watcher.start()
        return 'looking for motion'

    if request.form['motion'] == 'Stop Motion Detection':
        #watcher.join()
        #monitor.join()
        #pid = os.getpid()
        #os.kill(pid, signal.SIGQUIT) #or signal.SIGKILL
        #raise KeyboardInterrupt
        #sys.exit()
        subprocess.Popen('./kill_server.sh', shell=True)
        #print 'stopping motion detection'
        #try:
            #monitor.join()
            #del monitor
            #watcher.join()
            #del watcher
        #except NameError:
            #pass
        #return 'stopped motion detection'

#    if request.form['motion'] == 'Start Alerts':
#        print 'starting alerts'
#        try:
#            watcher.join()
#            del watcher
#        except NameError:
#            watcher = ImageWatcher(messager_list=messager_list)
#            watcher.start()
#        return 'started alerts'
#
#    if request.form['motion'] == 'Stop Alerts':
#        print 'stoping alerts'
#        try:
#            watcher.join()
#            del watcher
#        except NameError:
#            pass
#        return 'stopped alerts'

if __name__ == "__main__":
    app.run(host='192.168.0.16', port=8080, debug=False, threaded=False)
