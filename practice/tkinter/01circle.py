#!/usr/bin/python 
#-*- coding:utf-8 -*-

import tkinter

canves=Canvas(width=800,height=600,bg="red")
canves.pack(expand=YES,fill=BOTH)

k=1
j=1
for i in range(0,26):
    canves.create_oval(310-k,250-k,310+k,250+k,width=1)
    k+=j
    j+=0.3

