#!/usr/bin/env python3
# coding=utf8

def table(type,level):
  if type == "土地榮譽":
    if level == 0:
      return 0
    elif level == 1:
      return 0.03
    elif level == 2:
      return 0.06
    elif level == 3:
      return 0.09
    elif level == 4:
      return 0.12
    elif level == 5:
      return 0.15
    elif level == 6:
      return 0.18
    elif level == 7:
      return 0.21
    elif level == 8:
      return 0.24
    elif level == 9:
      return 0.27
    elif level == 10:
      return 0.27
    elif level == 11:
      return 0.27
    elif level == 12:
      return 0.27
    elif level == 13:
      return 0.27
    elif level == 14:
      return 0.27
    elif level == 15:
      return 0.30
    elif level == 16:
      return 0.33
    elif level == 17:
      return 0.36
    elif level == 18:
      return 0.36
    elif level == 19:
      return 0.36
    elif level == 20:
      return 0.36
    elif level == 21:
      return 0.36
    elif level == 22:
      return 0.36
    elif level == 23:
      return 0.39
    elif level == 24:
      return 0.42
    elif level == 25:
      return 0.45
    elif level == 26:
      return 0.48
    elif level == 27:
      return 0.51
    elif level == 28:
      return 0.54
    elif level == 29:
      return 0.57
    elif level == 30:
      return 0.60
    elif level == 31:
      return 0.63
    elif level == 32:
      return 0.66
    elif level == 33:
      return 0.69
    elif level == 34:
      return 0.72
    elif level == 35:
      return 0.75
    elif level == 36:
      return 0.78
    elif level == 37:
      return 0.81
    elif level == 38:
      return 0.84
    elif level == 39:
      return 0.87
    elif level == 40:
      return 0.90      
  elif type == "抗毒":
    if level <= 9:
      return 0
    elif level == 10:
      return 69
    elif level == 11:
      return 120
    elif level == 12:
      return 180
    elif level == 13:
      return 240
    elif level <= 20:
      return 300
    elif level == 21:
      return 360
    elif level == 22:
      return 420
    elif level == 23:
      return 480
    elif level == 24:
      return 540
    elif level <= 31:
      return 600
    elif level == 32:
      return 660
    elif level == 33:
      return 720
    elif level == 34:
      return 780
    elif level == 35:
      return 840
    elif level <= 42:
      return 900
    elif level == 43:
      return 960
    elif level == 44:
      return 1020
    elif level == 45:
      return 1080
    elif level == 46:
      return 1140
    elif level == 47:
      return 1200
  elif type == "建材提升":
    if level == 0:
      return 0
    elif level == 1:
      return 0.
    elif level == 2:
      return 0
    elif level == 3:
      return 0
    elif level == 4:
      return 0.02
    elif level == 5:
      return 0.04
    elif level == 6:
      return 0.06
    elif level == 7:
      return 0.08
    elif level == 8:
      return 0.10
    elif level == 9:
      return 0.12
    elif level == 10:
      return 0.12
    elif level == 11:
      return 0.12
    elif level == 12:
      return 0.12
    elif level == 13:
      return 0.12
    elif level == 14:
      return 0.12
    elif level == 15:
      return 0.14
    elif level == 16:
      return 0.16
    elif level == 17:
      return 0.18
  elif type == "土地經驗":
    if level == 12:
      return 12912
    elif level == 13:
      return 13720
    elif level == 14:
      return 14530
    elif level == 15:
      return 15340
    elif level == 16:
      return 16200
  elif type == "榮譽頒發":
    if level == 0:
      return 0
    elif level == 1:
      return 600000

  
