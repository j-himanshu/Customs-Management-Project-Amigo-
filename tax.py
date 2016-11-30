import Tkinter as tk
import MySQLdb
from PIL import ImageTk, Image
from generate_list import generate_country_list
from server import *

class tax:
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=400,height=300)
        self.frame = tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.lab1=tk.Label(self.frame, text="---Taxation---", width=20, fg="white", bg="black", font="Ariel 25 bold").pack(pady=5)

        self.list6=generate_country_list()
        self.country = tk.StringVar()
        self.box5 = tk.OptionMenu(self.frame, self.country, *self.list6).pack(pady = 5)
        self.country.set(u"Select Country")

        self.but1=tk.Button(self.frame, text="Search", width=25, command=self.search, font="Ariel 15").pack(pady=5)

        self.str3=tk.StringVar()
        self.lab3=tk.Label(self.frame, textvariable=self.str3, width=25, height=10, fg="white", bg="black", font="Ariel 15 italic").pack(pady=5)

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(pady = 5) 
        
        self.frame.pack()

    def search(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            code=self.list6[self.country.get()]
            sql="SELECT * FROM country WHERE country_code='%d'"%(code)
            cursor=self.db.cursor() 
            cursor.execute(sql)
            Result=cursor.fetchall()
            if len(Result)>0:
                result=Result[0]
                ans="Country: %s\nCode: %d\nDuty = %.2f %%\nExcise = %.2f\nCharges = %.2f\nAll charges in INR"%(result[1], result[0], result[2], result[3], result[4])
                self.str3.set(ans)
            else:
                self.str3.set(u"Not Found")
        except:
            self.str3.set(u"Error")

    def close(self):
        self.parent.destroy()
        
if __name__=="__main__":
    root=tk.Tk()
    app=tax(root)
    root.mainloop()
