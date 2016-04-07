#!/usr/bin/python
#-*- coding=utf-8 -*-


text=["说书唱戏劝人方"，"三条大路走中央","善恶到头终有报","人间正道是沧桑"]
#text=["abc","bcd","cde","def"]
f=open('./test.txt','w')

for line in text:
    f.write("%s\n"%(line))
    #print(line)
f.close()


f=open("./test.txt")
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line)
f.close()




'''

import pickle
filepath="test"

namelist=["peter","john","tom","king"]

f=open(filepath,"wb")
pickle.dump(namelist,f)
f.close()

del namelist

f=open(filepath,"rb")
storednamelist=pickle.load(f)

print(storednamelist)

'''
