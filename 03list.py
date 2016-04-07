#!/usr/bin/python
#-*- coding:utf-8 -*-

list1=[1,2,2,3]
print("原list:%s"%(list1))

#count()
num=list1.count(2)
print("元素中2的个数：%s"%(num))

#append()
list1.append(4)
print("增加元素4后list:%s"%(list1))

#extend()
list2=[5,6,7,1]
list1.extend(list2)
print("拼接list2后的list:%s"%(list1))

#index()
a=2
index=list1.index(a)#第一个出现2的下标
#异常输出
a=10
try:
    print("%d"%(list1.index(a)))
except ValueError as ve:
    print("在列表中找不到%d"%(a))

#insert()
list1.insert(1,100)
print("下标1插入100:%s"%(list1))
list1.insert(100,100)
print("下标超出后的插入:%s"%(list1))

#pop()
print("pop没参数执行%s"%(list1.pop()))
print("pop正常参数的执行%s"%(list1.pop(0)))
try:
    print("%s"%(list1.pop(100)))
except IndexError as ie:
    print("index out of range")
print("执行完pop函数后的list:%s"%(list1))

#reserve()
list1.reverse()
print("执行完reserve后的list:%s"%(list1))

#sort()
list3=["abc","bbd","cce","daf"]
list3.reverse()
print("%s"%(list3))
list3.sort()
print("执行sort后的list:%s"%(list3))
list3.sort(key=lambda s:s[1])
print("执行sort(key=lambda s:s[1])的list:%s"%(list3))

#sorted
list4=[1,9,4,2,6,10,0]
list5=sorted(list4)
print("list4:%s"%(list4))
print("list5:%s"%(list5))

#切片操作
list6=[0,1,2,3,4,5]
print("list:%s"%(list6))
print("[:]--%s"%(list6[:]))
print("[2:]--%s"%(list6[2:]))   #从2开始到结束
print("[:4]--%s"%(list6[:4]))   #从0开始到4-1
print("[2:4]--%s"%(list6[2:4])) #从2开始到4-1

#将链表当做栈使用
list0=[1,2,3]
print("栈：",list0)
list0.append(4)
print("入栈：",list0)
print("出栈：",list0.pop())
print(list0)

#队列queue
from collections import deque
queue=deque(list0)
print("队列：",queue)
queue.append(7)
print("入队列：",queue)
print("出队列左值：",queue.popleft(),queue)
print("出队列右值:",queue.pop(),queue)

#链表推导式
list7=[x**2 for x in range(8) ]
print("由推导式生成链表例1：",list7)
list7=[]
list7=[(x,y) for x in [1,2,3] for y in [1,2,3] if x!=y]
print("由推导式生成链表例2：",list7)




