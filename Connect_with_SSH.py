# -*- coding: utf-8 -*-

# Logger API'si icin 
import logging
# OS uzerinde komut calistirmak icin.
import os
import sys
# SSH baglantisi icin


# Scriptin bulundugu dizinin path bilgisini al.
_directory_of_Script_ = os.path.dirname(os.path.abspath(__file__))

# LOG dosyasi tanimlama.
log_fileName = ''+_directory_of_Script_+'/Connect_with_SSH_Script.txt'
logger = logging.getLogger('ScriptLogs')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(log_fileName)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("...............")
logger.debug("Script Starting...")

# Username ve Password bilgileri tanimlanir.
username = "user"
password = "pass"
commandList = []
# Komutlari dosyadan oku ve diziye at.
try:
    with open(''+_directory_of_Script_+'/Commands.txt','r') as commands:
        for row in commands:
            
            commandList.append(row)
            
    commands.close()
except:
    print("Unexcepted error : " +sys.exc_info()[0])
    

client1 = ""
def connection(HOST,USER,PASS):
  client1=paramiko.SSHClient()
  #Add missing client key
  client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  #connect to switch
  client1.connect(HOST,username=USER,password=PASS)
  print ("SSH connection  established with this server: " +HOST)
  #Gather commands and read the output from stdout
  # Baska bir metod komutlari çalıştırıp, sonucları dönsün.
  stdin, stdout, stderr = client1.exec_command('uptime\n')
  print (stdout.read())
  stdin, stdout, stderr = client1.exec_command('pwd\n')
  print (stdout.read())
  stdin, stdout, stderr = client1.exec_command( 'show processes memory | no-more\n')
  print (stdout.read())
  print (stderr.read())
  client1.close()
  print ("Logged out of device %s" %HOST)

        
# IP, bilgisini dosyadan okur, verilen username&password ile SSH baglantisi kur.
try:
    with open(''+_directory_of_Script_+'/connection_properties.txt','r') as readFile:
        for row in readFile:
            
            host = row
            print("Connecting to this server: " +row)
            connection(host,username,password)
                          
    readFile.close()
except:
    print("Unexcepted error : " +sys.exc_info()[0])
    
# Calistirilacak olan LINUX komutlarini bir dosyadan oku ve sirasiyle calistir.

