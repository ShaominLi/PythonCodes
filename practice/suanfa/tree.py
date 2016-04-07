#!/usr/bin/python 
#-*- coding:utf-8 -*-

#bitree类结构定义
class Node:
    def __init__(self,data=-1,lchild=None,rchild=None):
        self.data=data
        self.lchild=lchild
        self.rchild=rchild


#001 先序创建二叉树
def create_Titree(t):
    value=input("input value:")
    if value == ".":
        t=None
    else:
        t=Node(value)
        t.lchild=create_Titree(t.lchild)
        t.rchild=create_Titree(t.rchild)
    return t


#002 遍历输出
def travel(t,flag):
    if t != None:
        if flag == 0:
            "前序遍历"
            print(t.data,end=" ")
            travel(t.lchild,0)
            travel(t.rchild,0)
        elif flag == 1:
            "中序遍历"
            travel(t.lchild,1)
            print(t.data,end=" ")
            travel(t.rchild,1)
        elif flag == 2:
            "后序遍历"
            travel(t.lchild,2)
            travel(t.rchild,2)
            print(t.data,end=" ")
        else:
            print("未选择遍历方式")


#003 统计叶子节点
def static_leaf(t):
    if t == None:
        return 0
    elif (t.lchild == None) and (t.rchild == None):
        n=1
        print(t.data,end=" ")
    else:
        n=static_leaf(t.lchild)+static_leaf(t.rchild)

    return n





def test():
    root=Node()
    print("create Titree:")
    root=create_Titree(root)
    print("="*16+"create Titree ok!"+"="*16)
    print("前序遍历：")
    travel(root,0)
    print("\n中序遍历：")
    travel(root,1)
    print("\n后序遍历：")
    travel(root,2)
    print("\n叶子节点：")
    print("个数：",static_leaf(root))


if __name__ == "__main__":
    test()

