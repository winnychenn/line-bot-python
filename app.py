#!/usr/bin/env python3
# coding=utf8

import datetime 
import requests
from table import table
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

def Tile_Level(Ori_poison,b):
  if Ori_poison+b >=8000:
    return 16
  elif Ori_poison+b >= 7200:
    return 15
  elif Ori_poison+b >= 6400:
    return 14
  elif Ori_poison+b >= 5600:
    return 13
  elif Ori_poison+b >= 4800:
    return 12
  else:
    return 1

def flush_tile(event):
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='例行刷專精時間 早上9點20分:夏，中午3點30分:糖，晚上10點20:可愛\n 刷到本週結束 下週一開始都去解任務')
  )
  return ''

def manual(event):
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='專精點數:{} 原始抗毒:{} 現在建材產量:{} 城市增益:{} 建材綠上:{} ＠test123')
  )
  return ''

def text_split(str0,strx):
  length = len(str0)
  try:
    Location = str0.index(strx)
    for i in range(7):
      String = str0[Location+5:Location+i+5]
      temp = str0[Location+i+4]
      if Location+i+5 >=length or str0[Location+i+5] == " " or str0[Location+i+5] == "%":
        break
    print(String)
  except:
    String = 0
    print("error:{}".format(String))
  return String


@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
  str0 = event.message.text
  print(str0, file=sys.stderr)
  str1 = ["專精點數", "原始抗毒", "建材產量", "建材綠上", "城市增益"]
  strn = "test123"
  strh = "列舉指令"
  str2 = ["刷專精時間", "專精參數說明", "抽籤"]
  temp = ""
  echo = ""
  #if event.source.user_id == "Ueba67a4e14e3e486096171cc12900a81":
  #  echo = event.message.text
  #  line_bot_api.reply_message(event.reply_token,TextSendMessage(text= "羽靈echo:"+echo))
  #print(event.source.user_id,echo)
  if str2[0] in str0:
    flush_tile(event)
  elif str2[1] in str0:
    manual(event)
  elif strh in str0:
    for i in range(len ( str2 ) ):
      temp = temp + str2[i] + '\n'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= temp ))
  try:
    test = event.source.group_id
    try:
      test = str0.index(strn)
    except:
      return ''
  except:
    test = ''
  if str2[2] in str0:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text= lottery(str0)))
    return ''
  
  Land_investment = 0.2
  Exp_card = 1
  Attack_times = 240
  Point = int(text_split(str0,str1[0]))
  Ori_poison = int(text_split(str0,str1[1]))
  Material_per_hour = int(text_split(str0,str1[2]))
  Material_18_point = int(text_split(str0,str1[3]))
  City_bonus = float(text_split(str0,str1[4]))/100
  Ori_Material_product_per_hour = Material_per_hour / (1+City_bonus+table('建材提升',Material_18_point))
  Material_for_exp_per_day = 0
  Max_exp = 0
  Max_Land_investment = 0
  Max_Poison = 0
  Max_Land_level = 0 
  Max_material_point = 0
  Max_Honor_award_point = 0
  if(Point == 0):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='專精輸入有錯 預設0點專精 你還是洗洗睡吧')) 
    return ''
  for x in range(41):
    Land_honor_point = table('土地榮譽',x)
    for y in range(48):
      Land_level = Tile_Level(Ori_poison,table('抗毒',y))
      if Land_level == 1 : 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='fuck! 沒抗毒12都吃不了，你還是吃屎吧。別來鬧！'))
        return ''
      Land_exp = table('土地經驗',Land_level)*(1+Land_investment+Exp_card+Land_honor_point)*Attack_times
      if x+y > Point:
        break
      for z in range(18):
        Material_for_exp_per_day = Ori_Material_product_per_hour * (table('建材提升',z)) * 0.68 *24
        if x+y+z > Point:
          break
        for a in range(2):
          Honor_award = table('榮譽頒發',a)
          if x+y+z+a*22 > Point:
            break
          if Max_exp < Land_exp + Material_for_exp_per_day + Honor_award :
            Max_exp = Land_exp + Material_for_exp_per_day + Honor_award
            Max_Land_investment = x
            Max_Poison = y
            Max_Land_level = Land_level
            Max_material_point = z
            Max_Honor_award_point = 22
          
  now = a=datetime.datetime.now()
  end = datetime.datetime(2020, 11, 9, 10, 00, 0, 0)
  remain_hours=(end-now).days*24+int((end-now).seconds/3600)
  New_Material_per_hour=int (Ori_Material_product_per_hour * (1+table('建材提升',Max_material_point)+City_bonus) )
  text1 = ('🌝 專精點數:{} 原始抗毒:{} 建材原本產量:{} 城市增益:{}% \n更新點數後'.format(Point,Ori_poison,Material_per_hour,City_bonus*100))  
  text2 = ('🌚 建材時產量:{},建材日產量:{},\n伊甸結束前可以獲得的建材量:{}'.format(New_Material_per_hour,New_Material_per_hour*24,remain_hours*New_Material_per_hour)) 
  text3 = ('🆗  每日刷滿3條耐久共240次,加上經驗加倍卡,刷地土地等級:{},最大專精量:{}'.format(Max_Land_level,int(Max_exp)))
  if Max_Honor_award_point == 22:
    text4 = ('🍗  建材日產量轉換大興土木經驗:{},榮譽頒發經驗:{}'.format(int(New_Material_per_hour*24*0.68),Honor_award))
    text5 = ('🔑 建材18%點數{}, 土地榮譽點數:{}, 抗毒點數:{},榮譽頒發:22, 剩餘點數:{}'.format(Max_material_point,Max_Land_investment,Max_Poison,Point-Max_material_point-Max_Land_investment-Max_Poison-Max_Honor_award_point))
  else:
    text4 = ('🍗 建材日產量轉換大興土木經驗:{}'.format(int(New_Material_per_hour*24*0.68))) 
    text5 = ('🔑 建材18%點數:{}, 土地榮譽點數:{},抗毒點數:{}, 剩餘點數:{}'.format(Max_material_point,Max_Land_investment,Max_Poison,Point-Max_material_point-Max_Land_investment-Max_Poison))
  text6 = ('🚫 投資理財 有賺有賠 使用前請詳閱公開說明書')
 

  print(text1) 
  print(text2)
  print(text3)
  print(text4)
  print(text5)
  line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text1+"\n----------------------------\n"+text2+"\n----------------------------\n"+text3+"\n----------------------------\n"+text4+"\n----------------------------\n"+text5+"\n----------------------------\n\n"+text6))     
 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=6000)
   








