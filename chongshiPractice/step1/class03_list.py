#!/usr/bin/python
#-*- coding:utf-8 -*-
#基础篇 class3:列表和元组
#区别：列表可修改，元组不可修改；当任意添加元素时列表好用，不修改时元组适合


#索引
print "索引示例:"

x=[0,1,2,3,4,5,6,7,8,9]
#x="0123456789"
print "x=",x
print "x[0]=",x[0]
print "x[9]=",x[9]
print "x[-2]=",x[-2]

print "*"*30



#切片
print "切片示例:"

print "x[a:b]=从下标a开始向后数b-a个数"
y=r"C:/a/b/c/d.jpg"
print "y=",y
print "y[:]=",y[:]
print "y[0,9]=",y[0:9]
print "y[-5:-1]=",y[-5:-1]
print "y[-5:]=",y[-5:]

print "*"*30



#函数
print "序列操作和函数"

print "[0,1,2]+[5,6,7]=",[0,1,2]+[5,6,7]
print "[0]*10=",[0]*10
print "'one' in ['one','two','three']=",'one' in ['one','two','three']
print "'ooo' in ['one','two','three']=",'ooo' in ['one','two','three']
print "="*20
num=[1,6,3,7,5]
print "num=",num
print "len(num)=",len(num)
print "max(num)=",max(num)
print "min(num)=",min(num)
num.sort()
print "num.sort(),num=",num
num.reverse()
print "num.reverse(),num=",num
num.remove(1)
print "num.remove(1),num=",num

print "="*20
string="i love you"
print "string=",string
x=list(string)
print "string => list=",x

print "="*20
x=[1,2,3]
print "x=",x
x.append(3)
print "x.append(3),x=",x
num=x.count(3)
print "x.count(3)=",num
index=x.index(3)
print "x.index(3)=",index
x.insert(0,2)
print "x.insert(0,2),x=",x

print "*"*30



#栈
print "序列做栈使用"

x=[1,2,3]
print "x=",x
x.append(4)
print "x.append(4),x=",x
print "x.pop()=",x.pop(),"x=",x

print "*"*30



#队列
print "序列做队列使用"

from collections import deque
x=[1,2,3,4,5]
y=deque(x)
print "y=",y
y.append(6)
print "y.append(6),y=",y
print "y.pop()=",y.pop(),"y=",y
print "y.popleft()=",y.popleft(),"y=",y

print "*"*30



