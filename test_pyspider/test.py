#!/usr/bin/python 
#-*- coding:utf-8 -*-
import re

text="大洋新闻 时间: 2016-04-19 来源: 广州日报: 张涨"
#text="wdwheunjsdnw2016-04-19ksdjsiodns"
#pattern=re.compile(r"作者")
#result=re.findall(r"作者",text)
if (re.findall(r"作者",text)):
    print "ok"
else:
    print "error"
