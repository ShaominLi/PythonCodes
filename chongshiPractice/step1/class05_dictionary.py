#!/usr/bin/python 
# -*- coding:utf-8 -*-
#class5:dictionary操作

dic={
    "0001":"Tom",
    "0002":"Lily",
    "0003":"Susan"
}
print "dic=",dic 
print "dic['0001']=",dic["0001"]

print "="*30

keys=[1,2,3,4]
print "keys[]=",keys
dic1={}.fromkeys(keys)
print "{}.fromkeys(keys)=",dic1
dic1={}.fromkeys(keys,"default")
print "{}.fromkeys(keys,'default')=",dic1

print "="*30

dic2={
        1:"one",
        2:"two",
        3:"three"
        }
print "dic2=",dic2
print "dic2.get(1)=",dic2.get(1)
print "dic2.get(1)=",dic2.get(1)
print "dic2.get(4)=",dic2.get(4)
print "dic2.get(4,'Error')=",dic2.get(4,"Error")

print "="*30

dic3={
        1:"A",
        2:"B",
        3:"C"
        }
print "dic3=",dic3
print "1 in dic3 =",1 in dic3

print "="*30



