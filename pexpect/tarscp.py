#!/usr/bin/python
#coding=utf-8

import pexpect
import sys,os

ip="10.1.4.186"
user="root"
passwd="p@ssw0rd"
target_file="/dengminhui"

#child=pexpect.spawn('/usr/bin/ssh',[user+'@'+ip])
child=pexpect.spawn('ssh root@10.1.4.186')
fout=file('mylog.txt','w')
child.logfile=fout
try:
	child.expect('password:')
	child.sendline(passwd)
	child.expect('#')
	child.sendline('tar -czf /dengminhui.tar.gz /dengminhui')

	child.expect('#')
	print child.before
	child.sendline('exit')
	fout.close()
#except EOF:
#	print "expect EOF"
#except TIMEOUT:
#	print "expect TIMEOUT"
except Exception,e:
	print "Exception error"
child=pexpect.spawn('scp root@10.1.4.186:/dengminhui.tar.gz /')
fout=file('mylog.txt','a')
child.logfile=fout
try:
	child.expect('password:')
	child.sendline(passwd)
	child.expect(pexpect.EOF)
#except EOF:
#	print "expect EOF"
#except TIMEOUT:	
#	print "expect TIMEOUT"
except Exception,e:
	print "Exception error"		
