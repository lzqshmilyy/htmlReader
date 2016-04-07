#!/usr/bin/python
#_*_coding:utf-8 -*-

from bs4 import *
import re

def main():
	soup = BeautifulSoup(open("1.html"), "lxml")
	nameTag = soup.find_all(re.compile("h5"))
	skuTag = soup.find_all(re.compile("strong"))
	for txt in skuTag:
		print txt

def getName(tag):
	name = []
	for text in tag:
		txt = str(text)
		txt = txt.lstrip('<h5 class="title"><span id="order_item_1234567890_title">').rstrip('</span></h5>')
		name.append(txt)

	for string in name:
		print string


if __name__ == '__main__':
	main()