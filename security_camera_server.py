from flask import Flask, render_template, request
from flask_auth import requires_auth

import pickle
import datetime
import subprocess

from SecurityCamera import SecurityCamera
from messaging import Email

app = Flask(__name__)

messager_info = pickle.load(open('../rpi_security_tests/messager_info.pickle', 'rb'))
mlist = [
        Email.Email(messager_info[0], messager_info[1], messager_info[2], messager_info[3])
        ]

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
        if 'cam_obj' in locals():
            cam_obj.start_camera()
            return 'Camera enabled'
        else:
            cam_obj = SecurityCamera(fps=10, change_threshold=2, messager_list=mlist)
            cam_obj.start_camera()
            return 'Camera enabled'
        #return 'Camera enabled'

    if request.form['submit'] == 'Stop Camera':
        print 'stoping camera'
        try:
            #cam_obj.stop_camera()
            del cam_obj
            return 'Camera disabled'
        except NameError:
            pass
            return 'Camera disabled'
        #return 'Camera disabled'

if __name__ == "__main__":
    app.run(host='192.168.0.16', port=8080, debug=True)
