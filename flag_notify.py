#!/usr/bin/env python3
# coding=utf8
import configparser
import datetime
import requests
import schedule
import time
from table import table

token = 'N2t8a0XQS43ps1MpWEdIfBU3qyUlza1w5JZ9krk7lMb'
token2 = 'eD0kajWXCsWf7FOWgfbxGJB8b93nZAEp1VMD5VFHv9I'

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    print(msg)
    return r.status_code

    

while True:
    config = configparser.ConfigParser()
    config.read('config.ini')
    timestamp=config.get('super-manager', '設定戰旗時間').split(',')  
    gbxtime=config.get('super-manager', 'GBX戰旗時間').split(',')
    timestamp44a=config.get('super-manager', '44a戰旗時間').split(',')
    x=datetime.datetime.now() + datetime.timedelta(hours = +8)
    for i in timestamp:
        now = str(x.hour)+":"+str(x.minute)
        if now in i:
            if x.second <1:
                lineNotifyMessage(token,'cnm刷戰旗時間')
    for i in timestamp44a:
        now = str(x.hour)+":"+str(x.minute)
        if now in i:
            if x.second <1:
                lineNotifyMessage(token,'44a刷戰旗時間')
    for i in gbxtime:
        now = str(x.hour)+":"+str(x.minute)
        if now in i:
            if x.second <1:
                lineNotifyMessage(token2,'GBX戰旗時間')
    time.sleep(1)

