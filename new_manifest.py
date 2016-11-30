import smtplib
import Tkinter as tk
import MySQLdb
from random import randint
from PIL import ImageTk, Image
from datetime import datetime
from generate_list import *
from server import *

class new_manifest:
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=400,height=300)
        self.frame = tk.Frame(self.parent)
        
        self.img = ImageTk.PhotoImage(Image.open("db_amigo.jpg"))
        self.panel1 = tk.Label(self.frame, image = self.img).pack(side = "left", fill = "both", expand = "yes")
        self.panel2 = tk.Label(self.frame, image = self.img).pack(side = "right", fill = "both", expand = "yes")

        self.head=tk.Label(self.frame,text="New Manifest", width=15, font="Comic_sans_ms 25 bold", bg="green", fg="red").pack(pady = 5)

        self.list1=generate_issuer_list()
        self.issuer_info=tk.StringVar()
        self.box0=tk.OptionMenu(self.frame, self.issuer_info, *self.list1).pack(pady = 5)
        self.issuer_info.set(u"Select Issuer")

        self.list2=generate_port_list()
        self.port_info=tk.StringVar()
        self.box1=tk.OptionMenu(self.frame, self.port_info,*self.list2).pack(pady = 5)
        self.port_info.set(u"Select FROM PORT")

        self.port_info2=tk.StringVar()
        self.box12=tk.OptionMenu(self.frame, self.port_info2, *self.list2).pack(pady = 5)
        self.port_info2.set(u"Select TO PORT")

        self.list3=generate_mode_list()
        self.mode_info=tk.StringVar()
        self.box2=tk.OptionMenu(self.frame, self.mode_info, *self.list3).pack(pady = 5)
        self.mode_info.set(u"Select Mode")

        self.list4=generate_carrier_list()
        self.comp_info=tk.StringVar()
        self.box3=tk.OptionMenu(self.frame, self.comp_info, *self.list4).pack(pady = 5)
        self.comp_info.set(u"Select Carrier")

        self.list5=generate_product_list()
        self.prod = tk.StringVar()
        self.box4 = tk.OptionMenu(self.frame, self.prod, *self.list5).pack(pady = 5)
        self.prod.set(u"Select Product")

        self.list6=generate_country_list()
        self.country = tk.StringVar()
        self.box5 = tk.OptionMenu(self.frame, self.country, 	*self.list6).pack(pady = 5)
        self.country.set(u"Select Country")

        self.remark = tk.StringVar()
        self.box6 = tk.Entry(self.frame, textvariable = self.remark, width = 50, bg="yellow")
        self.box6.pack(pady = 5)
        self.remark.set(u"Remarks(optional)")
        
        self.button=tk.Button(self.frame, text="Submit", width=25, command=self.insert, font="Ariel 15", bg="red", fg = "blue").pack(pady = 5)

        self.status=tk.StringVar()
        self.label=tk.Label(self.frame, textvariable=self.status, width=25, bg="purple", font="Ariel 15")
        self.label.pack(pady = 5)
        self.status.set(u"Enter Values")

        self.close_button = tk.Button(self.frame, text = "Back", bg="red", fg = "white", command = self.close).pack(pady = 5) 
        
        self.frame.pack(pady = 5)

    def close(self):
        self.parent.destroy()


    def insert(self):
    	try:
    		db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
    	except:
            start_server()
            db= MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        cursor=db.cursor()
        result=[1]
        try:
            while len(result)>0:
                manifest_id= randint(0, 10000)
                sql = "SELECT * FROM manifest WHERE manifest_id = '%d'"%(manifest_id)
                cursor.execute(sql)
                result=cursor.fetchall()

            product_id = self.list5[self.prod.get()]
            carrier_id = self.list4[self.comp_info.get()]
            issuer_id  = self.list1[self.issuer_info.get()]
            mode_id    = self.list3[self.mode_info.get()]
            date=str(datetime.now())
            date=date[0:10]
            country_code = self.list6[self.country.get()]

            from_port_id = self.list2[self.port_info.get()]
            to_port_id = self.list2[self.port_info2.get()]
            remarks = self.box6.get()
            if remarks == "Remarks(optional)":
                remarks = ""

            #get weight of product
            sql = "SELECT category, weight FROM product WHERE id = '%d'"%(product_id)
            cursor.execute(sql)
            result=cursor.fetchall()
            category, weight=result[0][0], float(result[0][1])

            #Malicious product check
            if category == "Malicious" or category == "malicious":
                self.status.set(u"Malicious Product\nCannot generate manifest\nContact\nadmin or customs officer")

                gmail_user = 'customs.rv.amigo@gmail.com'  
                gmail_password = 'rabecaps'
                
                dat = str(datetime.now())
                From = 'customs.rv.amigo@gmail.com'
                to = ['himanshu.janawadkar14@gmail.com']  
                subject = 'Malicious Product #'+dat
                body="System Admin/Custom officer,\n\tMalicious product manifest generation tried. \nRespond immediately"
                email_text = "From: %s \nTo: %s \nSubject: %s \n\n%s" %(From, ", ".join(to), subject, body)

                try:
                    filee = open("log.txt", "a")
                    filee.write("\n%s: %s"%(dat, body))
                    filee.close()
                except:  
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    #server.starttls()
                    server.ehlo()
                    server.login(gmail_user, gmail_password)
                    server.sendmail(From, to, email_text)
                    server.close()

            else:
                #calculate the tax
                sql = "SELECT * FROM country WHERE country_code = '%d'"%(country_code)
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
                bill_amount = fixed_charge + exempt_charge * duty/100
                
                #insert in manifest table
                sql = "INSERT INTO manifest VALUES('%d', '%d', '%d', '%d', '%d', '%s')"%(manifest_id, carrier_id, issuer_id, mode_id, product_id, remarks)
                cursor.execute(sql)
                #insert in bill of landing table
                sql = "INSERT INTO bill_of_landing VALUES('%d', '%d', '%s', '%d', '%f')"%(10000-manifest_id, country_code, date, manifest_id, bill_amount)
                cursor.execute(sql)
                #insert in manifest_port
                sql = "INSERT INTO manifest_port VALUES('%d', '%d', '%d')"%(manifest_id, from_port_id, to_port_id)
                cursor.execute(sql)
                db.commit()
                self.status.set(u"Manifest\nGenerated\nSuccessfully\nID: %d"%(manifest_id))
                print "Manifest %d Generated @ %.19s"%(manifest_id, datetime.now())
            db.close()

        except:
            self.status.set(u"Error Insertion, please re validate details")
            db.rollback()
            db.close()
            pass


if __name__=="__main__":
    root = tk.Tk()
    app = new_manifest(root)
    root.mainloop()
