#coding:utf8
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
#5.获取线程对象以及名称
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
#6.售票的例子
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

#########################################PythonTip
'''
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
TCP编程
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示打开了一个"网络链接"，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型
即可。

客户端
大多数链接
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
