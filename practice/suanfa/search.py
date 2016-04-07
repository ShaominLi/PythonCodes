#!/usr/bin/python 
#-*- coding:utf-8 -*-

#001 顺序表查找（递归法）
def list_search_1(l=[],v=-1):
    count=l.count(v)
    s=[]
    if count == 0:
        return [-1]
    elif count == 1:
        return [l.index(v)]
    else:
        s += [l.index(v)]
        s += list_search_1(l[l.index(v)+1:len(l)],v)
        return s
def list_search_2(l=[]):
    for v in range(1,len(l)):
        l[v]+=l[v-1]+1

def list_search(l=[],v=-1):
    print("在%s中查找%s:"%(l,v),end=" ")
    count=l.count(v)
    if count == 0:
        print("no exist")
    elif count == 1:
        print(list_search_1(l,v))
    else:
        s=list_search_1(l,v)   
        list_search_2(s)
        print(s)


#002 二分查找



