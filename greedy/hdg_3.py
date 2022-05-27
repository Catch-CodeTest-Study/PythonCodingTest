# -*- coding: UTF-8 -*-
'''
@Project ：catchstudy 
@File ：hdg_3.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-05-27 오후 7:20 
'''
import itertools
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] != arr[j]:
            cnt +=1

print(cnt)
