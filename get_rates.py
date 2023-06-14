#! /usr/bin/env python3

import xml.etree.ElementTree as ET
import urllib.request

from prettytable import PrettyTable

# get the file from CS
with urllib.request.urlopen('https://www.credit-suisse.com/media/tetris-assets/calculators-excel/iPRICE_dailyRates.xml') as f:
    rates = f.read()

root = ET.fromstring(rates, parser=ET.XMLParser(encoding='latin-1'))


# initialize a table
t = PrettyTable(['Years', 'Price'])

for product in root.findall('./*[@code="0011"]/productGroup/currency/product'):

    # select only standard product
    if product.find('code').text == "00538":
        for pricing in product.findall('pricing'):
            years = pricing.find('term').text
            price = pricing.find('price').text

            # limit output to a few years
            if years in ['2', '3', '5', '10']:
                t.add_row([years, price])
                # print("{}, {}".format(years, price))

print(t)