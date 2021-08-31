#!/usr/bin/env python3
# coding=utf8

import requests
import json

def get(city):
    token = 'CWB-C6395F88-EDA2-4018-9EFC-968C2B318CC3' 
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=' + token + '&format=JSON&locationName=' + str(city)
    Data = requests.get(url)
    Data = (json.loads(Data.text,encoding='utf-8'))['records']['location'][0]['weatherElement']
    res = [[] , [] , []]
    text = ""
    for j in range(3):
        for i in Data:
            res[j].append(i['time'][j])
    for data in res:
        text += '{} ~ {}\n'.format(res[0][0]['startTime'][5:-3],res[0][0]['endTime'][5:-3])
        text += '天氣狀況 {}\n溫度 {} ~ {} °C\n降雨機率 {}\n'.format(data[0]['parameter']['parameterName'],data[2]['parameter']['parameterName'],data[4]['parameter']['parameterName'],data[1]['parameter']['parameterName'])
        
    return text


if __name__ == '__main__':
  print(get("新竹市"))
