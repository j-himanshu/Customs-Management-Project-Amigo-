import Tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime
from tax import tax
from calc import tax_calculator
from product import product
from carrier import carrier
from new_manifest import new_manifest
from search import search
from view import view_all
from report import report
from label import label

class MainApp:
    def __init__(self, parent):
        self.parent=parent
        self.parent.minsize(width=900,height=300)
        self.frame=tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.headl=tk.Label(self.frame, text="----Welcome User----", width=20, bg="orange", fg="red", font = "Verdana 25 bold").pack(pady=5)

        self.but0=tk.Button(self.frame, text="New Manifest", command=self.new, width=30, bg="orange", font = "Ariel 15").pack(pady=5)

        self.but1=tk.Button(self.frame, text="Search Manifest", command=self.search, width=30, bg="orange", font = "Ariel 15").pack(pady=5)

        self.but2=tk.Button(self.frame, text="View All", command=self.show, width=30, fg="blue", bg="white", font = "Ariel 15").pack(pady=5)

        self.but3=tk.Button(self.frame, text="Add Carrier", command=self.carry, width=30, fg="blue", bg="white", font = "Ariel 15").pack(pady=5)

        self.but3=tk.Button(self.frame, text="Add New Product", command=self.prodct, width=30, fg="blue", bg="white", font = "Ariel 15").pack(pady=5)

        self.but5=tk.Button(self.frame, text="Countries and Taxes", command=self.tax, width=30, bg="green", font = "Ariel 15").pack(pady=5)

        self.but6=tk.Button(self.frame, text="Tax and charge Calculator", command=self.calc, width=30, bg="green", font = "Ariel 15").pack(pady=5)

        self.but7=tk.Button(self.frame, text="Generate Report", command = report, width=30, bg="green", font = "Ariel 10").pack(pady=5, side="left")

        self.but8=tk.Button(self.frame, text="Print Labels", command = label, width=30, bg="green", font = "Ariel 10").pack(pady=5, side="right")

        self.frame.pack(pady=5)

    def new(self):
    	print "New Manifest Activity Started @ %.19s"%(datetime.now())
        self.newman=tk.Toplevel(self.parent)
        self.app=new_manifest(self.newman)

    def search(self):
    	print "Search Manifest Activity Started @ %.19s"%(datetime.now())	
        self.srch=tk.Toplevel(self.parent)
        self.app=search(self.srch)

    def show(self):
    	print "Display Manifest Activity Started @ %.19s"%(datetime.now())
        self.veiw=tk.Toplevel(self.parent)
        self.app=view_all(self.veiw)

    def carry(self):
    	print "Carrier Activity Started @ %.19s"%(datetime.now())
        self.carrierr=tk.Toplevel(self.parent)
        self.app=carrier(self.carrierr)

    def prodct(self):
    	print "Product Activity Started @ %.19s"%(datetime.now())
        self.prod=tk.Toplevel(self.parent)
        self.app=product(self.prod)

    def tax(self):
    	print "Taxation Activity Started @ %.19s"%(datetime.now())
        self.tx=tk.Toplevel(self.parent)
        self.app=tax(self.tx)

    def calc(self):
    	print "Tax Calculator Activity Started @ %.19s"%(datetime.now())
        self.cal=tk.Toplevel(self.parent)
        self.app=tax_calculator(self.cal)      

if __name__=="__main__":
    root=tk.Tk()
    app=MainApp(root)
    root.mainloop()