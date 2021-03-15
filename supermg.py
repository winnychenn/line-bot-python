#!/usr/bin/env python3
# coding=utf8
import configparser
config = configparser.ConfigParser()

# 讀取 INI 設定檔
config.read('config.ini')

def write_doc(string,string2,string3):
  config[string2][string] = string3
  with open('config.ini', 'w') as configfile:
    config.write(configfile)

def read_doc(string,string2):
  txt = config[string][string2]
  return txt 

def test():
  config['super-manager']['strsuper']= '設定戰旗時間,test'
  txt = config['super-manager']['strsuper']
  print(txt)
  return txt


if __name__ == '__main__':
  test()
