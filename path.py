import os

def path():
        cwd = str(os.path.dirname(os.path.abspath(__file__)))
        current_directory = ""
        
        if os.name == "nt":
                #windows backup
                i = cwd.find("PROJECT AMIGO DBMS")
                backup_directory = cwd[0: i] + "\""  + cwd[i:len(cwd)] + "\"\\Backup\\"
                mysql_path = "C:\\xampp\\mysql\\bin\\"

        else:
                #Linux Backup
                cwd = cwd.split(' ')
                for word in cwd:
                        current_directory = current_directory + '\ ' + str(word)
                current_directory = current_directory[2:len(current_directory)]
                mysql_path = ""
                backup_directory = current_directory + "/Backup/"
        return [mysql_path, backup_directory]