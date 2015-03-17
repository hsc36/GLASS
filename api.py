# Security Server API
import sys
import json
import ast
import dbfunctions as dbf
from flask import Flask, request, Response, render_template

###--- Setup ---###
# Read in Configurations
login_page = 'login.html'
swipe_id_page = 'swipe_id.html'
access_denied_page = 'access_denied.html'
access_page = 'access.html'
error_page = 'error.html'

# Construct the Flask API
api = Flask(__name__)

# Default - Homepage/Login 
@api.route("/")
def default_func():
	return render_template(login_page)

# Username Authentication
@api.route("/auth", methods=['POST'])
def auth_func():
	if request.method == 'POST':
		verified = dbf.verify_user(request.form['user'], request.form['pass'])
		return render_template(swipe_id_page) if verified else render_template(access_denied_page)
	else:
		return render_template(error_page)

# RFID & Location Authentication
@api.route("/id", methods=['POST'])
def id_func():
	if request.method == 'GET':
		verified = request.data
		return render_template(access_page) if verified else render_template(access_denied_page)
	elif request.method == 'POST':
		verified = dbf.verify_id_locat(request.form['rfid'], request.form['gps'])
		return render_template(swipe_id_page) if verified else render_template(access_denied_page)
	else:
		return render_template(error_page)

# Run the API
if __name__ == "__main__":
	api.run(debug=True)