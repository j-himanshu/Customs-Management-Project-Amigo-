import os
import MySQLdb
from datetime import datetime
from path import path
from server import *

def restore_backup():
        mysql_path, backup_directory = path()
        try:
        	db = MySQLdb.connect("127.0.0.1", "root", "root", "customs")
        except:
        	start_server()
        comman_command = "%smysql -h 127.0.0.1 -P 3306 -u root -proot customs < %sAmigo_Restore.sql"%(mysql_path, backup_directory)
        os.system(comman_command)
        print "Database Succesfully Recovered/Restored from last saved state @ %.19s"%(datetime.now())