import MySQLdb
import Tkinter as tk
from PIL import ImageTk, Image
from server import *

class view_all:
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=400,height=300)
        self.frame = tk.Frame(self.parent)

        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.lab1=tk.Label(self.frame, text="---List of Manifests---", width=20, fg="white", bg="black", font="Ariel 25 bold").pack(pady=5)

        self.str3=tk.StringVar()
        self.lab3=tk.Label(self.frame, textvariable=self.str3, width=25, height=15, fg="white", bg="black", font="Ariel 15 italic").pack(pady=5)

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(pady = 5)       
        self.frame.pack()

        try:
            self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        except:
            start_server()
            self.db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        cursor=self.db.cursor()
        try:
            sql="SELECT manifest_id FROM manifest" 
            cursor.execute(sql)
            Result=cursor.fetchall()
            if len(Result)>0:
                ans = ""
                i = 1
                for res in Result:
                    ans = ans + "%5.0f"%(res[0]) + ",  "
                    if i%3 == 0:
                        ans = ans + "\n"
                    i=i+1
                self.str3.set(ans)
            else:
                self.str3.set(u"No Manifests")
        except:
            self.str3.set(u"Error")

    def close(self):
        self.parent.destroy()
        
if __name__=="__main__":
    root=tk.Tk()
    app=view_all(root)
    root.mainloop()
