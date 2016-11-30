import Tkinter as tk
import MySQLdb
import webbrowser as localhost
from PIL import ImageTk, Image
from user  import MainApp
from admin import admin
from server import *

class login:
    def __init__(self, parent):
        self.parent=parent
        self.parent.minsize(width=900,height=300)
        self.frame=tk.Frame(self.parent).pack(pady=5)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.head=tk.Label(self.frame, text="----Customs---\n---Login---", fg="black", bg="orange", width=25, font = "Verdana 25 bold").pack(pady=5)

        self.uname=tk.StringVar()
        self.box1=tk.Entry(self.frame, textvariable=self.uname, width=50, fg="blue", font = "Ariel 15")
        self.box1.pack(pady=5)
        self.uname.set(u"Username")

        self.passw=tk.StringVar()
        self.box2=tk.Entry(self.frame, show="*", textvariable=self.passw, width=50, bg="green", font = "Ariel 15")
        self.box2.pack(pady=5)
        self.passw.set(u"Password")

        self.button=tk.Button(self.frame, text="Login", command=self.login, width=25, font = "Ariel 15").pack(pady=5)

        self.status=tk.StringVar()
        self.label=tk.Label(self.frame, textvariable=self.status, width=50, font = "Ariel 15").pack(pady=5)
        self.status.set(u"Enter Username and Password")

        self.bot=tk.Label(self.frame, text = "Customs Management System \nalias\n\nProject Amigo (Copyright 2016)", fg="red", bg="blue", font="Comic\ Sans\ Ms 25 ", width=30).pack(pady=5)
        localhost.open("http://localhost/phpmyadmin")
    def login(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            username=self.box1.get()
            password=self.box2.get()
            
            cursor = self.db.cursor()
            sql="SELECT * FROM admin where username='%s' && pword='%s'"%(username, password)
            cursor.execute(sql)
            result=cursor.fetchall()
            self.db.close()            
            if len(result)>0:
                self.parent.destroy()
                root=tk.Tk()
                if username!="admin":
                    app=MainApp(root)            
                else:
                    app=admin(root)
                root.mainloop()
            else:
                self.status.set(u"Login Failed")
        except:
            self.status.set(u"Launch MySQL Server First")

if __name__=="__main__":
    root=tk.Tk()
    app=login(root)
    root.mainloop()
