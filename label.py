import MySQLdb
from datetime import datetime
from server import *
from search import Search

def dummy_spacer(word):
	x = len(str(word))
	y = " "*(20-x)
	return y

def label():
	lab = open("label.txt", "w")
	text = "\t\t\t\t\tCustoms Management\n\t\t\t\t\t  Project Amigo\n\nLabels Generated on \t\t\t\t\t\t: %.19s"%(datetime.now())
	lab.write(text)
	try:
		db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	except:
		start_server()
		db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	cursor=db.cursor()
	cursor.execute("SELECT manifest_id FROM manifest")
	manifest=cursor.fetchall()
	db.close()
	lab.write("\n-----------------------------------------------------------------------------------")
	i = 1
	for man in manifest:
		manifest_id= man[0]
		result = Search(manifest_id)
		[manifest_id, description, carrier_name, issuer_name, transport_description, bol_id, date, country, bill_amount, from_port_name, to_port_name, remarks] = result

		answer = "\n\nMANIFEST \t\t\t: %0.4d"%(manifest_id) + "\t\t\t|"
		answer = answer + "\nCARRIED BY \t\t\t: %s"%(carrier_name) + dummy_spacer(carrier_name) + "\t| Recepient Signature"
		answer = answer + "\nBill Number \t\t: %0.4d"%(bol_id) + "\t\t\t|" 
		answer = answer + "\nDate \t\t\t\t: %s"%(date) + "\t\t| Contact Number : "
		answer = answer + "\nCountry \t\t\t: %s"%(country) + dummy_spacer(country) + "\t|"
		answer = answer + "\nBill amount \t\t: INR %7.2f"%(bill_amount) + dummy_spacer("inr %7.2f"%(bill_amount))  + "\t| Customs Officer Signature"
		answer = answer + "\nFrom Port \t\t\t: %s"%(from_port_name) + dummy_spacer(from_port_name) + "\t|"
		answer = answer + "\nTo Port \t\t\t: %s"%(to_port_name) + dummy_spacer(to_port_name) + "\t| Seal- CBEC, India"

		lab.write(answer)
		if i % 5 != 0:
			lab.write("\n\n--------------------------------- -X Tear Here X- ---------------------------------")
		else:
			lab.write("\n\n-----------------------------------------------------------------------------------")
		if i > 5 and i % 5 == 0:
			lab.write("\n\n\n\n")
		i = i+1
	print "Labels Printed @ %.19s"%(datetime.now())    
	lab.close()