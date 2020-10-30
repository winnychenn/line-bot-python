import random
import csv
from csvwrite import write

def record(event,nox):
  ID = event.source.user_id
  raw = [[0]*3 for i in range(10)]
  i = 0
  new_member = 1
  promise = 0 
  with open('card.csv', newline='') as csvfile: 
    rows = csv.DictReader(csvfile)
    for row in rows:
      a = int(row['抽卡次數'])
      b = int(row['總抽卡數'])
      if row['UID'] == '0':
        break
      if row['UID'] == ID:
        new_member = 0
        if nox == 1:
          a += 1
          if a > 100: 
            promise = 1
            a = 0
        else: 
          a = 0 
        raw[i] = [row['UID'],a,b+1] 
      else:
        raw[i] = [row['UID'],a,b] 
      i = i + 1
    if new_member == 1:
      raw[i] = [ID,1,1]
  write (raw)
  return promise 
def single_card(event):
  flag = random.randint(0, 1000)
  if flag % 1000 < 3:
    result = '神風'
  elif flag % 1000 < 6:
    result = '暴怒'
  elif flag % 1000 < 9:
    result = '不死'
  elif flag % 1000 < 12:
    result = '鋼鐵'
  elif flag % 1000 < 15:
    result = '漫遊'
  elif flag % 1000 < 50:
    result = '普金'
  elif flag % 1000 < 150:
    result = '紫卡'
  elif flag % 1000 < 500:
    result = '藍卡'
  else:
    result = '綠卡'
  if flag > 15:
    nox = 1
  else : 
    nox = 0 
  if record(event,nox) == 1 :
    return '保底'
  else :
    return result

def multi_card(event):
  flag = random.randint(0, 1000)
  multi_result = ''
  for i in range(11):
    multi_result += single_card(event) + ', '
  return multi_result

