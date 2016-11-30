import os
import MySQLdb
from datetime import datetime
from path import path
from server import *

def backup():
        dat = str(datetime.now())
        dat = dat[0:10] + '_'
        dat = dat + "Hour_" +str(datetime.now().hour) +"_Min_" + str(datetime.now().minute)

        mysqldump_path, backup_directory = path()

        if os.name == "nt":
                present_directory = backup_directory[0:backup_directory.find("Backup")]
                copy_python_files = "copy /Y " + present_directory + "*.py " + backup_directory
        else:
                copy_python_files = "cp *.py "+ backup_directory

        try:
        	db = MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        except:
        	start_server()
        os.system(copy_python_files)
        comman_command = "%smysqldump -h 127.0.0.1 -P 3306 -u root -proot customs > %sAmigo_Backup_%s.sql"%(mysqldump_path, backup_directory, dat)
        os.system(comman_command)
        restoration_db = "%smysqldump -h 127.0.0.1 -P 3306 -u root -proot customs > %sAmigo_Restore.sql"%(mysqldump_path, backup_directory)
        os.system(restoration_db)
        print "Database Backup Successful"