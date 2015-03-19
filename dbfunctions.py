import sys
import json
import ast
from sys import argv
import dbfunctions as dbf
from flask import Flask, request, Response, render_template, url_for
import MySQLdb as mdb
# Security Server DB Access Functions
def getUserInfo(username,password):
	print 'Retrieving Authroized User Acess Information'
	con = mdb.connect('localhost', 'admin', 'glassadmin', 'glass');
	del userInfo[:]
	with con:
		cur = con.cursor()
		cur.execute("SELECT ID_Num FROM LoginInfo WHERE Username = %s AND Password = %s" ,(username,password))
		row = cur.fetchone()
		id_num = row[0]
		cur.execute("SELECT * FROM AccessInfo WHERE ID_Num = %s" ,(id_num))
		row = cur.fetchone()
		access_type = row[1]
		cur.execute("SELECT * FROM AccessType WHERE Access_Type = %s" ,(access_type))
		row = cur.fetchone()
		access_desc = row[2]
		cur.execute("SELECT * FROM UserInfo WHERE ID_Num = %s" ,(id_num))
		row = cur.fetchone()
		first_name = row[1]
		last_name = row[2]
		userInfo.append(str(id_num))
		userInfo.append(first_name)
		userInfo.append(last_name)
		userInfo.append(access_desc)
		return userInfo

def verifyUser(username, password):
	username_check = []
	password_check = []
	userInfo = []
	authorize = False
	userOn = 0
	passOn = 0
	i = 0
	print "Verifying user %s" % username
	con = mdb.connect('localhost', 'admin', 'glassadmin', 'glass');
	with con:
		cur = con.cursor()
		cur.execute("SELECT Username, Password FROM LoginInfo")
		for i in range(cur.rowcount):
			row = cur.fetchone()
			username_check.append(row[0])
			password_check.append(row[1])
		i = 0
		while (i < len(username_check)):
			if(username_check[i] == username):
				userOn = 1
			i+=1
		i = 0
		while (i < len(password_check)):
			if(password_check[i] == password):
				passOn = 1
			i+=1
		if (userOn == 1 and passOn == 1):
			print "Successful Username and Password entry!!"
			authorize = True
		elif (userOn == 1 and passOn == 0):
			print "Incorrect Password"
			authorize = False
		elif (userOn == 0 and passOn == 0):
			print "Incorrect Username and Password"
			authorize = False
	return authorize


def verify_user(user, pasw):
	username_check = []
	password_check = []
	userInfo = []
	authorize = False
	userOn = 0
	passOn = 0
	i = 0
	print "Verifying user %s" % username
	con = mdb.connect('localhost', 'admin', 'glassadmin', 'glass');
	with con:
		cur = con.cursor()
		cur.execute("SELECT Username, Password FROM LoginInfo")
		for i in range(cur.rowcount):
			row = cur.fetchone()
			username_check.append(row[0])
			password_check.append(row[1])
		i = 0
		while (i < len(username_check)):
			if(username_check[i] == username):
				userOn = 1
			i+=1
		i = 0
		while (i < len(password_check)):
			if(password_check[i] == password):
				passOn = 1
			i+=1
		if (userOn == 1 and passOn == 1):
			print "Successful Username and Password entry!!"
			authorize = True
		elif (userOn == 1 and passOn == 0):
			print "Incorrect Password"
			authorize = False
		elif (userOn == 0 and passOn == 0):
			print "Incorrect Username and Password"
			authorize = False
	return authorize

def verify_id_locat(rfid, gps):
	# Check the Database for Verification
	#if Checks Out
	#	return True
	#else
	return False