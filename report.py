import MySQLdb
import csv
from datetime import datetime
from search import Search
from server import start_server

def report():
    rep = open("report.csv", "wb")
    text = [["\t\t\tCustoms Management Database Management System"], [ "\t\t\t                             Project Amigo"], [ "\tReports Generated on:"], ["\t%0.19s"%(datetime.now())],[""],["MANIFEST#","PRODUCT","CARRIED BY","ISSUED BY","MODE","BILL#","DATE","COUNTRY","BILL AMOUNT","FROM PORT","TO PORT","REMARKS"]]
    writer = csv.writer(rep, delimiter = ',')
    for each_line in text:
        writer.writerow(each_line)
    try:
    	db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    except:
    	start_server()
    	db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    cursor=db.cursor()
    cursor.execute("SELECT manifest_id FROM manifest")
    manifest=cursor.fetchall()
    db.close()
    for man in manifest:
        manifest_id= man[0]
        result = Search(manifest_id)
        [manifest_id, description, carrier_name, issuer_name, transport_description, bol_id, date, country, bill_amount, from_port_name, to_port_name, remarks] = result
        answer = [manifest_id,description,carrier_name,issuer_name,transport_description,bol_id,date,country,"INR %0.2f"%(bill_amount),from_port_name,to_port_name,remarks]
        writer.writerow(answer)

    print "Report Generated @ %.19s"%(datetime.now())       
    rep.close()
#report()