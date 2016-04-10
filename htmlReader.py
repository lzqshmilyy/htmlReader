#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import re
import csv
import os

def main():
	nameList = os.listdir('/Users/Isaac/Documents/Python/htmlReader/html')
	for fileName in nameList:
		writeCSV('/Users/Isaac/Documents/Python/htmlReader/html/' + fileName)

def writeCSV(fileName):
	global soup
	#open the html file and get the product information 
	soup = BeautifulSoup(open(fileName), "lxml")
	
	nameList = getName()
	number = len(nameList)
	skuList = getSKU()
	priceList = getPrice(number)
	quantityList = getQuantity()
	date = fileName.rstrip('.html').lstrip('Users/Isaac/Documents/Python/htmlReader/html/')

	#oprn the csv file and write the information into csv
	csvfile = open('sales.csv', 'a+')
	csvfile.write('\xEF\xBB\xBF') #add BOM to the file, then it will show chinese in excel
	writer = csv.writer(csvfile)

	writer.writerow(['Date','Name', 'SKU', 'Price', 'Quantity'])

	data = []
	for i in range(0, number):
		line = [date, nameList[i], skuList[i], priceList[i], quantityList[i]]
		data.append(line)

	emptyline = []
	data.append(emptyline)

	writer.writerows(data)

	csvfile.close()



def getName():
	nameList = []
	for name in soup.find_all('h5'):
		nameList.append(name.string.encode('UTF_8', 'replace'))
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
