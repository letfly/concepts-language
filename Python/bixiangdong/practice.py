#coding:utf8
class Books:
    def __init__(self, title, author, subject, book_id):
        self.title = title
        self.author = author
        self.subject = subject
        self.book_id = book_id

if __name__ == '__main__':
    book1 = Books("C Programming", "letfly", "C Programming Tutorial", 6495407)
    book2 = Books("C Programming 2", "letfly", "C Programming Tutorial", 6495408)
    print "Book 1 title : {title}\n".format(title=book1.title)
    print "Book 2 title : {title}\n".format(title=book2.title)
'''
x=4;print "x="+str(x);print "x=",x
##2
a=1>2 and 1 or 2;print a
##3
x=2
if x==3 or x==4 or x==5:
    print str(x)+"春季"
elif x==6 or x==7 or x==8:
    print str(x)+"夏季"
else:
    print "月份不存在"
##4
num=4
if num==4:
    print 'a'
elif num==6:
    print 'b'
else:
    print 'c'
##5
x=1
while x<3:
    print x
    x+=1
else:
    print x,"is not less than 3"
##6
for x in range(0,3):
    print x
print x
##7
for x in range(0,3):
    for y in range(0,4):
        print "*",
    print
##8
#break,continue 
##9
#pass
##10
def getResult(num):
    return num*3+5
print getResult(4)
#python不需要重载：1，python 可接受任何类型的参数2，python 可接受缺省参数
##11
x=('8',)
print type(x)#tuple
tup1=(12,345);tup2=('abc',)
print tup1+tup2
tup=('p','c')
print tup;del tup;
print len((1,2,3))
print (1,2)+(3,)
print ['Hi!']*4
print 3 in (1,2,3)
for x in (1,2,3):
    print x
##
####二，面向对象
##1
class Car:
    num=0
    color="red"
    def run(self):
        print "%d::%s"%(self.num,self.color)
c=Car()
c.run()
##5匿名函数
sum=lambda arg1,arg2:arg1+arg2
print "Value of total:",sum(10,20)
def sum(arg1,arg2):
    return arg1+arg2
print "Value of total:",sum(10,20)
##8构造函数
class Person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
##9构造代码块
#python没有这种概念
    #基础重载
#__init__(self[,args...])构造函数  obj=Classname(args)
#__del__(self)析构方法删除一个对象  del obj
#__repr__(self)转化为供解释器读取的形式  repr(obj)
#__str__(self)用于将值转化为适于人阅读的形式  str(obj)
#__cmp__(self)对象比较  cmp(obj,x)
class Vector:
    def __init__(self,a,b):
        self.a=a;self.b=b
    def __str__(s):
        return 'Vector (%d,%d)'%(s.a,s.b)
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
v1=Vector(2,10)
v2=Vector(5,-1)
print v1+v2
##10this关键字
#0、python中的self相当于this.
#1、如果调用成员变量必须使用self.
#2、self不一定叫self，可以改变它的名称
#3、在成员函数中使用self.name变量相当于声明一个成员变量
#4、函数调用时不用传入self
##11this应用


## day06
##1，static关键字
##静态static[用于修饰成员，共享内容]
##1)静态方法无需self,类成员方法需cls参数;
##2)因无需self,静态方法是无法访问实例变量与类变量。
##3)静态方法像函数工具库的作用，而类成员方法则更接近类似java面向对象概念中的静态方法
##2，main()函数[作为程序的入口]
#没有main住函数
def foo():
    str="function";print(str)
if __name__=='__main__':
    print "main"
foo()
##3，没有定义，字段全是静态的，创建非静态需在字段前加self,字段才属于某个对象。
class aaa:
    def __init__(self,cs):
        self.a=[]
        self.a.append(cs)
b=aaa('b');c=aaa('c');print b.a,c.a#['b']['c']
class aaa:
    a=[]
b=aaa();b.a.append('b');c=aaa();c.a.append('c')
print b.a,c.a#['b','c']['b','c']
##4，静态的应用-工具类
#没有定义，字段全是静态的
##6，静态代码块[随着类的加载而执行，只执行一次用于给类初始化]
class StaticCode:
    print "cry"
StaticCode();StaticCode()
##7，对象的初始化过程：
##9，单例设计模式：[偏思想]
class Singleton(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):
            orig=super(Singleton,cls)
            cls._instance=orig.__new__(cls,*args,**kw)
        return cls._instance
class Myclass(Singleton):
    a=1
one=Myclass();two=Myclass();two.a=3
print one.a;print one is two


##day07
##1，继承-概述[为了提高代码的复用性，提出类类之间关系所属关系 is a]
class Parent:
    parentArr=100
    def __init__(self):
        print "Parent constructor"
    def parentMethod(self):
        print "Parent method"
class Child(Parent):
    def __init__(self):
        print "Child constructor"
    def childMethod(self):
        Parent.parentMethod(self)
        print Parent.parentArr
c=Child();c.childMethod()
class P1:
    def p(self):
        print "p1"
class P2:
    def p(self):
        print "p2"
class P(P1,P2):
    def __init__(self):
        print "p"
p=P();p.p()
##4，子父类中变量特点：
class Fu:
    num=4
class Zi(Fu):
    num=5
    def show(self):
        print Fu.num,self.num
z=Zi();z.show()
##5，子父类覆盖
class Fu:
    def show(self):
        print "Fu"
class Zi(Fu):
    def show(self):
        print "Zi"
z=Zi();z.show()
def test(a,*args,**k):
    print a,args,k
test(1,2)

##day11
##5.获取线程对象以及名称
from threading import Thread
class Test(Thread):
    def __init__(self,name):
        self.u=name
        super(Test,self).__init__()
    def run(self):
        for x in range(0,50):
            print self.getName(),"thread...",x#获取默认线程名称
class Test(Thread):
    def __init__(self,name):
        super(Test,self).__init__()
        self.name=name
    def run(self):
        for x in range(0,50):
            print self.getName(),"thread...",x#获取当前线程名称
t1 = Test("one")
t2 = Test("two")
t1.start()
t2.start()
for x in range(0,10):
    print "main...",x
##6.售票的例子
from threading import Thread
class Ticket(Thread):
    def run(self):
        tick = 100
        while True:
            if tick>0:
                print self.getName(),"sale:",tick
                tick-=1
t1 = Ticket()
t1.start()
t1.start()
'''
##day12
##装饰器学习
"""
'''示例1：最简单的函数，表示调用了两次'''
def myfunc():
    print "myfunc() called."
myfunc()
myfunc();print
'''示例2：替换函数(装饰)
装饰函数的参数是被装饰的函数对象，返回原函数对象
装饰的实质语句：myfunc = deco(myfunc)'''
def deco(func):
    print "before myfunc() called."
    func()
    print "after myfunc() called."
    return func
def myfunc():
    print "myfunc() called."
myfunc = deco(myfunc)
myfunc()
myfunc();print
'''示例3：使用语法糖@来装饰函数，相当于"myfunc = deco(myfunc)"
但发现新函数只在第一次被调用，而原函数多调用了一次'''
def deco(func):
    print "before myfunc() called."
    func()
    print "after myfunc() called."
    return func
@deco
def myfunc():
    print "myfunc() called."
myfunc()
myfunc();print 
'''示例4：使用内嵌包装函数来确保每次新函数都被调用，内嵌
包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
def deco(func):
    def _deco():
        print "before myfunc() called."
        func()
        print "after myfunc() called."
    return _deco
@deco
def myfunc():
    print "myfunc() called."
    return 'ok'
myfunc()
myfunc();print

'''示例5：对带参数的函数进行装饰，内嵌包装函数的形参
和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
def deco(func):
    def _deco(a, b):
        print "before myfunc() called."
        ret = func(a, b)
        print "after myfunc() called. result: %s" % ret
        return ret
    return _deco
@deco
def myfunc(a, b):
    print "myfunc(%s, %s) called." % (a, b)
    return a + b
myfunc(1, 2)
myfunc(3, 4);print
#before myfunc() called.
#myfunc(1, 2) called.
#after myfunc() called. result: 3
#before myfunc() called.
#myfunc(3, 4) called.
#after myfunc() called. result: 7
#before myfunc() called.
myfunc = deco(myfunc)
myfunc(1, 2)
myfunc(3, 4);print
'''示例6：对参数数量不确定的函数进行装饰，参
数用(*args, **kwargs)，自动适应变参和命名参数'''
def deco(func):
    def _deco(*args, **kwargs):
        print "before %s called." % func.__name__
        ret = func(*args, **kwargs)
        print "after %s called. result: %s" % (func.__name__, ret)
        return ret
    return _deco
@deco
def myfunc(a, b):
    print "myfunc(%s, %s) called." % (a, b)
    return a + b
@deco
def myfunc2(a, b, c):
    print "myfunc2(%s, %s, %s) called." % (a, b, c)
    return a + b + c
myfunc(1, 2)
myfunc2(1, 2, 3);print
#before myfunc called.
#myfunc(1, 2) called.
#after myfunc called. result: 3
#before myfunc2 called.
#myfunc2(1, 2, 3) called.
#after myfunc2 called. result: 6
'''示例7：在示例4的基础上，让装饰器带参数，和上一示例
相比在外层多了一层包装。装饰函数名实际上应更有意义些'''
def deco(arg):
    def _deco(func):
        def __deco():
            print "before %s called [%s]." % (func.__name__, arg)
            func()
            print "after %s called [%s]." % (func.__name__, arg)
        return __deco
    return _deco
@deco('module')
def myfunc():
    print "myfunc() called."
@deco('module2')
def myfunc2():
    print "myfunc2 called."
myfunc()
myfunc2();print
#before myfunc called [module].
#myfunc() called.
#after myfunc called [module].
#before myfunc2 called [module2].
#myfunc2() called.
#after myfunc2 called [module2].
'''示例8：装饰器带类参数'''
class locker:
    def __init__(self):
        print "locker.__init__() should be not called."
    @staticmethod
    def acquire():
        print "locker.acquire() called.(这是静态方法)"
    @staticmethod
    def release():
        print "locker.release() called.(不需要对象实例)"
def deco(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco():
            print "before %s called [%s]." % (func.__name__, cls)
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco
@deco(locker)
def myfunc():
    print "myfunc() called."
myfunc()
myfunc()
#before myfunc called [__main__.locker]
#"locker.acquire() called.(这是静态方法)"
#"myfunc() called."
#"locker.release() called.(不需要对象实例)"
#before myfunc called [__main__.locker]
#"locker.__init__() should be not called."
#"myfunc() called."
'''mylocker.py: 公共类for 示例9.py'''
"""
class mylocker:
    def __init__(self):
        print "mylocker.__init__() called."
    @staticmethod
    def acquire():
        print "mylocker.acquire() called."
    @staticmethod
    def unlock():
        print "mylocker.unlock() called.\n"
class lockerex(mylocker):
    @staticmethod
    def acquire():
        print "lockerex.acquire() called."
    @staticmethod
    def unlock():
        print "lockerex.unlock() called."
def lockhelper(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco(*args, **kwargs):
            print "before %s called." % func.__name__
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco























#########################################PythonTip
##A.abstract_factory
"""Implementation of the abstract factory pattern"""
import random

class PetShop:
    """A pet shop"""
    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.
        We can set it at will."""
        self.pet_factory = animal_factory
    def show_pet(self):
        """Creates and shows a pet using the
        abstract factory"""
        pet = self.pet_factory.get_pet()
        print("This is a lovely",pet)
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())

# Stuff that our factory makes
class Dog:
    def speak(self):
        return "woof"
    def __str__(self):
        return "Dog"
class Cat:
    def speak(self):
        return "meow"
    def __str__(self):
        return "Cat"
# Factory classes
class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "dog food"
class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "cat food"
# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()

# Show pets with various factories
if __name__ == "__main__":
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("="*20)
'''
'''
'''
TCP编程
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示打开了一个"网络链接"，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型
即可。

客户端
大多数链接
'''
'''
def bubbleSort(numbers):
    for j in xrange(len(numbers)-1, -1, -1):
        for i in xrange(j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            print numbers

def main():
    numbers = [23, 12, 9, 15, 6]
    bubbleSort(numbers)
if __name__ == '__main__':
    main()
'''
#### metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass #指示使用ListMetaclass来定制类
#### 草稿
import json
# -*- coding: utf-8 -*-
'''
class Student(object):
    def __init__(self, name):
        self.name = name
print Student('Michael')
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print Student('Michael')
s = Student('Michael')
s
'''
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a, b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __getitem__(self, n):
        a, b = 1, 1
        for x in xrange(n):
            a, b = b, a + b
        return a

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10000:
            raise StopIteration()
        return self.a
for n in Fib():
    print n
print Fib()[80]
'''
'''
class Student(object):
    pass

s = Student()
s2 = Student()
s.name = 'Michael'
print s.name

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age

def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, None, Student)
s.set_score(100)
print s.score
s2.set_score(99)
print s2.score
'''
'''
import threading
storage = threading.local()
storage.foo = 1
print storage.foo
class AnotherThread(threading.Thread):
    def run(self):
        storage.foo = 2
        print storage.foo, '==='

another = AnotherThread()
another.start()
print storage.foo
'''
d = dict(name='a', age=20)
print json.dumps(d)
