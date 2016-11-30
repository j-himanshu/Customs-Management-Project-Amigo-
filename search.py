import Tkinter as tk
import MySQLdb
from PIL import ImageTk, Image
from datetime import datetime
from server import *

def Search(manifest_id):
    try:
        db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    except:
        start_server()
        db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")

    cursor=db.cursor()
    
    try:    
        sql = "SELECT * FROM manifest WHERE manifest_id = '%d'"%(manifest_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        carrier_id, issuer_id, mode_id, product_id, remarks = result[1], result[2], result[3], result[4], result[5]

        sql = "SELECT * FROM bill_of_landing WHERE manifest_id = '%d'"%(manifest_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        bol_id, country_code, date, bill_amount = result[0], result[1], result[2], result[4]

        sql = "SELECT * FROM manifest_port WHERE manifest_id = '%d'"%(manifest_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        from_port_id, to_port_id = result[1], result[2]

        sql = "SELECT * FROM product WHERE id = '%d'"%(product_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        description = result[2]

        sql = "SELECT * FROM carrier WHERE carrier_id = '%d'"%(carrier_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        carrier_name = result[1]

        sql = "SELECT * FROM manifest_issuer WHERE issuer_id = '%d'"%(issuer_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        issuer_name = result[1]

        sql = "SELECT * FROM mode_of_transport WHERE mode_id = '%d'"%(mode_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        transport_description = result[1]

        sql = "SELECT * FROM country WHERE country_code = '%d'"%(country_code)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        country = result[1]

        sql = "SELECT * FROM port WHERE port_id = '%d'"%(from_port_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        from_port_name = result[1]

        sql = "SELECT * FROM port WHERE port_id = '%d'"%(to_port_id)
        cursor.execute(sql)
        result=cursor.fetchall()
        result=result[0]
        to_port_name = result[1]

        return [manifest_id, description, carrier_name, issuer_name, transport_description, bol_id, date, country, bill_amount, from_port_name, to_port_name, remarks]


    except:
        db.rollback()
        return []
    db.close()

class search:
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=400,height=300)
        self.frame = tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.lab1=tk.Label(self.frame, text="---Search Manifest---", width=20, fg="white", bg="black", font="Ariel 25 bold").pack(pady=5)

        self.str2=tk.StringVar()
        self.box1=tk.Entry(self.frame, textvariable=self.str2, width=25, font="Ariel 15")
        self.box1.pack(pady=5)
        self.str2.set(u"Manifest ID")

        self.but1=tk.Button(self.frame, text="Search", width=25, command=self.show, font="Ariel 15").pack(pady=5)

        self.str3=tk.StringVar()
        self.lab3=tk.Label(self.frame, textvariable=self.str3, width=35, height=13, fg="white", bg="black", font="Ariel 15 italic").pack(pady=5)

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(pady = 5) 
        
        self.frame.pack()

    def close(self):
        self.parent.destroy()

    def show(self):
        try:
        	manifest_id= int(self.box1.get())
        	result = Search(manifest_id)
        	[manifest_id, description, carrier_name, issuer_name, transport_description, bol_id, date, country, bill_amount, from_port_name, to_port_name, remarks] = result
        	answer = "MANIFEST : %d\nPRODUCT : %s \nCARRIED BY : %s\nISSUED BY : %s\nMODE : %s\n"%(manifest_id, description, carrier_name, issuer_name, transport_description)
        	answer = answer + "Bill Number : %d\nDate : %s\nCountry : %s\nBill amount = INR %0.2f\n"%(bol_id, date, country, bill_amount)
        	answer = answer + "From Port : %s\nTo Port : %s\n\n%s"%(from_port_name, to_port_name, remarks)
        	self.str3.set(answer)
        except:
        	self.str3.set(u"Manifest Not Found")

if __name__=="__main__":
    root=tk.Tk()
    app=search(root)
    root.mainloop()
