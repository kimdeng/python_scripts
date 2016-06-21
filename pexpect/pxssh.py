#!/usr/bin/python
#coding=utf-8
import pexpect
from pexpect import pxssh
import getpass
import sys,os

#def writelog(text):
#	f=open('mylog.txt','a')
#	f.write('text')
#	f.close()
	

try:
	s=pxssh.pxssh()
	hostname=raw_input('hostname: ')
	username=raw_input('username: ')
	password=getpass.getpass('please input password: ')
	s.login(hostname,username,password)
	s.sendline('uptime')
	s.prompt()
	print s.before
	
	s.sendline('ls -l')
	s.prompt()
	print s.before
	s.sendline('df -h')
	print s.before
	s.logout()
except pxssh.ExceptionPxssh,e:
	print "pxssh failed on login."
	print str(e)


