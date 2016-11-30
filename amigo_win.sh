echo "Amigo Started"
date
C:/xampp/xampp_start.exe
echo "STARTED SERVER"
python -c 'from restore_backup import restore_backup; restore_backup()'
echo "Here comes Amigo ... ;^)"
python login.py
python -c 'from backup import backup; backup()'
echo "STOPING SERVER"
C:/xampp/xampp_start.exe