#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2

file = open("newfile.txt", "a")
a=1
while(1):
	theurl = "https://eksisozluk.com/recep-tayyip-erdogan--95281?p="+str(a)
	thepage = urllib2.urlopen(theurl)


	soup = BeautifulSoup(thepage,"html.parser")
	for entries in soup.findAll('li',{"data-flags":"share vote report"}):
		file.write(str(entries.get('data-author')) + "\n")
		file.write(str(entries.find('div',{'class':'content'}))+ "\n")
		file.write(str(entries.find('a',{'class':'entry-date permalink'}).text)+ "\n")
		file.write("----------------------------------------------------------------------\n\n")
		a=a+1
		print(a)
		print()


#dnzyslrmk@gmail.com 2011