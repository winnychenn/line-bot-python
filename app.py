#!/usr/bin/env python3
# coding=utf8

import requests
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
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
app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
  print("test111", file=sys.stderr)
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
  line_bot_api.reply_message(
    event.reply_token,
    #TextSendMessage(text='例行刷專精時間 早上10點45分:夏，下午5點00分:糖，晚上12點00分:可愛\n 刷到本週結束 下週一開始都去解任務')
    TextSendMessage(text='請去解任務  感恩～')
  )
  return ''




@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
  str0 = event.message.text
  print(str0, file=sys.stderr)
  str1 = ["專精點數", "原始抗毒", "建材產量", "建材綠上", "城市增益"]
  strn = "test123"
  strh = "列舉指令"
  str2 = ["刷專精時間", "專精參數說明", "抽籤", "抽卡", "十連抽", "油價", "註冊暱稱", "查詢資料", "卡池機率"]
  temp = ""
  echo = ""
  #if event.source.user_id == "Ueba67a4e14e3e486096171cc12900a81":
  #  echo = event.message.text
  #  line_bot_api.reply_message(event.reply_token,TextSendMessage(text= "羽靈echo:"+echo))
  #print(event.source.user_id,echo)
  if str2[0] in str0:
    flush_tile(event)
  elif str2[1] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = manual(event) ))
  elif strh in str0:
    for i in range(len ( str2 ) ):
      temp = temp + str2[i] + '\n'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= temp ))
  try:
    test = event.source.group_id
    if test == 'C603fb2aaf553d5bef57c2e8e467b1311':
      return ''
    try:
      test = str0.index(strn)
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
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= register(event.source.user_id,event.message.text.strip('@test123'+' '+str2[6]+' ')) ))
  elif str2[7] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = showdata(event.source.user_id) )) 
  elif str2[8] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text = random_var() ))
  else:  
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= calculator(event,str0)))
 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=6000)
   








