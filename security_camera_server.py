from flask import Flask, render_template, request
from flask_auth import requires_auth

import datetime
import subprocess

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
            stop(process_obj)
            process_obj = create_process()
        except NameError:
            process_obj = create_process()
        return 'Camera enabled'

    if request.form['submit'] == 'Stop Camera':
        print 'stoping camera'
        try:
            process_obj.kill()
        except NameError:
            pass
        return 'Camera disabled'

def create_process():
    return subprocess.Popen('./run_camera.sh', shell=True)

if __name__ == "__main__":
    app.run(host='192.168.0.16', port=8080, debug=True)
