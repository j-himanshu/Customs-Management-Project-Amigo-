import Tkinter as tk
import MySQLdb
from PIL import ImageTk, Image
from datetime import datetime
from server import *

class company:
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=400,height=300)
        self.frame = tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.label0=tk.Label(self.frame, text="---Company---", width=20, fg="green", bg="cyan", font="Ariel 25 bold").pack(pady=10)

        self.str0=tk.StringVar()
        self.box0=tk.Entry(self.frame, textvariable=self.str0, width=30, font="Ariel 15")
        self.box0.pack(pady=10)
        self.str0.set(u"Company ID")

        self.str1=tk.StringVar()
        self.box1=tk.Entry(self.frame, textvariable=self.str1, width=30, font="Ariel 15")
        self.box1.pack(pady=10)
        self.str1.set(u"Company Name (Ex: Air Carriers)")

        self.str5=tk.StringVar()
        self.label1=tk.Label(self.frame, textvariable=self.str5, width=25, fg="green", bg="magenta", font="Ariel 15").pack(pady=10)

        self.button=tk.Button(self.frame, text="Add Company", width=25, command=self.insert, font="Ariel 15").pack(pady=10)

        self.str2=tk.StringVar()
        self.box2=tk.Entry(self.frame, textvariable=self.str2, width=25, font="Ariel 15")
        self.box2.pack(pady=10)
        self.str2.set(u"Location")

        self.button2=tk.Button(self.frame, text="Add Company Location", width=25, command=self.loca, font="Ariel 15").pack(pady=10)

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(pady = 5) 
        
        self.frame.pack(pady=10)

    def insert(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
	    	self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            Id=int(self.box0.get())
            name=self.box1.get()
            sql="INSERT INTO company VALUES('%d', '%s')"%(Id, name)
            cursor=self.db.cursor()
            cursor.execute(sql)
            self.str5.set(u"Inserted Successfully")
            print "New Company Added: %s, @ %0.19s"%(name, datetime.now())
            self.db.commit()
            self.db.close()
        except:
            self.str5.set(u"Insertion Error")
            self.db.rollback()
            self.db.close()

    def loca(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            Id=int(self.box0.get())
            location=self.box2.get()
            sql="SELECT * FROM location WHERE company_id='%d' && location='%s'"%(Id, location)
            cursor=self.db.cursor()
            cursor.execute(sql)
            result=cursor.fetchall()
            if len(result)>0:
                self.str5.set(u"Location Already Exists")
            else:
                sql="INSERT INTO location VALUES('%d', '%s')"%(Id, location)
                cursor.execute(sql)
                self.str5.set(u"Location Added")
                print "Location Added @ %.19s"%(datetime.now())
            self.db.commit()
            self.db.close()
        except:
            self.str5.set(u"Error")
            self.db.rollback()
            self.db.close()
    
    def close(self):
        self.parent.destroy()

if __name__=="__main__":
    root=tk.Tk()
    app=company(root)
    root.mainloop()
