import Tkinter as tk
import MySQLdb
from PIL import ImageTk, Image
from datetime import datetime
from generate_list import generate_country_list
from server import *

class tax_calculator:
    def __init__(self, parent):
        self.parent=parent
        self.parent.minsize(width=700, height=400)
        self.frame=tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.head=tk.Label(self.frame, text="Charges Calculator", width=25, font="Verdana 20 bold", bg="orange").pack(pady=5)

        self.list6=generate_country_list()
        self.country = tk.StringVar()
        self.box5 = tk.OptionMenu(self.frame, self.country,     *self.list6).pack(pady = 5)
        self.country.set(u"Select Country")

        self.str2=tk.StringVar()
        self.box2=tk.Entry(self.frame, textvariable=self.str2, width=30, font="Ariel 15")
        self.box2.pack(pady=5)
        self.str2.set(u"Weight (kg)")

        self.str3=tk.StringVar()
        self.box3=tk.Entry(self.frame, textvariable=self.str3, width=30, font="Ariel 15")
        self.box3.pack(pady=5)
        self.str3.set(u"Number of days")

        self.but1=tk.Button(self.frame, text="Calculate", command=self.calculate, width=30, font="Ariel 15").pack(pady=5)

        self.str4=tk.StringVar()
        self.lab=tk.Label(self.frame, textvariable=self.str4, width=30, height=6, font="Ariel 20 italic", bg="green").pack(pady=5)

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(pady = 5) 
        
        self.frame.pack(pady=5)

    def calculate(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
	    	self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        self.str4.set(u"")
        try:
            code=self.list6[self.country.get()]
            weight=float(self.box2.get())
            days=int(self.box3.get())
            sql="SELECT * FROM country WHERE country_code='%d'"%(code)
            cursor=self.db.cursor()
            cursor.execute(sql)
            res=cursor.fetchall()
            result=res[0]
            country, duty, excise, charge = result[1], result[2], result[3], result[4]
            if 0<weight<=100:
                fixed_charge=charge
            elif 100<weight<=400:
                fixed_charge=1.4*charge
            elif 400<=1500:
                fixed_charge=1.8*charge
            else:
                fixed_charge=2*charge

            exempt_charge = excise + 0.04*fixed_charge
            total_tax = fixed_charge + exempt_charge * duty/100
            surge = days * total_tax
            ans = "\nCountry : %s\nFixed Charge = INR %0.2f \nExemption Charges = INR %0.2f\nTotal Tax = INR %0.2f\nSurge = INR %0.2f"%(country, fixed_charge, exempt_charge, total_tax, surge) 
            self.str4.set(ans)
            print "Taxation query @ %.19s"%(datetime.now())
            
        except:
            self.str4.set(u"Error: Invalid Input")
        self.db.close()

    def close(self):
        self.parent.destroy()
 
if __name__=="__main__":
    root=tk.Tk()
    app=tax_calculator(root)
    root.mainloop()
