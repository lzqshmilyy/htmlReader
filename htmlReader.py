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
	nameList = []
	for name in soup.find_all('h5'):
		nameList.append(name.string)
	return nameList

def getSKU():
	skuList = []
	for sku in soup.select('td div strong'):
			skuList.append(sku.next_sibling)
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
	quantityList = []
	for quantity in soup.find_all('td', 'a-center'):
		quantityList.append(quantity.string)
	return quantityList
	


if __name__ == '__main__':
	main()
