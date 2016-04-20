#!/usr/bin/python 
#-*- coding:utf-8 -*-
#class 7:函数练习

'''
#斐波那契数列
def fib(x):
    a=0;b=1;
    list_fib=[]
    list_fib.append(a)
    list_fib.append(b)
    while((len(list_fib))<x):
        c=a+b
        a=b
        b=c
        list_fib.append(c)
    return list_fib;
'''

#初始化扑克
from random import shuffle
def initPoker(flag=0):
    pNum=range(1,14)
    pType=["HO","HE","FA","MH"]

    result=["%s:%s"%(pt,pn)for pt in pType for pn in pNum]
    if(flag==0):#有大小王
        result.append("S:DW")
        result.append("S:XW")
        #print "OOOOOO"
    shuffle(result)
    return result
    

#发牌函数
def initPerson(personNum,gameType,poker):
    pokerSum=54
    pokerCurson=0
    pokerEnd=0
    result={}

    if(gameType==0):#斗地主
        if(personNum<3 or personNum>4):
            print "人数不正确"
            return
        elif(personNum==3):
            pokerCurson=51
            pokerEnd=3
            user=["NM1","NM2","DZ"]
            result.fromkeys(user,"")
            result["NM1"]=poker[0:17]
            result["NM2"]=poker[17:34]
            result["DZ"]=poker[34:54]
        else:
            pokerEnd=2
            pokerCurson=52
            user=["NM1","NM2","NM3","DZ"]
            result.fromkeys(user,"")
            result["NM1"]=poker[0:13]
            result["NM2"]=poker[13:26]
            result["NM3"]=poker[26:39]
            result["DZ"]=poker[39:54]
    return result






if __name__=="__main__":
    '''list_fib=fib(10)
    print "fib(10)=",list_fib'''
    s=initPoker();
    r=initPerson(4,0,s)
    print r



