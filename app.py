#!/usr/bin/env python3
# coding=utf8

import requests
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, CarouselTemplate, CarouselColumn, URIAction
from argparse import ArgumentParser
#from __future__ import unicode_literals
import os
import configparser
import sys
import random
from lottery import lottery
from specialization import calculator, manual
from card import single_card, multi_card, random_var
from oil import oil
from csvwrite import register, showdata
from supermg import write_doc, read_doc
from weather import get
from stone import stone
app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

SUPER_MANAGER=['U6b5b5168c4a6ad4cab5026788dc1a612']
cities = ['基隆市','嘉義市','臺北市','嘉義縣','新北市','臺南市','桃園縣','高雄市','新竹市','屏東縣','新竹縣','臺東縣','苗栗縣','花蓮縣','臺中市','宜蘭縣','彰化縣','澎湖縣','南投縣','金門縣','雲林縣','連江縣']

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
  #print("test111", file=sys.stderr)
  signature = request.headers['X-Line-Signature']

  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)
         
  try:
    print(body, signature)
    handler.handle(body, signature)
                                            
  except InvalidSignatureError:
    abort(400)

  return 'OK'

def flush_tile(event):
  flush_tile_text=read_doc('super-manager','設定戰旗時間')
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text="戰旗時間為: "+flush_tile_text)
  )




@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
  str0 = event.message.text
  print(event, file=sys.stderr)
  print(str0, file=sys.stderr)
  str1 = ["專精點數", "原始抗毒", "建材產量", "建材綠上", "城市增益"]
  strn = "瑪莎拉蒂"
  strh = "列舉指令"
  str2 = ["刷專精時間", "專精參數說明", "抽籤", "抽卡", "十連抽", "油價", "註冊暱稱", "查詢資料", "卡池機率", "天氣","猜拳"]
  strcard = "抽卡說明"
  strsuper = ["設定戰旗時間"]
  temp = ""
  echo = ""
  #if event.source.user_id == "U6b5b5168c4a6ad4cab5026788dc1a612":
  #  line_bot_api.reply_message(event.reply_token,TextSendMessage(text= "@U6b5b5168c4a6ad4cab5026788dc1a612"))
  if event.source.user_id in SUPER_MANAGER:
  # super manager
    if strsuper[0] in str0:
      write_doc(strsuper[0],'super-manager',str0.strip(strsuper[0]+' '))
      flush_tile(event)
      return ''
  if str2[0] in str0:
    flush_tile(event)
  elif str2[1] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = manual(event) ))
  elif strh in str0:
    for i in range(len ( str2 ) ):
      temp = temp + str2[i] + '\n'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= temp+strcard ))
  elif strcard in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "賽季獎勵 (不累積資料) \n@test123  抽卡 指定池\n金卡池 (累積資料)\n＠test123 抽卡\n＠test123 十連抽\n先抽卡後可以註冊,註冊後可以註冊暱稱\n" ))
  try:
    test = event.source.group_id
    if test == 'C603fb2aaf553d5bef57c2e8e467b1311':
      print(test, file=sys.stderr)
#      return ''
    try:
      test = str0.index("@"+strn)
    except:
      return ''
  except:
    test = ''
  if str2[2] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= lottery(str0)))
  elif str2[3] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = single_card(event) ))
  elif str2[4] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = multi_card(event) ))
  elif str2[5] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = oil() ))
  elif str2[6] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= register(event.source.user_id,event.message.text.strip(strn+' '+str2[6]+' ')) ))
  elif str2[7] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = showdata(event.source.user_id) )) 
  elif str2[8] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = random_var() ))
  elif str2[9] in str0:
    city=str0.replace(str2[9],"").replace(" ","").replace('台','臺').replace('@瑪莎拉蒂',"")
    if(not (city in cities)):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="查詢格式為: 天氣 縣市,不要亂打")) 
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get(city)))
  elif str2[10] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=stone(str0.replace(str2[10],"").replace(" ","").replace('@瑪莎拉蒂',""))))
  else:  
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= calculator(event,str0)))
 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=6000)








