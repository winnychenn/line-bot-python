import random
def lottery(str0):
  flag = random.randint(0, 100)
  if "會不會" in str0:
    if flag % 2 == 0:
      result = '會'
    elif flag % 2 == 1:
      result = '不會'
  elif "是不是" in str0:
    if flag % 2 == 0:
      result = '是'
    elif flag % 2 == 1:
      result = '不是'
  else:
    if flag % 5 == 0:
      result = '大吉'
    elif flag % 5 == 1:
      result = '小吉'
    elif flag % 5 == 2:
      result = '中'
    elif flag % 5 == 3:
      result = '下'
    elif flag % 5 == 4:
      result = '下下'

  return result
