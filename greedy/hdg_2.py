# -*- coding: UTF-8 -*-
'''
@Project ：catchstudy 
@File ：hdg_2.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-05-27 오후 7:06 
'''
import sys

s = sys.stdin.readline()

cnt_zero = 0
cnt_one = 0


for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            cnt_zero +=1
        else:
            cnt_one +=1

if s[-1] != s[-2]:
    if s[-2] == '0':
        cnt_zero +=1
    else:
        cnt_one +=1


print(min(cnt_zero, cnt_one))