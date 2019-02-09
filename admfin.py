#Author: Hybridth
#Versi: V1
#Date :09/02/2019

import sys
import httplib
import socket
import random
	      
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

#Real Fun Start Here!
class adminfinder():
	print 
	print GREEN+"ADMIN FINDER BY HYBRIDTH"
	print GREEN+"Tools V1"
	print GREEN+"NB: Tools Ini Belum 100% jadi Next Update Akan Berjalan Dengan Normal"
	print GREEN+"Enjoy"
	print 

	def __init__(self):
		self.admin_locate()

	def admin_locate(self):
		try:
		   sites = raw_input(RED+"Masukan Sitenya Cok: %s"%(ENDC))
		   site = sites.replace("http://", "")
		   print (BLUE+"\n\t[*] Enteni Disek %s{}"%(ENDC)).format(site)
		   conn = httplib.HTTPConnection(site)
		   kntl = conn.connect() # Connecting The Website
		   print (BLUE+"\t[+] Di Temokno Cok. %s{}"%(ENDC)).format(kntl)
		except EOFError:
		   print (RED+"\t[!] Gak onok Cok. %s{}"%(ENDC)).format(kntl)
		   sys.exit()

	        print (YELLOW+"\t[*] Memproses. %s {}"%(ENDC)).format(kntl)

		# This Will Loop through Word to get Admin Page
		wordfile = open("wordlist.txt", "r")
		wordlist = wordfile.readlines()
		wordfile.close()


		for word in wordlist:
		    admin = word.strip("\n")
		    sadmin = "/" + admin
		    target = site + admin
		    print (BLUE + "[+] Mengecek: %s{}"% (ENDC)).format(kntl)
		    connection = httplib.HTTPConnection(site)
		    connection.request("GET", admin)
		    response = connection.getresponse()


		    # Deciding the Response Status and Print out the Result!...
		    if response.status == 200:
			print (GREEN + "\n\n\t+------------------+ %s{}"%(ENDC)).format(kntl)
			print  (GREEN + "\t[!]Onok Iki Loh Cok>> %s{}"%(ENDC)).format(target)
			print (GREEN + "\t+------------------+\n %s{}"%(ENDC)).format(kntl)
			raw_input(BLUE + "[*] Enter For Done. \n %s{}"%(ENDC)).format(kntl)



adminfinder()
