# Security Server API
import sys
import json
import ast
from sys import argv
import dbfunctions as dbf
from flask import Flask, request, Response, render_template, url_for
import MySQLdb as mdb

###--- Setup ---###
# Check if in Debug Mode
debug = True if argv[-1] == 'debug' else False
authorize = False
userInfo = []

# Set Pages
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
		username = request.form['user']
		password = request.form['pass']
		verified = dbf.verify_user(username, password)
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
	if debug:
		api.run(debug=True)
	else:
		api.run(host='0.0.0.0', port=80, debug=False)