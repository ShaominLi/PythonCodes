#!/usr/bin/python 
# -*- coding:utf-8 -*-
#class10:正则表达式

#通配符:.
#字符集:[]
#转义:\
#或:|
#子模式:p(ython|erl)
#可选项:?
#重复模式:
'''
    *:允许至少0次
    +:允许至少1次
    ?:允许0..1次
    {m,n}:允许m-n次
'''
#特殊:
'''
    \d:[0-9]
    \D:[^\d]非数字
    \s:空白字符[  \t\r\n\f\v]
    \S:非空白字符[^\s]
    \w:[a-zA-Z0-9]
    \W:非单词字符[^\w]
'''

#re模块函数
import re
pattern=re.compile(r"(\w+)\s")#将正则表达式编译为pattern对象
text="I am a boy,and I love my country"
m=pattern.match(text)#匹配第一个符合项
if(m):
    print m.groups()
else:
    print "error"

print "="*30
#split函数:以匹配项分割
pattern=re.compile(r"\d+")
text="one12131two23242three232four12333"
result=pattern.split(text)
print result

print "="*30
#findall函数:找出所有匹配项
result=pattern.findall(text)
print result 

print "="*30
#sub函数:替换匹配项
pattern=re.compile(r"\d+")
result=pattern.sub("-",text)
print result

