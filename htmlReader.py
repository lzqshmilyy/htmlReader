#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import *
import re
import csv
import codecs
import sys

def main():
	global soup 
	soup = BeautifulSoup(open("2.html"), "lxml")
	
	nameList = getName()
	number = len(nameList)
	skuList = getSKU()
	priceList = getPrice(number)
	quantityList = getQuantity()
	"""
	for i in range(0, number):
		print nameList[i]
		print skuList[i]
		print priceList[i]
		print quantityList[i]
"""

	csvfile = file('sales.csv', 'wb')
	writer = csv.writer(csvfile)
	writer.writerow(['Name', 'SKU', 'Price', 'Quantity'])

	data = []
	for i in range(0, number):
		line = [nameList[i], skuList[i], priceList[i], quantityList[i]]
		data.append(line)

	writer.writerows(data)

	csvfile.close()



def getName():
	nameList = []
	for name in soup.find_all('h5'):
		nameList.append(name.string.encode('ANSI', 'replace'))
	return nameList

def getSKU():
	skuList = []
	for sku in soup.select('td div strong'):
			skuList.append(sku.next_sibling.strip())
	return skuList

def getPrice(number):
	priceList = []
	priceTag = soup.select('td span span')
	for i in range(0,number):
		i = i * 2
		price = priceTag[i]
		priceList.append(str(price.string[2:]))
	return priceList

def getQuantity():
	quantityList = []
	for quantity in soup.find_all('td', 'a-center'):
		quantityList.append(quantity.string)
	return quantityList
	


if __name__ == '__main__':
	main()