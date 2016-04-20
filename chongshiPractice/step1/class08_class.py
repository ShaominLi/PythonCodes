#!/usr/bin/python 
# -*- coding:utf-8 -*-
#class 8:类的练习

_metaclass_=type #确定新类

class Persion:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    Name=property(getName,setName)
    
    def setAge(self,age):
        self.age=age

    def getAge(self):
        return self.age

    Age=property(getAge,setAge)

    def __init__(self,name,age):
        self.name=name
        self.age=age

one=Persion("Tom",21)
print "%s\'age is %d"%(one.Name,one.Age)

one.Age=20
print "%s\'age is %d"%(one.Name,one.Age)




#print "="*30
#class squre
class Squre:
    def getArea(self):
        return self.area

    def getPerimeter(self):
        return self.persion

class Circle(Squre):
    def __init__(self,radius):
        self.radius=radius

    def getRadius(self):
        return self.radius

    def getArea(self):
        self.area=3.14*self.radius**2
        return self.area

    def getPerimeter(self):
        self.persion=2*3.14*self.radius
        return self.persion

x=Circle(1.2)
print "x\'radius is %.2f,and area is %.2f,persion is %.2f"\
        %(x.getRadius(),x.getArea(),x.getPerimeter())






