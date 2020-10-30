#!/usr/bin/env python3
# coding=utf8

from urllib.request import urlopen
from xml.etree.ElementTree import parse

def oil():
  u = urlopen('https://vipmember.tmtd.cpc.com.tw/opendata/ListPriceWebService.asmx/getCPCMainProdListPrice_XML')
  doc = parse(u)
 
  oil_product = ['98無鉛汽油', '95無鉛汽油', '92無鉛汽油']
  text = ''
  for item in doc.iterfind('Table'):
    product = item.findtext('產品名稱')
    if product in oil_product: 
      price = item.findtext('參考牌價')
      text += ('{}:{}元/公升\n'.format(product,price))
 
  print(text)
  return text

