import random
import csv
from csvwrite import write
 
random_x = 0.015
random_golden = 0.055
random_purple = 0.23
random_blue = 0.7
s1 = ['龍怒','鷹眼','狂蟒','昨日','聖君','閃靈','勇者','禁衛','獵鷹']
s2 = ['子爵','騎士','審判','執行','上尉','獵豹']
s3 = ['祭司','自由','少校','先驅','遠視','喪鐘']
s4 = ['主宰','毒行','天降','政委','蜂鳥','凱薩']
x1 = ['玫瑰','遊牧','猛漢','愛國','鋼鐵','器修','不死','紅帽','漫遊','追蹤']
x2 = ['爆食','修女','天國','阿堆','斯溫','莫離','獨狼','死騎','神風','暴怒']


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
  if 's1' in event.message.text:
     return goldpool(s1)
  elif 's2' in event.message.text:
     return goldpool(s2)
  elif 's3' in event.message.text:
     return goldpool(s3)
  elif 's4' in event.message.text:
     return goldpool(s4)
  elif 'x1' in event.message.text:
     return goldpool(x1)
  elif 'x2' in event.message.text:
     return goldpool(x2)

  if flag % 1000 < random_table('x'):
    result = goldpool(x1+x2)
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
 
def goldpool(pool):
  pool_size = len(pool)
  flag = random.randint(0, 1000)
  return pool[flag%pool_size]


if __name__ == '__main__':
  goldpool(x1+x2)
