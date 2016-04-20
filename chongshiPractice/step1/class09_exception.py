#!/usr/bin/python 
#-*- coding:utf-8 -*-
#class 9:异常练习

import exceptions

#test1
print "test1:"
print "="*30
try:
    x=input("输入被除数:")
    y=input("输入除数:")
    #flag=raw_input("是否屏蔽异常信息（n/y）:")
    print "x/y=",x/y
except ZeroDivisionError:
    #if(flag=="n"):
    print "除数不能为0！"
    '''else:
        raise'''
except TypeError:
    print "请输入数字！"



#test2
print "="*30
while(1):
    try:
        x=input("输入被除数：")
        y=input("输入除数：")
        z=x/y
        print "x/y=",z
        break
    except :
        print "输入错误，再输一次"








