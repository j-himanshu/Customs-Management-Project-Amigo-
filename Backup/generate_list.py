import MySQLdb
from server import *

try:
	db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
except:
	start_server()
	db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")

def generate_issuer_list():
	issuer_list={}
	db = MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	try:
		cursor = db.cursor()
		cursor.execute("SELECT issuer_name, issuer_id FROM manifest_issuer")
		result = cursor.fetchall()
		for res in result:
			issuer_list[str(res[0])] = int(res[1])
	except:
		pass
	return issuer_list

def generate_port_list():
	port_list={}
	db=MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	try:
		cursor = db.cursor()
		cursor.execute("SELECT port_name, port_id FROM port")
		result = cursor.fetchall()
		for res in result:
			port_list[str(res[0])] = int(res[1])
	except:
		pass
	return port_list


def generate_mode_list():
	mode_list = {}
	db=MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	try:
		cursor = db.cursor()
		cursor.execute("SELECT description, mode_id FROM mode_of_transport")
		result = cursor.fetchall()
		for res in result:
			mode_list[str(res[0])] = int(res[1])
	except:
		pass
	return mode_list

def generate_carrier_list():
	carrier_list = {}
	db=MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	try:
		cursor = db.cursor()
		cursor.execute("SELECT carrier_name, carrier_id FROM carrier")
		result = cursor.fetchall()
		for res in result:
			carrier_list[str(res[0])] = int(res[1])
	except:
		pass
	return carrier_list

def generate_product_list():
	product_list = {}
	db=MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	try:
		cursor = db.cursor()
		cursor.execute("SELECT description, id FROM product")
		result = cursor.fetchall()
		for res in result:
			product_list[str(res[0])] = int(res[1])
	except:
		pass
	return product_list

def generate_country_list():
	country_list = {}
	db=MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	try:
		cursor = db.cursor()
		cursor.execute("SELECT name, country_code FROM country")
		result = cursor.fetchall()
		for res in result:
			country_list[str(res[0])] = int(res[1])
	except:
		pass
	return country_list

def generate_company_list():
	company_list = {}
	db=MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	try:
		cursor = db.cursor()
		cursor.execute("SELECT name, id FROM company")
		result = cursor.fetchall()
		for res in result:
			company_list[str(res[0])] = int(res[1])
	except:
		pass
	return company_list

def generate_user_list():
	user_list = {}
	db=MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	try:
		cursor = db.cursor()
		cursor.execute("SELECT username FROM admin")
		result = cursor.fetchall()
		for res in result:
			user_list[str(res[0])] = -1
	except:
		pass
	return user_list