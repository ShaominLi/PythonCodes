#!/usr/bin/python
#-*- coding:utf-8 -*-

#初始化
dic1={}
dic2={0:"zero",1:"one",2:"two",3:"three"}

dic1[4]="four"
dic1[5]="five"
dic1[6]="six"

print("dic1:%s"%(dic1))
print("dic2:%s"%(dic2))


#copy()
dic3=dic1.copy()
print("dic3 is copy dic2:%s"%(dic3))


#用list创建字典fromkeys(list,value)
l=[1,2,3]
dic4={}.fromkeys(l)
print("fromkeys(l):%s"%(dic4))
dic5={}.fromkeys(l,"default")
print("fromkeys(l,\"default\"):%s"%(dic5))


#get(key,value),若key存在返回值，否则返回value
print(dic1.get(4,"test"))
print(dic1.get(10,"test"))


#key in dictionary判断有无此key，有true，无false
print(1 in dic5)
print(10 in dic5)


#items(),keys(),values()
#items()
for item in dic1.items():
    print(item)
for key,value in dic1.items():
    print("%s:%s"%(key,value))
#keys()
for key in dic1.keys():
    print(key)
#values()
for value in dic1.values():
    print(value)


#pop(key,default)若key存在返回value并删除，不存在返回default，无第二参数异常
print(dic2)
print("dic.pop(1)--%s"%(dic2.pop(1)))
print("dic.pop(4,\"test\")--%s"%(dic2.pop(4,"test")))
try:
    print("dic.pop(1)--%s"%(dic2.pop(4)))
except KeyError as ke:
    print("dic.pop(4)--KeyError")


#setdefault(key,default)若key存在则返回value，否则加上key：default
print(dic1)
print("dic.setdefault(4)--%s"%(dic1.setdefault(4)))
print("dic.setdefault(1,\"test\")--%s"%(dic1.setdefault(1,"test")))



#update(dictionary)合并字典，重复覆盖
print("dic1--%s"%(dic1))
print("dic2--%s"%(dic2))
dic1.update(dic2)
print("dic1.update(dic2)--%s"%(dic1))












