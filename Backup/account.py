import MySQLdb
import Tkinter as tk
import re
from PIL import ImageTk, Image
from datetime import datetime
from server import *
from generate_list import generate_user_list

class Account:
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=400,height=300)
        self.frame = tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.entryVariable1 = tk.StringVar()
        self.entry1 = tk.Entry(self.frame, textvariable = self.entryVariable1, width = 25, font="Ariel 15")
        self.entry1.pack(pady=5)
        self.entryVariable1.set(u"Username");

        self.entryVariable2 = tk.StringVar()
        self.entry2 = tk.Entry(self.frame, show="*", textvariable = self.entryVariable2, width = 25, font="Ariel 15")
        self.entry2.pack(pady=5)
        self.entryVariable2.set(u"Password");

        self.button = tk.Button(self.frame, text = "Add Account", width = 25, command = self.add, font="Ariel 15").pack(pady=5)

        self.button2 = tk.Button(self.frame, text = "Delete Account", width = 25, command = self.remove, font="Ariel 15").pack(pady=5)

        self.status=tk.StringVar()
        self.label=tk.Label(self.frame, textvariable=self.status, width=25, font="Ariel 15", bg="green").pack(pady=5)
        self.status.set(u"Enter")

        self.users_list = tk.StringVar()
        self.User_list = tk.Label(self.frame, textvariable = self.users_list, font = "Times\ New\ Roman 15").pack(pady = 5)

        instructions = "Rules for Password\n1. Length-minimum 10 characters\n2. Should have atleast one UPPERCASE [A-Z]\none lowercase alphabet [a-z] &\none digit [0-9]"
        self.instructions = tk.Label(self.frame, text = instructions).pack(side = "bottom")

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(side = "bottom", pady = 5) 
      
        self.show_users()

        self.frame.pack(pady=5)

    def add(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
			start_server()
			self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            username=self.entry1.get()
            password=self.entry2.get()
            m = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$')
            if m.match(password):
                sql = "INSERT INTO admin VALUES('%s', '%s')"%(username, password)
                cursor=self.db.cursor()
                cursor.execute(sql)
                self.status.set(u"Added Successfully")
                print "Account Activity: %s Account Added @ %.19s"%(username, datetime.now())
            else:
                self.status.set(u"Enter Valid password")
            self.db.commit()
            self.db.close()
        except:
            self.db.rollback()
            self.status.set(u"Invalid Credentials")
        self.show_users()

    def remove(self):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
    		start_server()
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            username=self.entry1.get()
            password=self.entry2.get()
            sql = "select * from admin WHERE username='%s' && pword='%s'" %(username, password)
            cursor=self.db.cursor()
            cursor.execute(sql)
            result=cursor.fetchall()
            if len(result)>0 and username!="admin":
                self.status.set(u"Removed Successfully")
                print "Account Activity: %s Account Deleted @ %.19s"%(username, datetime.now())
            else:
                self.status.set(u"Invalid Credentials")
            sql = "DELETE FROM admin WHERE username='%s' && pword='%s'" %(username, password)
            cursor=self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
            self.db.close()
        except:
            self.db.rollback()
            self.status.set(u"Invalid Credentials")
        self.show_users()

    def show_users(self):
        usernames = "Users' List : \n"
        userlist = generate_user_list()
        i = 1
        for each_user in userlist:
            usernames = usernames + "|" + str(each_user) + "|"

            if i % 4 == 0:
                usernames = usernames + "\n" 
            i = i + 1
        self.users_list.set(usernames)
    
    def close(self):
        self.parent.destroy()

if __name__=="__main__":
    root=tk.Tk()
    app=Account(root)
    root.mainloop()
