#!/usr/bin/python
#-*- coding: utf-8 -*-

i=0
j=1

n=int(input("输入个数："))
k=0

while k<int(n) :
    print(i)
    s=i+j
    i=j
    j=s
    k+=1



