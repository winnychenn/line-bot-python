import csv

def write(raw):
  with open('card.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入一列資料
    writer.writerow(['UID', '抽卡次數', '總抽卡數', '抽中次數', '註冊暱稱'])

    # 寫入另外幾列資料
    for i  in range(100):
      writer.writerow(raw[i])


def register(uid,name):
  raw = [[0]*5 for i in range(100)]
  with open('card.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    i = 0
    success = 0 
    for row in rows:
      if row['UID'] == uid:
        raw[i] = [row['UID'],row['抽卡次數'],row['總抽卡數'],row['抽中次數'],name]
        success = 1
      else :
        raw[i] = [row['UID'],row['抽卡次數'],row['總抽卡數'],row['抽中次數'],row['註冊暱稱']]
      i = i + 1
    write (raw)
  if success == 1:
    return ('成功註冊名稱為:{}'.format(name))
  else :
    return ('註冊失敗,找不到您的資料')

def showdata(uid):
  raw = [[0]*5 for i in range(100)]
  with open('card.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    i = 0
    for row in rows:
      if row['UID'] == uid:
        text =  ("暱稱:{}\n".format(row['註冊暱稱']))
        text += ("抽卡次數:{},總抽卡數:{},抽中次數:{}".format(row['抽卡次數'],row['總抽卡數'],row['抽中次數']))
        return text
    return "查無資料"
  
