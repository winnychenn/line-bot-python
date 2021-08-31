#!/usr/bin/env python3
# coding=utf8

import random
def stone(player):
    if player == "":
        return "你要先出拳"
    if player!="石頭" and player!="布" and player!="剪刀":
        return "你會不會玩？出什麼鬼？" 
    computer = random.randint(0,2)
    if computer == 0:
        computer = "石頭"
    elif computer == 1:
        computer = "布"
    else:
        computer = "剪刀"
    if (player == "石頭" and computer == "剪刀") or (player == "布" and computer == "石頭") or (player  == "剪刀" and computer == "布"):
        return "電腦出{},你贏電腦了".format(computer)
    elif (player == computer):
        return "電腦出{},平手".format(computer)
    else:
        return "電腦出{},你這爛咖".format(computer)


if __name__ == '__main__':
    print(stone("石頭"))
