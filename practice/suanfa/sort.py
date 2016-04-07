#!/usr/bin/python 
#-*- coding:utf-8 -*-

#001 冒泡排序
def BubbleSort(x=[]):
    exchange=1
    n=len(x)
    for i in range(1,n):
        exchange=0
        for j in range(i,n)[::-1]:
            if x[j]<x[j-1]:
                t=x[j-1]
                x[j-1]=x[j]
                x[j]=t
                exchange=1
        if exchange==0:
            break



#002 选择排序
def selectSort(s=[]):
    size=len(s)
    for i in range(0,size-1):
        k=i
        for j in range(i+1,size):
            if s[k]>s[j]:
                k=j
        if k!=i:
            t=s[i]
            s[i]=s[k]
            s[k]=t



#003 一次快速排序
def quickSort(s=[]):
    t=s[0]
    low=0
    high=len(s)-1
    while low<high:
        while low<high and s[high]>t:
            high-=1
        s[low]=s[high]
        while low<high and s[low]<t:
            low +=1
        s[high]=s[low]
    s[low]=t



#004 插入排序
def insertSort(s=[]):
    n=len(s)-1
    ss=s[0:1]
    for v in s[1:]:
        nn=len(ss)-1
        while ss[nn]>v:
            nn-=1
            if nn==-1:
                break
        ss.insert(nn+1,v)
    return ss

s=[1,4,6,3,2]
s=insertSort(s)
print(s)







