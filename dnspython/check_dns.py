#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dns.resolver
import os
import httplib

domain='www.qq.com'
iplist=[]

def get_iplist(appdomain=""):
	try:
		A=dns.resolver.query(appdomain,'A')
	except Exception,e:
		print "dns resolver error:"+str(e)
		return
	for i in A.response.answer:
		for j in i.items:
			iplist.append(j.address)
	return True

def checkip(ip):
	checkurl=ip+":80"
	getcontent=""
	httplib.socket.setdefaulttimeout(5)
	conn=httplib.HTTPConnection(checkurl)
 
	try:
		conn.request("GET","/",headers={"Host":domain})
		
		r=conn.getresponse()
		getcontent = r.read(9)

		print getcontent 

	finally:
		if getcontent=="<!DOCTYPE":
			print ip+"[ok]"
		else:
			print ip+"[ERROR]"
if __name__=="__main__":
	if get_iplist(domain) and len(iplist)>0:
		for ip in iplist:
			checkip(ip)
	else:
		print "dns resolver error."
