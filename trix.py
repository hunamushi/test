#!/usr/bin/python
# -*- coding: utf-8 -*-

#import signal
import sys
import os
#def signal_handler(signum,stack):
#	print 'bye'
#	sys.exit()

#signal.signal(signal.SIGINT,signal_handler)
home = os.environ['HOME']
print u'ポータル認証'
try:
	f=open(home+'/matrix2.txt')
except:
	print 'error!'
	sys.exit()

s='abcdefghij'
S='ABCDEFGHIJ'
d={}
for i in range(1,11):
	d[s[i-1:i]]=i
	d[S[i-1:i]]=i
while True:
	print 'input A-J1-7:'
	try:
		i=raw_input()
	except EOFError:
		print 'Bye.'
		sys.exit()
	if i=='q':
		f.close()
		break
	elif i=='a' or i=='':
		print f.read()
		f.seek(0)
		continue
	try :
		num=int(i[1:])
		alp=i[:1]
		for m in range(num):
			f.readline()
		t=f.readline()
		c=d[alp]
		print t[c:c+1]
		f.seek(0)
	except:
		print "Error! Try again..."
		continue

