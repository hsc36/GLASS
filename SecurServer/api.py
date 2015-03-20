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
@api.route("/verify", methods=['POST'])
def ver_func():
	if request.method == 'POST':
		return render_template(access_page)

@api.route("/id", methods=['POST', 'GET'])
def id_func():
	if request.method == 'GET':
		print 'in funct'
		verified = request.data
		return render_template(access_page)# if verified else render_template(access_denied_page)
	if request.method == 'POST':
		print 'In post'
		#gps_data = json.dumps(ast.literal_eval(request.data))
		#verified = dbf.verify_id_locat('', gps_data)	#@TODO: Pass ACTUAL ID
		return render_template(access_page) #if verified else render_template(access_denied_page)
	print 'here in id'
	print 'befoe error'
	return render_template(error_page)

# Run the API
if __name__ == "__main__":
	if debug:
		api.run(debug=True)
	else:
		api.run(host='0.0.0.0', port=80, debug=False)