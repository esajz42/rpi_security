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

#    if request.method == 'POST':
#
#        if request.form['submit'] == 'Start Camera':
#            print 'starting camera'
#            subprocess.call(['raspistill', '-o', '/home/pi/Documents/rpi_security/play_scripts/omg_the_call_worked.jpg'])
#
 #       if request.form['submit'] == 'Stop Camera':
 #           print 'stoping camera'

    return render_template('camera_home.html', **templateData)


@app.route("/control", methods=['POST'])
@requires_auth
def camera_control():

    if request.form['submit'] == 'Start Camera':
        print 'starting camera'
        return 'Camera enabled'

    if request.form['submit'] == 'Stop Camera':
        print 'stoping camera'
        return 'Camera disabled'

#    return render_template('camera_control.html')

if __name__ == "__main__":
    app.run(host='192.168.0.16', port=8080, debug=True)
