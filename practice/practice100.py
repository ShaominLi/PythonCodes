#!/usr/bin/python 
#-*- coding -*-


#001.py
'''1，2,3,4数字，组成不相同，无重复三位数
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                print(i*100+j*10+k,end="\t")
        print()
'''


#002.py
'''输入一行字符串，统计其中各个字符字数 
import string

line=input("input a line string:")

num=len(line)
letter=0
space=0
digit=0
other=0

for i in range(0,num):
    if line[i].isalpha():
        letter+=1
    elif line[i].isspace():
        space+=1
    elif line[i].isdigit():
        digit+=1
    else:
        other+=1
print("%d-letters,%d-space,%d-digit,%d-other"%(letter,space,digit,other))
'''


#003.py 
'''递归方法求叠乘 
def fun(x):
    if x==1:
        return 1
    else:
        return int(x)*fun(int(x)-1)

n=input("input a number:")
print(fun(n))
'''


#004.py
''' '''

