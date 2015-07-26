from flask import Flask, render_template
from flask_auth import requires_auth
import datetime
app = Flask(__name__)

@app.route("/")
@requires_auth
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
                    'title' : 'HELLO!',
                    'time': timeString
                                       }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='192.168.0.16', port=8080, debug=True)
