#!/usr/bin/env python

import dns.resolver

domain=raw_input('please input: ')
MX=dns.resolver.query(domain,'MX')
for i in MX:
	print 'MX preference=',i.preference,'mail exchanger=',i.exchange
