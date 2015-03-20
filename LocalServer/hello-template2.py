from flask import Flask, render_template
import datetime
import getValidation as gv
import requests


app = Flask(__name__)
global json_data

@app.route("/")
def hello():
	#json_data = gv.get_validation_data(gv.setup_serial())
	json_data = {'id':'abc123', 'gps':{'lat':123.45, 'lng':678.911}}
	now = datetime.datetime.now()
	req = requests.post("http://192.168.2.2/id", data=json_data)
	print json_data
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {'title' : 'GPS SERVER!','time': timeString}
	return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='192.168.2.2', port=8000, debug=True)