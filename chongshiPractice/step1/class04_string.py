#!/usr/bin/python 
#-*- coding:utf-8 -*-
#class4:string操作

x="I Love You"
print "x=",x
index=x.find("You")
print "x.find('you')",index
print "x.find('ok')",x.find("ok")

print "="*30

x="1+2+3+4"
print "x=",x
list1=x.split('+')
print "x.split('+')=",list1
y=["5","6","7","8","9"]
print "y=",y
string=','.join(y)
print "','.join(y)=",string

print "="*30

x="I LOYE YOU"
print "x=",x
print "x.lower()=",x.lower()
print "x.replace('LOYE','LOVE')=",x.replace("LOYE","LOVE")


