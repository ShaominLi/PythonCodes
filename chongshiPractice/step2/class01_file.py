#!/usr/bin/python 
#-*- coding:utf-8 -*-
#class1:文件操作

#文件函数
#f=open(path,model):
'''
    r:read
    w:write
    a:append
    b:binary(配合其他模式使用)
    +:读/写(配合其他模式使用)
'''
#f=open("class1_test","r")
#f.write("line3") #写入
#text=f.readline()  #读一行
#text=f.readlines()  #读所有，以list返回
#f.seek(10,0)  #定位光标：0-开头；1-当前；2-末尾
#num=f.tell()  #返回当前光标
#print num
#f.close()




#目录操作
import os
#os.mkdir("class1_test_dir")    #创建目录
#os.rmdir("class1_test_dir")    #删除目录

#输出目录内容
'''
for fileName in os.listdir("class1_test_dir"):
    print fileName'''  

#输出并筛选
'''
import fnmatch
for fileName in os.listdir("class1_test_dir"):
    #print fileName
    if fnmatch.fnmatch(fileName,"*.txt"):  
        print fileName
'''

#遍历文件夹所有文件










