import random
import csv
from csvwrite import write
 
random_x = 0.015
random_golden = 0.055
random_purple = 0.23
random_blue = 0.7

def random_table(color):
  if color == 'x':
    return random_x*1000
  elif color == 'golden':
    return (random_x+random_golden)*1000
  elif color == 'purple':
    return (random_x+random_golden+random_purple)*1000
  elif color == 'blue':
    return (random_x+random_golden+random_purple+random_blue)*1000

def random_var():
  return ("機率表:\nX機率:{}\n金卡機率:{}\n紫卡機率:{}\n藍卡機率:{}".format(random_x,random_golden,random_purple,random_blue))

def record(event,nox):
  ID = event.source.user_id
  raw = [[0]*5 for i in range(100)]
  i = 0
  new_member = 1
  promise = 0 
  with open('card.csv', newline='') as csvfile: 
    rows = csv.DictReader(csvfile)
    for row in rows:
      a = int(row['抽卡次數'])
      b = int(row['總抽卡數'])
      c = int(row['抽中次數'])
      name = row['註冊暱稱']
      if row['UID'] == '0':
        break
      if row['UID'] == ID:
        new_member = 0
        if nox == 1:
          a += 1
          if a > 100: 
            promise = 1
            a = 0
            c += 1
        else: 
          a = 0 
          c += 1 
        raw[i] = [row['UID'],a,b+1,c,name] 
      else:
        raw[i] = [row['UID'],a,b,c,name] 
      i = i + 1
    if new_member == 1:
      raw[i] = [ID,1,1,0,'空暱稱']
  write (raw)
  return promise 

def single_card(event):
  flag = random.randint(0, 1000)
  if flag % 1000 < random_table('x'):
    result = xpool()
  elif flag % 1000 < random_table('golden'):
    result = '普金'
  elif flag % 1000 < random_table('purple'):
    result = '紫卡'
  elif flag % 1000 < random_table('blue'):
    result = '藍卡'
  else:
    result = '綠卡'
  if flag > random_table('x'):
    nox = 1
  else : 
    nox = 0 
  if record(event,nox) == 1 :
    return '保底'
  else :
    return result

def multi_card(event):
  multi_result = ''
  for i in range(11):
    multi_result += single_card(event) + ', '
  return multi_result


def xpool():
  flag = random.randint(0, 1000)
  if flag % 1000%20 == 1:
    result = '神風'
  elif flag % 1000%20 == 2:
    result = '暴怒'
  elif flag % 1000%20 == 3:
    result = '不死'
  elif flag % 1000%20 == 4:
    result = '鋼鐵'
  elif flag % 1000%20 == 5:
    result = '漫遊'
  elif flag % 1000%20 == 6:
    result = '爆食'
  elif flag % 1000%20 == 7:
    result = '汽修'
  elif flag % 1000%20 == 8:
    result = '紅帽'
  elif flag % 1000%20 == 9:
    result = '獨狼'
  elif flag % 1000%20 == 10:
    result = '瓦爾'
  elif flag % 1000%20 == 11:
    result = '玫瑰'
  elif flag % 1000%20 == 12:
    result = '修女'
  elif flag % 1000%20 == 13:
    result = '死騎'
  elif flag % 1000%20 == 14:
    result = '阿堆'
  elif flag % 1000%20 == 15:
    result = '愛國'
  elif flag % 1000%20 == 16:
    result = '追蹤'
  elif flag % 1000%20 == 17:
    result = '天國'
  elif flag % 1000%20 == 18:
    result = '遊牧'
  elif flag % 1000%20 == 19:
    result = '猛漢'
  elif flag % 1000%20 == 0:
    result = '斯溫'
  return result
