# -*- coding: UTF-8 -*-
'''
@Project ：catchstudy 
@File ：hdg_1.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-05-26 오후 1:40
'''
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

result = 0
cnt = 0

for i in arr:
    cnt += 1
    if cnt >= i:
        result +=1
        cnt = 0

print(result)