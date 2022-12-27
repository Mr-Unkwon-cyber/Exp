#DOMAIN EXTRAXTOR
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614

import re,time,random ,os, sys
from colorama import Fore

def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]

    x = '''

               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|  
=============
[ Domain Extraxtor | Python Code ]
'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)
Banner()

def Ex():
	try:
		pler = raw_input("Input : ")
		file = open(pler, 'r')
		for line in file:
			urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
			for res in urls:
				print(Fore.RED + 'Coded By Shin_Code' +' : '+Fore.GREEN + res + Fore.WHITE)
				open('domain.txt', 'a').write(res+'\n')
	except:
		pass
Ex()
      
