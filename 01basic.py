#!/usr/bin/python
#-*- coding:utf-8 -*-
#Quick python script explanation for programmers
#给程序员的脚本解说

#导入模块
import os,sys

def main():
    #声明单行字符串，使用单双引号都行，若字符串中有引号需转义  \'
    print( 'hello world!')
    print( '这是Bob\'的问候')

    foo(5,10)

    #字符串可乘，等同于==========
    print ('=' * 10)

    print ('这将直接执行' + 'hello world')

    count = 0
    count += 1

    food=['红','黄','蓝','紫','黑']

    for i in food:
        print ('我喜欢'+i+'色')

    print( '数到10')
    for i in range(10):
        print('%d'%(i+1))


def foo(i,j):
    add=i+j
    print ('%s加%s等于%s'%(i,j,add))

    if add<10:
        print ('aaaaaaaaaa')
    elif (add>=10) and (i==1):
        print ('bbbbbbbbbb')
    else:
        print ('cccccccccc')

    return add



#当且仅当直接运行当且脚本时，条件才会成立
if __name__=='__main__':
    main()


