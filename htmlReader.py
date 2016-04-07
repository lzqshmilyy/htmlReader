#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import *
import re

def main():
	global soup 
	soup = BeautifulSoup(open("1.html"), "lxml")
	skuList = getSKU()
	for sku in skuList:
		print sku
	


def getName():
	namePattern = re.compile("h5")
	nameTag = soup.find_all(namePattern)
	name = []
	for text in nameTag:
		txt = str(text)
		txt = txt.lstrip('<h5 class="title"><span id="order_item_1234567890_title">').rstrip('</span></h5>')
		name.append(txt)
	return name

def getSKU():
	skuList = []
	skuTag = soup.find_all(text = re.compile('\d{7,8}'))
	for sku in skuTag:
		try:
			skuString = str(sku).strip()
			if re.match('^\d{7,8}$', skuString):
				skuList.append(skuString)
		except:
			continue
	return skuList


if __name__ == '__main__':
	main()