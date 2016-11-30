import MySQLdb
import os
from Tkinter import *

root = Tk()

try:

	try:
		fil = open("temp.txt", "r")
		text = fil.read().split("\n")
		select_what, table_name, where = text[0], text[1], text[2]
	except:
		select_what = "*"
		table_name = "country"
		where = "1"

	query = "SELECT %s FROM %s WHERE %s"%(select_what, table_name, where)

	frame1 = Frame(root)
	print_query = "SELECT %s \nFROM %s\nWHERE %s;"%(select_what, table_name, where)
	head = Label(frame1, text = print_query, fg = "red").grid(row = 0)
	frame1.grid(row = 0)

	frame2 = Frame(root)

	try:
		db = MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	except:
		os.system("sudo /opt/lampp/xampp start")
		db = MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	cursor = db.cursor()

	tabel = []

	if select_what == "*":
		attrib = 0
		table_list = table_name.split(",")

		for each_table_name in table_list:
			cursor.execute("DESC %s"%(each_table_name))
			result = cursor.fetchall()

			label = []
			for j in range(len(result)):
				lab = Label(frame2, text=str(result[j][0]), height = 2, width = 25, font = "Times\ New\ Roman 13 bold", bg= "black", fg = "white").grid(row = 1, column = attrib + j)
				label.append(lab)

			tabel.append(label)
			attrib = attrib + len(result)

	else:
		attrib_list = select_what.split(",")
		attrib = len(attrib_list)
		label = []
		j = 0

		for each_attrib in attrib_list:
			lab = Label(frame2, text = str(each_attrib), height = 2, width = 25, font = "Times\ New\ Roman 13 bold", bg = "black", fg = "white").grid(row = 1, column = j)
			j = j + 1
			label.append(lab)

		tabel.append(label)

	cursor.execute(query)
	result = cursor.fetchall()
	db.close()

	for i in range(len(result)):
		label = []
	
		for j in range(attrib):
			if (j)%2 == 0:
				bg = "pink"
			else:
				bg = "grey"
	
			lab = Label(frame2, text=str(result[i][j]), height = 2, bg = bg, width = 32, font = "Times\ New\ Roman 10").grid(row = i + 2, column = j)
			label.append(lab)
	
		tabel.append(label)
	
	frame2.grid(row = 1)	

except:
	print "Stupid Input!!! X(  " + query 
mainloop()