# -*- coding: utf-8 -*-
# time: 2023/7/6 16:23
# file: test01.py
# author: wht

# def t0707(**kwargs):
#     data = {}
#     print('kwagrs --->', kwargs)
#     data.update(**kwargs)
#     return data
#
#
# f = t0707(a=123)
# print(f)


# l1 = 10
# l2 = 9
# print(-13 % 11)


#
# print([0 for i in range(10)])
# print([i for i in range(10)])


# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class Queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.queue = [0 for _ in range(size)]

    def push(self, element):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('queue is full')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('queue is empty')

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


if __name__ == '__main__':
    qu = Queue(10)
    # qu.push(11)
    # qu.push(14)
    # qu.push(17)
    # qu.push(17)
    # qu.push(17)
    # qu.push(17)
    # qu.push(17)
    # qu.push(17)
    # # qu.push(17)
    # qu.push(12)
    # # qu.push(17)
    # print(qu.queue)
    # print(qu.pop())
    # qu.push(99)
    # qu.push(199)
    # print(qu.queue)


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# a = Node(3)
# b = Node(6)
# c = Node(9)
#
# a.next = b
# b.next = c
#
# print(a.item)
# print(a.next.item)
# print(a.next.next.item)

class BiTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTree('A')
b = BiTree('B')
c = BiTree('C')
d = BiTree('D')
e = BiTree('E')
f = BiTree('F')
g = BiTree('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f
root = e


# 前序遍历
def pre_order(root):
    if root:
        print(root.data,end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

pre_order(root)
print('\n')
# 中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data,end=',')
        in_order(root.rchild)

in_order(root)
print('\n')

def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')

post_order(root)


