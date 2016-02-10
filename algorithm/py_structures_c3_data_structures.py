# -*-coding: utf-8 -*-
### (1)list
# list各个操作的时间复杂度
#def test1():
#    l = []
#    for i in range(1000):
#        l = l + [i]
#
#def test2():
#    l = []
#    for i in range(1000):
#        l.append(i)
#
#def test3():
#    l = [i for i in range(1000)]
#
#def test4():
#    l = list(range(1000))

#from timeit import timer
## if the above line is excluded, you need to replace timer with
## timeit.timer when defining a timer object
#t1 = timer("test1()", "from __main__ import test1")
#print ("concat", t1.timeit(number=1000), "milliseconds")
#t2 = timer("test2()", "from __main__ import test2")
#print ("concat", t2.timeit(number=1000), "milliseconds")
#t3 = timer("test3()", "from __main__ import test3")
#print ("concat", t3.timeit(number=1000), "milliseconds")
#t4 = timer("test4()", "from __main__ import test4")
#print ("concat", t4.timeit(number=1000), "milliseconds")

#from timeit import timer
#x = list(range(200000))
#pop_zero = timer("x.pop(0)", "from __main__ import x")
#print ("pop_zero", pop_zero.timeit(number=1000), "milliseconds")
#x = list(range(200000))
#pop_end = timer("x.pop()", "from __main__ import x")
#print("pop_end", pop_zero.timeit(number=1000), "milliseconds")

### (2)dictonary
#import timeit
#import random
#
#for i in range(10000, 100001, 20000):
#    t = timeit.timer("random.randrange(%d) in x"%i, "from __main__ import random, x")
#    print 'aa'
#    x = list(range(i))
#    print 'bb'
#    lst_time = t.timeit(number=1000)
#    print 'cc'
#    x = {j:None for j in range(i)}
#    d_time = t.timeit(number=1000)
#    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))


#### 2.栈：lifo结构，后进先出
#class stack:
#    def __init__(self):
#        self.items = []
#    def is_empty(self):
#        return self.items == []
#    def push(self, item):
#        self.items.append(item)
#    def pop(self):
#        return self.items.pop()
#    def peek(self):
#        return self.items[len(self.items)-1]
#    def size(self):
#        return len(self.items)
#
#s = stack()
#print(s.is_empty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(true)
#print(s.size())
#print(s.is_empty())
#s.push(8.4)
#print(s.pop())
#print(s.pop())
#print(s.size())


#### 3.队列：fifo结构，先进先出
#class queue:
#    def __init__(self):
#        self.items = []
#    def is_empty(self):
#        return self.items == []
#    def enqueue(self, item):
#        self.items.insert(0, item)
#    def dequeue(self):
#        return self.items.pop()
#    def size(self):
#        return len(self.items)
#
#q = queue()
#q.enqueue('hello')
#q.enqueue('dog')
#print(q.items)
#q.enqueue(3)
#q.dequeue()
#print(q.items)


#### 4.双向队列：左右两边都可以插入和删除的队列
#class deque:
#    def __init__(self):
#        self.items = []
#    def is_empty(self):
#        return self.items == []
#    def add_front(self, item):
#        self.items.append(item)
#    def add_rear(self, item):
#        self.items.insert(0, item)
#    def remove_front(self):
#        return self.items.pop()
#    def remove_rear(self):
#        return self.items.pop(0)
#    def size(self):
#        return len(self.items)
#dq = deque()
#dq.add_front('dog')
#dq.add_rear('cat')
#print(dq.items)
#dq.remove_front()
#dq.add_front('pig')
#print(dq.items)


#### 5.二叉树
## 1.直接使用list
#def binary_tree(r):
#    return [r, [], []]
#def insert_left(root, new_node):
#    t = root.pop(1)
#    if len(t) > 1:
#        root.insert(1, [new_node, t, []])
#    else:
#        root.insert(1, [new_node, [], []])
#    return root
#def insert_right(root, new_node):
#    t = root.pop(2)
#    if len(t) > 1:
#        root.insert(2, [new_node, [], t])
#    else:
#        root.insert(2, [new_node, [], []])
#    return root
#def get_root_val(root):
#    return root[0]
#def set_root_val(root, new_val):
#    root[0] = new_val
#def get_left_child(root):
#    return root[1]
#def get_right_child(root):
#    return root[2]
#r = binary_tree(3)
#insert_left(r, 4)
#insert_left(r, 5)
#insert_right(r, 6)
#insert_right(r, 7)
#print(r)
#l = get_left_child(r)
#print(r), '===='
#set_root_val(l, 9)
#insert_left(l, 11)
#print(r)
#print(get_right_child(get_right_child(r)))
### 2，使用类的形式定义二叉树，可读性更好
#class BinaryTree:
#    def __init__(self, root):
#        self.key = root
#        self.left_child = None
#        self.right_child = None
#
#    def insert_left(self, new_node):
#        if self.left_child is None:
#            self.left_child = BinaryTree(new_node)
#        else:
#            t = BinaryTree(new_node)
#            t.left_child = self.left_child
#            self.left_child = t
#
#    def insert_right(self, new_node):
#        if self.right_child is None:
#            self.right_child = BinaryTree(new_node)
#        else:
#            t = BinaryTree(new_node)
#            t.right_child = self.right_child
#            self.right_child = t
#    def get_left_child(self):
#        return self.left_child
#    def get_right_child(self):
#        return self.right_child
#    def set_root_val(self, obj):
#        self.key = obj
#    def get_root_val(self):
#        return self.key
#
#r = BinaryTree(3)
#r.insert_left(4)
#r.insert_left(5)
#r.insert_right(6)
#r.insert_right(7)
#print r.key
#l = r.get_left_child()
#print(l.key)
#l.set_root_val(9)
#print(r.get_right_child().get_right_child())
### 6.二叉堆
#class BinHeap:
#    def __init__(self):
#        self.heap_list = [0]
#        self.current_size = 0
#    def perc_up(self, i):
#        while i // 2 > 0:
#            if self.heap_list[i] < self.heap_list[i//2]:
#                tmp = self.heap_list[i//2]
#                self.heap_list[i // 2] = self.heap_list[i]
#                self.heap_list[i] = tmp
#            i = i // 2
#    def insert(self, k):
#        self.heap_list.append(k)
#        self.current_size = self.current_size + 1
#        self.perc_up(self.current_size)
#    def perc_down(self, i):
#        while(i * 2) <= self.current_size:
#            mc = self.min_child(i)
#            if self.heap_list[i] > self.heap_list[mc]:
#                tmp = self.heap_list[i]
#                self.heap_list[i] = self.heap_list[mc]
#                self.heap_list[mc] = tmp
#            i = mc
#    def min_child(self, i):
#        if i * 2 + 1 > self.current_size:
#            return 1 * 2
#        else:
#            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
#                return i * 2
#            else:
#                return i * 2 + 1
#    def del_min(self):
#        ret_val = self.heap_list[1]
#        self.heap_list[1] = self.heap_list[self.current_size]
#        self.current_size = self.current_size - 1
#        self.heap_list.pop()
#        self.perc_down(1)
#        return ret_val
#    def build_heap(self, a_list):
#        i = len(a_list) // 2
#        self.heap_list = [0] + a_list[:]
#        while(i > 0):
#            self.perc_down(i)
#            i = i - 1
#a_list = [9, 6, 5, 2, 3]
#bh = BinHeap()
#bh.build_heap(a_list)
#print(bh.heap_list)
#print(bh.current_size)
#bh.insert(10)
#bh.insert(7)
#print(bh.heap_list)
#print(bh.current_size)
my_num = 7
def func(number):
    my_num = number * 2
    print my_num
    return 'ff'
print func(7)
print 'outside', my_num
