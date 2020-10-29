import random
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
  return result

def multi_card(event):
  flag = random.randint(0, 1000)
  multi_result = ''
  for i in range(11):
    multi_result += single_card(event) + ', '
  return multi_result
