import csv

def write(raw):
  with open('card.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入一列資料
    writer.writerow(['UID', '抽卡次數', '總抽卡數'])

    # 寫入另外幾列資料
    for i  in range(10):
      writer.writerow(raw[i])
