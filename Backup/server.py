import os

def start_server():
	print "Starting Server"
	if os.name == "nt":
		os.system("C:/xampp/xampp_start.exe")
	else:
		os.system("sudo /opt/lampp/xampp start")
		os.system("sleep 2")

def stop_server():
	print "Stoping Server"
	if os.name == "nt":
		os.system("C:/xampp/xampp_stop.exe")
	else:
		os.system("sudo /opt/lampp/xampp stop")

def get_login_info():
	return ["127.0.0.1", "root", "root", "customs"]
	return ["sql6.freemysqlhosting.net", "sql6146734", "L6i7NAjPr4", "sql6146734"]