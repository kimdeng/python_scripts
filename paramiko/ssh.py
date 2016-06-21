#!/usr/bin/python
#coding=utf-8

import paramiko
hostname='10.1.4.186'
username='root'
password='p@ssw0rd'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()
