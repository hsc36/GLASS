from flask import Flask, render_template
import datetime
import getValidation as gv
import requests


app = Flask(__name__)
global json_data

@app.route("/")
def hello():
	json_data = gv.get_validation_data(gv.serial_setup())
	now = datetime.datetime.now()
	req = requests.post("192.168.2.2/id", data=json_data)
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='192.168.2.2', port=8000, debug=True)