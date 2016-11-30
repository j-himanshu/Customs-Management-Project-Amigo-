import Tkinter as tk
import MySQLdb
from PIL import ImageTk, Image
from datetime import datetime
from server import *

class country:
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=900,height=300)
        self.frame = tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.label0=tk.Label(self.frame, text="---Country---", width=25, fg="yellow", bg="green", font="Ariel 25 italic").pack(pady=10)

        self.str0=tk.StringVar()
        self.box0=tk.Entry(self.frame, textvariable=self.str0, width=25, font="Ariel 15")
        self.box0.pack(pady=10)
        self.str0.set(u"Country Code")

        self.str1=tk.StringVar()
        self.box1=tk.Entry(self.frame, textvariable=self.str1, width=25, font="Ariel 15")
        self.box1.pack(pady=10)
        self.str1.set(u"Country Name")

        self.str2=tk.StringVar()
        self.box2=tk.Entry(self.frame, textvariable=self.str2, width=25, font="Ariel 15")
        self.box2.pack(pady=10)
        self.str2.set(u"Duty %")

        self.str3=tk.StringVar()
        self.box3=tk.Entry(self.frame, textvariable=self.str3, width=25, font="Ariel 15")
        self.box3.pack(pady=10)
        self.str3.set(u"Excise")

        self.str4=tk.StringVar()
        self.box4=tk.Entry(self.frame, textvariable=self.str4, width=25, font="Ariel 15")
        self.box4.pack(pady=10)
        self.str4.set(u"Charges")

        self.str5=tk.StringVar()
        self.label1=tk.Label(self.frame, textvariable=self.str5, width=25, font="Ariel 15", fg="green", bg="yellow").pack(pady=10)

        self.button1=tk.Button(self.frame, text="Add", width=25, font="Ariel 15", command=self.insert).pack(pady=10)
        self.button2=tk.Button(self.frame, text="Update", width=25, font="Ariel 15", command=self.update, bg="black", fg="green").pack(pady=10)

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(pady = 5) 
 
        self.frame.pack(pady=10)

    def insert(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            code=int(self.box0.get())
            name=self.box1.get()
            duty=float(self.box2.get())
            excise=float(self.box3.get())
            charges=float(self.box4.get())
            sql="INSERT INTO country VALUES('%d', '%s', '%f', '%f', '%f')"%(code, name, duty, excise, charges)
            cursor=self.db.cursor()
            cursor.execute(sql)
            self.str5.set(u"Inserted Successfully")
            print "New Country Added: %s, @ %0.19s"%(name, datetime.now())
            self.db.commit()
            self.db.close()
        except:
            self.str5.set(u"Insertion Error")
            self.db.rollback()
            self.db.close()

    def update(self):
    	try:
    		db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
    		db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            code=int(self.box0.get())
            duty=float(self.box2.get())
            excise=float(self.box3.get())
            charges=float(self.box4.get())
            sql="UPDATE country SET duty = '%f', excise = '%f', charges = '%f' WHERE country_code = '%d'"%(duty, excise, charges, code)
            cursor=db.cursor()
            cursor.execute("SELECT * FROM country WHERE country_code= '%d'"%(code))
            result = cursor.fetchall()
            a=1/len(result) #generate error
            cursor.execute(sql)
            self.str5.set(u"Updated Successfully")
            print "%s : Taxes Updated, @ %.19s"%(name, datetime.now())
            db.commit()
        except:
            self.str5.set(u"Couldn't Update!")
            db.rollback()
        db.close()

    def close(self):
        self.parent.destroy()
        
if __name__=="__main__":
    root=tk.Tk()
    app=country(root)
    root.mainloop()
