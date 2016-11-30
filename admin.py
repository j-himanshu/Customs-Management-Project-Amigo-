import Tkinter as tk
import os
from PIL import ImageTk, Image
from datetime import datetime
from account import Account
from country import country
from port import port
from transport import transport
from company import company
from manifestIssuer import manifestIssuer
from user import MainApp
from cli import CLI
from backup import backup
from restore_backup import restore_backup

class admin:

    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=900,height=300)
        self.frame = tk.Frame(self.parent).pack(pady=5)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.status=tk.StringVar()
        self.label=tk.Label(self.frame, textvariable=self.status, width=15, bg="blue", fg="red", font = "Verdana 25 bold").pack(pady=5)
        self.status.set(u"----Admin----")

        self.button0 = tk.Button(self.frame, text = "CREATE/Remove Account", width = 25, font="Ariel 15", command = self.add_remove,).pack(pady=5)

        self.button2 = tk.Button(self.frame, text = "Country Taxation", width = 25, font="Ariel 15", command = self.country).pack(pady=5)

        self.button3 = tk.Button(self.frame, text = "Add Port", width = 25, font="Ariel 15", command = self.port).pack(pady=5)

        self.button4 = tk.Button(self.frame, text = "Transportation", width = 25, font="Ariel 15", command = self.transport).pack(pady=5)

        self.button5 = tk.Button(self.frame, text = "Company", width = 25, font="Ariel 15", command = self.company).pack(pady=5)

        self.button6 = tk.Button(self.frame, text = "Manifest Issuer", width = 25, font="Ariel 15", command = self.manifest).pack(pady=5)

        self.button7 = tk.Button(self.frame, text = "User Console", width = 25, font="Ariel 15 italic", command = self.setup, bg="yellow", fg="red").pack(pady=5)
        
        self.button8 = tk.Button(self.frame, text = "Query", width=25, font="Ariel 15 italic", command=self.query, bg="black", fg="white").pack(pady=5)     

        self.button9 = tk.Button(self.frame, text = "Backup Database", width = 16, font = "Times\ New\ Roman 15 bold", command = backup, fg = "white", bg = "green").pack(side = "left", pady = 5)

        self.button10 = tk.Button(self.frame, text = "Restore Database", width = 16, font = "Times\ New\ Roman 15 bold", command = restore_backup, fg = "white", bg = "blue").pack(side= "right", pady = 5)

    def add_remove(self):
    	print "Account Activity opened @ %.19s"%(datetime.now())
        self.account = tk.Toplevel(self.parent)
        self.app = Account(self.account)

    def country(self):
    	print "Country Activity opened @ %.19s"%(datetime.now())
        self.countr = tk.Toplevel(self.parent)
        self.app=country(self.countr)

    def port(self):
    	print "Port Activity opened @ %.19s"%(datetime.now())
        self.por = tk.Toplevel(self.parent)
        self.app=port(self.por)

    def transport(self):
    	print "Transport Activity opened @ %.19s"%(datetime.now())
        self.transp = tk.Toplevel(self.parent)
        self.app=transport(self.transp)

    def company(self):
    	print "Company Activity opened @ %.19s"%(datetime.now())
        self.comp = tk.Toplevel(self.parent)
        self.app=company(self.comp)

    def manifest(self):
    	print "Manifest Activity opened @ %.19s"%(datetime.now())
        self.man = tk.Toplevel(self.parent)
        self.app=manifestIssuer(self.man)

    def setup(self):
    	print "User Activity opened @ %.19s"%(datetime.now())
        self.set = tk.Toplevel(self.parent)
        self.app = MainApp(self.set)
        
    def query(self):
    	print "Query Box opened @ %.19s"%(datetime.now())
        self.quer=tk.Toplevel(self.parent)
        self.app=CLI(self.quer)

if __name__=="__main__":
    root=tk.Tk()
    app=admin(root)
    root.mainloop()