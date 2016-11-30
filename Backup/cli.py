import Tkinter as tk
import MySQLdb
import traceback
import os
from server import *
from query_box import query_box

class CLI:
    def __init__(self, parent):
        self.parent=parent
        self.frame=tk.Frame(self.parent)

        self.entryvar=tk.StringVar()
        self.entry=tk.Entry(self.frame, textvariable=self.entryvar, width=100, fg="white", bg="black", font="Ariel 15")
        self.entry.bind("<Return>", self.query2)
        self.entry.pack(pady = 5)
        self.entryvar.set(">>>Enter Query")
        self.entry.config(insertbackground = "white")

        self.flexlabel=tk.StringVar()
        self.label=tk.Label(self.frame, textvariable=self.flexlabel, width=137, fg="white", bg="black", anchor='w', font="Ariel 10")
        self.label.pack(pady = 5)
        self.flexlabel.set(">>>")

        self.flexlabel2=tk.StringVar()
        self.label2=tk.Label(self.frame, textvariable=self.flexlabel2, width=137, fg="white", bg="black", anchor='w', font="Ariel 10")
        self.label2.pack(pady = 5)
        self.flexlabel2.set(u"Enter your Query Mr. Admin")

        self.query_button = tk.Button(self.frame, text = "Custom Select Query", command=self.query, bg= "red", fg = "white").pack(pady=10)

        self.frame.pack()
        
    def query2(self, event):
    	try:
    		self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
            start_server()
            self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        try:
            sql=self.entry.get()
            cursor=self.db.cursor()
            cursor.execute(sql)
            result=cursor.fetchall()
            if len(result)>0:
                ans=">>>"
                for res in result:
                    ans=ans+str(res)+"\n"
                self.flexlabel.set(ans)
            else:
                self.flexlabel.set(">>>Query returned 0 rows")
            self.flexlabel2.set(">>>Successfully Executed")
            self.db.commit()
        except:
            self.flexlabel2.set(">>>")
            error=str(traceback.format_exc())
            error=">>>"+error[error.find("Error: "):len(error)]
            self.flexlabel.set(error)
            self.db.rollback()
        self.db.close()

    def query(self):
        self.quer= tk.Toplevel(self.parent)
        self.app = query_box(self.quer)    	        
if __name__=="__main__":
    root=tk.Tk()
    app=CLI(root)
    root.mainloop()
    os.system("python table.py")