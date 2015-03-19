import serial
import json

def setup_serial(com='com3'):
	ser = serial.Serial(com_port, 9600, timeout=3)

def get_validation_data(ser):
	
	# Send Message to Microcontroller, to Get Data
	ser.write('getMyData')
	# Read the data from the serial as json
	msg = ser.readline().strip()
	if msg.startswith('GPGGA'):
		msg = msg.replace('GPPGA', '')
	# Parse the message into its associted data and store it in a dictionary
	lat_deg = float(msg[17:19])
	lat_min = float(msg[20:26])
	lng_deg = float(msg[29:32])
	lng_min = float(msg[32:39])
	lat_direc = msg[27]
	lng_direc = msg[40]
	# Convert the Minutes into Degrees and sume them
	lat = lat_deg + (lat_min / 60) + 0.833344 # Offset Value
	lng = lng_deg + (lng_min / 60)
	# Determine if the lattitude or longitude should be a negative value
	if lat_direc == 'S':
	 	lat = (lat * (-1))
	if lng_direc == 'W':
		lng = (lng * (-1))
	
	# Package GPS Data
	gps_data = {}
	gps_data['lat'] = lat
	gps_data['lng'] = lng
	
	# Convert Dictionaries to JSON
	data = {}
	data['gps'] = gps_data
	#data['id'] = id_data @TODO: Include on Arduino-end
	return json.dumps(data)