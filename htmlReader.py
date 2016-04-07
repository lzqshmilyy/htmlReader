#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import *
import re

def main():
	global soup 
	soup = BeautifulSoup(open("2.html"), "lxml")

	nameList = getName()
	number = len(nameList)
	skuList = getSKU()
	priceList = getPrice(number)
	quantityList = getQuantity()

	for i in range(0, number):
		print nameList[i] + ' ' + skuList[i] + ' ' + priceList[i] + ' ' + quantityList[i]

def getName():
	namePattern = re.compile("h5")
	nameTag = soup.find_all(namePattern)
	nameList = []
	for name in nameTag:
		name = str(name)
		name = name.lstrip('<h5 class="title"><span id="order_item_1234567890_title">').rstrip('</span></h5>')
		nameList.append(name)
	return nameList

def getSKU():
	skuList = []
	skuTag = soup.find_all(text = re.compile('\d{7,8}|U\d{6,7}'))
	for sku in skuTag:
		try:
			sku = str(sku).strip()
			if re.match('^\d{7,8}$|^U\d{6,7}$', sku):
				skuList.append(sku)
		except:
			continue
	return skuList

def getPrice(number):
	priceTag = soup.find_all('span', 'price')
	priceList = []

	for i in range(0,number):
		i = 1 + i * 5
		price = priceTag[i]
		price = str(price).lstrip('<span class="price">$ ').rstrip('</span>')
		priceList.append(price)
	return priceList

def getQuantity():
	quantityTag = soup.find_all('td', 'a-center')
	quantityList = []
	for quantity in quantityTag:
		quantity = str(quantity).lstrip('<td class="a-center">').rstrip('</td>')
		quantityList.append(quantity)
	return quantityList
	


if __name__ == '__main__':
	main()
