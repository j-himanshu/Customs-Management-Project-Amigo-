import Tkinter as tk
import MySQLdb
from PIL import ImageTk, Image
from datetime import datetime
from generate_list import generate_company_list
from server import *

class carrier:
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=900,height=300)
        self.frame = tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.label0=tk.Label(self.frame, text="---Carrier---", width=20, fg="green", bg="pink", font="Ariel 25 italic").pack(pady=25)

        self.str0=tk.StringVar()
        self.box0=tk.Entry(self.frame, textvariable=self.str0, width=30, font="Ariel 15")
        self.box0.pack(pady=25)
        self.str0.set(u"Carrier ID")

        self.str1=tk.StringVar()
        self.box1=tk.Entry(self.frame, textvariable=self.str1, width=30, font="Ariel 15")
        self.box1.pack(pady=25)
        self.str1.set(u"Carrier Name (Ex: Courier Company)")

        self.list6=generate_company_list()
        self.company = tk.StringVar()
        self.box5 = tk.OptionMenu(self.frame, self.company, *self.list6).pack(pady = 5)
        self.company.set(u"Select Company")

        self.str5=tk.StringVar()
        self.label1=tk.Label(self.frame, textvariable=self.str5, width=25, fg="red", bg="blue", font="Ariel 15").pack(pady=25)

        self.button=tk.Button(self.frame, text="Insert", width=25, command=self.insert, font="Ariel 15").pack(pady=25)

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(pady = 5) 
        
        self.frame.pack(pady=25)

    def insert(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
	    	self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
	    	
        try:
            Id=int(self.box0.get())
            name=self.box1.get()
            company_id=self.list6[self.company.get()]
            
            sql="INSERT INTO carrier VALUES('%d', '%s')"%(Id, name)
            cursor=self.db.cursor()
            cursor.execute(sql)

            sql="INSERT INTO service_by VALUES('%d', '%d')"%(Id, company_id)
            cursor.execute(sql)
            
            self.str5.set(u"Inserted Successfully")
            print "Carrier Added : %s, @ %.19s"%(name, datetime.now())
            self.db.commit()
            self.db.close()
        except:
            self.str5.set(u"Insertion Error")
            self.db.rollback()
            self.db.close()


    def close(self):
        self.parent.destroy()
 
 

if __name__=="__main__":
    root=tk.Tk()
    app=carrier(root)
    root.mainloop()
