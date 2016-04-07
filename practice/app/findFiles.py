#!/usr/bin/python 
#-*- coding -*-
import os


file_type=input("input file type:")
fold=input("input fold:")

#遍历文件夹，找出所有符合的文件，并打印出路径
def trans_fold(dir):
    filenames=os.listdir(dir)
    for name in filenames:
        #print(dir+"/"+name)
        if os.path.isfile(dir+"/"+name):
            #判断后缀
            if name.endswith(file_type):
                print(dir+"/"+name)
        else:
            trans_fold(dir+"/"+name)

trans_fold(fold)

