#!/usr/bin/env python3
# coding=utf8

from table import table
import datetime

str1 = ["專精點數", "原始抗毒", "建材產量", "建材綠上", "城市增益", "戰旗數量"]

def manual(event):
  text = ""
  for i in range(len(str1)):
    text += str1[i] + ':{} '
  text += '@test123 \n'
  text += '(P.S: 專精點數不可以是0 建材綠上是綠專精增加建材點數 城市增益 建材產量預設都是0  戰旗數量 預設是3)'
  return text

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

def calculator(event,str0):
  Land_investment = 0.2                                 #土地投資
  Exp_card = 1                                          #經驗加倍卡   
  Point = int(text_split(str0,str1[0]))                 #專精點數
  Ori_poison = int(text_split(str0,str1[1]))            #原始抗毒
  Material_per_hour = int(text_split(str0,str1[2]))     #原始產量/小時
  Material_18_point = int(text_split(str0,str1[3]))     #綠上增加建材點數
  City_bonus = float(text_split(str0,str1[4]))/100      #城市加成
  Flag = int(text_split(str0,str1[5]))                  #戰旗數量
  if Flag == 0 :
    Flag = 3
  Attack_times = Flag*80                                #攻擊次數= 戰旗數量*80
  Ori_Material_product_per_hour = Material_per_hour / (1+City_bonus+table('建材提升',Material_18_point))
  Material_for_exp_per_day = 0
  Max_exp = 0
  Max_Land_investment = 0
  Max_Poison = 0
  Max_Land_level = 0
  Max_material_point = 0
  Max_Honor_award_point = 0
  Max_Land_exp = 0 
  if(Point == 0):
    return '專精輸入有錯 預設0點專精 你還是洗洗睡吧'
  for x in range(41):
    Land_honor_point = table('土地榮譽',x)
    for y in range(48):
      Land_level = Tile_Level(Ori_poison,table('抗毒',y))
      if Land_level == 1 :
        return 'fuck! 沒抗毒12都吃不了，你還是吃屎吧。別來鬧！'
      Land_exp = table('土地經驗',Land_level)*(1+Land_investment+Exp_card+Land_honor_point)*Attack_times
      if x+y > Point:
        break
      for z in range(18):
        Material_for_exp_per_day = Ori_Material_product_per_hour * (1+City_bonus+table('建材提升',z)) * 0.68 *24
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
            Max_Honor_award_point = a*22
            Max_Land_exp = Land_exp

  now = a=datetime.datetime.now()
  end = datetime.datetime(2020, 11, 9, 10, 00, 0, 0)
  remain_hours=(end-now).days*24+int((end-now).seconds/3600)
  New_Material_per_hour=int (Ori_Material_product_per_hour * (1+table('建材提升',Max_material_point)+City_bonus) )
  text1 = ('🌝 專精點數:{} 原始抗毒:{} 原始建材產量:{} 城市增益:{:.1f}% 戰旗數量:{} \n更新點數後'.format(Point,Ori_poison,Material_per_hour,City_bonus*100,Flag))
  text2 = ('🌚 建材時產量:{},建材日產量:{},\n伊甸結束前可以獲得的建材量:{}'.format(New_Material_per_hour,New_Material_per_hour*24,remain_hours*New_Material_per_hour))
  text3 = ('🆗  每日刷滿{}戰旗共{}次,加上經驗加倍卡,刷地土地等級:{},最大專精量:{}'.format(Flag,Attack_times,Max_Land_level,int(Land_exp)))
  if Max_Honor_award_point == 22:
    text4 = ('🍗 建材日產量轉換大興土木經驗:{},榮譽頒發經驗:{}'.format(int(New_Material_per_hour*24*0.68),Honor_award))
    text5 = ('🔑 建材18%點數{}, 土地榮譽點數:{}, 抗毒點數:{},榮譽頒發:22, 剩餘點數:{}'.format(Max_material_point,Max_Land_investment,Max_Poison,Point-Max_material_point-Max_Land_investment-Max_Poison-Max_Honor_award_point))
  else:
    text4 = ('🍗 建材日產量轉換大興土木經驗:{}'.format(int(New_Material_per_hour*24*0.68)))
    text5 = ('🔑 建材18%點數:{}, 土地榮譽點數:{},抗毒點數:{}, 剩餘點數:{}'.format(Max_material_point,Max_Land_investment,Max_Poison,Point-Max_material_point-Max_Land_investment-Max_Poison))
  text6 = ('每日最大專精量:{}'.format(int(Max_exp)))
  text7 = ('🚫 投資理財 有賺有賠 使用前請詳閱公開說明書')
   

  print(text1)
  print(text2)
  print(text3)
  print(text4)
  print(text5)
  
  return text1+"\n----------------------------\n"+text2+"\n----------------------------\n"+text3+"\n----------------------------\n"+text4+"\n----------------------------\n"+text5+"\n----------------------------\n"+text6+"\n----------------------------\n\n"+text7


