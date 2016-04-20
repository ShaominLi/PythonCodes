#!/usr/bin/python 
#-*- coding:utf-8 -*-
#class6 基本结构和语句

#print
print "="*30
x=30
print "x=",30
print x
print "%d+30=60"%x

#if语句
print "="*30
print "if语句练习"
string=raw_input("input a string:")
if string.endswith("you"):
    print "you is the end"
elif string.endswith("her"):
    print "her is the end"
if string.startswith("I"):
    print "I is start"
elif string.startswith("He"):
    print "He is start"


#assert语句
print "="*30
print "assert语句练习"
age=input("input age:")
assert 0<age<100,"the number is bigger"


#while语句
print "="*30
print "while练习"
x=1
xsum=0
while x <=100:
    xsum+=x
    x+=1
print "1+2+3+...+100=",xsum



#for语句
from math import sqrt
print "="*30
print "for练习"
for x in range(1,101,1):
    y=sqrt(x)
    if(y==int(y)):
        print "%d能开方"%x
    
