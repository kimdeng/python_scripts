#!/usr/bin/python
#coding=utf-8

import pexpect
import sys

child=pexpect.spawn('ssh root@10.1.4.186')
fout=file('mylog.txt','w')
child.logfile=fout

child.expect("password:")
child.sendline("p@ssw0rd")
child.expect('#')
child.sendline('ls /root')
child.expect('#')

