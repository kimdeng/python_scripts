#!/usr/bin/env python

import dns.resolver

domain=raw_input('please  input a domain: ')
A = dns.resolver.query(domain,'CNAME')
for i in A.response.answer:
	for j in i.items:
		print j.to_text()
