echo "Amigo Started"
date
sudo /opt/lampp/xampp start
echo "STARTED SERVER"
echo "MOUNTING PARTITION"
sudo mount /dev/sda3/ /media/D/
cd /media/D/PROJECT\ AMIGO\ DBMS/
python -c 'from restore_backup import restore_backup; restore_backup()'
echo "Here comes Amigo ... ;^)"
python login.py
python -c 'from backup import backup; backup()'
sleep 2
cd
echo "UNMOUNT PARTITION"
sudo umount /dev/sda3/
echo "STOPING SERVER"
sudo /opt/lampp/xampp stop