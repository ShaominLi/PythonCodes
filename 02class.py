#!/usr/bin/python
#-*- coding:utf-8 -*-


'''
class Person:
    gCount=0
    def __init__(self,name,age):
        Person.gCount+=1
        self.name=name
        self.__age=age
p1=Person("tom",20)
p2=Person("peter",21)

print(Person.gCount)
print(p1.name)
#print(p1.__age),无法访问私有属性，报错
'''



#多继承实例
class SchoolMember:
    '''a SchoolMember'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Init a school member")
    def tell(self):
        print("name:%s,age:%s"%(self.name,self.age))

#继承SchoolMember
class Teacher(SchoolMember):
    '''a teacher'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print("init a teacher")
    def tell(self):
        SchoolMember.tell(self)
        print("salary:%s"%(self.salary))

#多继承实例
class Student(SchoolMember):
    '''a student'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print("init a student")
    def tell(self):
        SchoolMember.tell(self)
        print("marks:%s"%(self.marks))


print(SchoolMember.__doc__)
print(Teacher.__doc__)
print(Student.__doc__)

t=Teacher("Mr.Li",30,3000)
s=Student("Peter",25,2000)

members=[t,s]

for m in members:
    m.tell()










