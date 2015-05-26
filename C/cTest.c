//////////////////////////////////结构体
#include<stdio.h>
#include<string.h>

/*struct Books{
	char title[50];
	char author[50];
	char subject[100];
	int book_id;
}Book1,Book2;*/
// 访问结构体成员
/*int main(){
	// Book1 详述 
	strcpy(Book1.title, "C Programming");
	strcpy(Book1.author, "letfly");
	strcpy(Book1.subject, "C Programming Tutorial");
	Book1.book_id = 6495407;

	// Book2 详述
	strcpy(Book2.title, "C Programming");
	strcpy(Book2.author, "letfly");
	strcpy(Book2.subject, "C Programming Tutorial");
	Book2.book_id = 6495408;

	// 输出 Book1 信息
	printf("Book 1 title : %s\n", Book1.title);
	printf("Book 1 author : %s\n", Book1.author);

	return 0;
}*//*

// 结构作为函数参数
// 声明printBook()函数
void printBook(struct Books book);
int main(){
	// Book1 详述
	strcpy(Book1.title, "C Programming");
	strcpy(Book1.author, "letfly");
	strcpy(Book1.subject, "C Programming Tutorial");
	Book1.book_id = 6495407;
	
	// Book2 详述 
	strcpy(Book2.title, "C Programming");
	strcpy(Book2.author, "letfly");
	strcpy(Book2.subject, "C Programming Tutorial");
	Book1.book_id = 6495408;

	// 输出Book1信息 
	printBook(Book1);
	// 输出Book2信息
	printBook(Book2);
}
void printBook(struct Books book){
	printf("Bookt title : %s\n", book.title);
}*/

// 指向结构的指针
/*struct Books{
	char title[50];
	char author[50];
	char subject[100];
	int book_id;
};
void printBook(struct Books *book);
int main(){
	struct Books Book1; //声明Book1
	struct Books Book2; //声明Book2

	strcpy(Book1.title, "C Programming");
	strcpy(Book1.author, "Nuba Ali");
	Book1.book_id = 6;

	// Book2 详述
	strcpy(Book2.title, "Telecom");
	strcpy(Book2.author, "Zara Ali");
	Book2.book_id = 7;
	
	printBook(&Book1);
}
void printBook(struct Books *book){
	printf("title: %s\n", book->title);
	printf("author: %s\n", book->author);
}*/
////////////////////////////////////////指针
/*int main(){
	int var1;
	char var2[10];

	printf("var1 变量的地址： %x\n", &var1);
	printf("var2 变量的地址： %x\n", &var2);
	printf("var2 变量的地址： %x\n", &var2[0]);
	printf("var2 变量的地址： %x\n", &var2[1]);

	return 0;
}*/
// 如何使用指针？
/*int main(){
	int var = 20;  //实际变量的声明
	int *ip;  //指针变量的声明

	ip = &var;  //在指针变量中存储var的地址

	printf("Address of var variable: %p\n", &var);

	// 在指针变量中存储的地址
	printf("Address stored in ip variable: %p\n", ip);
	// 使用指针访问值
	printf("Value of *ip variable: %d\n", *ip);
	
	return 0;
}*/
// C中的NULL指针
/*int main(){
	int *ptr = NULL;

	printf("ptr的值是 %x\n", ptr);
}*/

/////////////////////////////////////////typedef
// 基础概念
/*typedef struct Books{
	char title[50];
	char author[50];
	char subject[100];
	int book_id;
}Book;
int main(){
	Book book;  //声明变量book，类型为Book

	strcpy(book.title, "C Programming");

	printf(book.title);
}*/
// typedef vs #define
/*#define TRUE 1
#define FALSE 0
int main(){
	printf("Value of TRUE: %d\n", TRUE);
	printf("%d",FALSE);
}*/
// C指针详解

//       从函数返回指针
/*#include <time.h>
#include <stdlib.h>

// 要生成和返回随机数的函数
int *getRandom(){
	static int r[10];
	int i;

	// 设置种子
	//srand((unsigned)time(NULL));
	for (i=0; i<10; ++i){
		r[i] = rand();
		printf("%d\n", r[i]);
	}
	return r;
}
// 要调用上面定义函数的主函数
int main(){
	// 一个指向整数的指针
	int *p;
	int i;

	p = getRandom();
	for(i=0; i<10; i++){
		printf("*(p + [%d]): %d\n", i, *(p+i));
	}
	return 0;
}*/

//////////////////////////////////////C预处理器
//       预处理器实例
/*#define MAX_ARRAY 20

#include <stdio.h>
#include "myheader.h"

#undef FILE_SIZE
#define FILE_SIZE

#ifndef MESSAGE
	#define MESSAGE "You wish!"
#endif

#ifdef DEBUG
	//Your debugging
#endif*/
// 预定义宏
/*#include <stdio.h>

int main(){
	printf("%s\n", __FILE__);
	printf("%s\n", __DATE__);
	printf("%s\n", __TIME__);
}*/
// 预处理器运算符
/*// 宏延续运算符(\)
#define message_for(a, b)\
	printf(#a " and " #b ": We love you!\n")
// 字符串常量运算符(#)
#include <stdio.h>
#define message_for(a, b)\
	printf(#a " and " #b ": We love you!\n")

int main(void){
	message_for(fyf,letfly);
}
// 标记粘贴运算符(##)
#include <stdio.h>
#define tokenpaster(n) printf("token" #n " = %d",token##n)

int main(){
	int token34 = 40;

	tokenpaster(34);
	return 0;
}
//defined()运算符
#include <stdio.h>
#if !defined (MESSAGE)
	#define MESSAGE "You wish!"
#endif

int main(){
	printf("MESSAGE: %s\n",MESSAGE);
	return 0;
}*/
// 参数化的宏
/*#include <stdio.h>
#define MAX(x,y) ((x) > (y) ? (x):(y))

int main(void){
	int a = 10,b = 20;
	printf("Max between %d and %d is %d\n", a, b, MAX(a, b));
}*/


部分代码如下：char *s;
cout<<"请输入字符串，以'\n'结束";
cin.getline(s, 1000, '\n');cin.getline(s, 1000, '\n');
哪里有问题吗
getline()函数有两个版本，关于这个三个参数的版本，它的第一个参数是指向字符数组的指针，因为你
定义的是：char *s(只说明s是指向字符类型的指针，但没有说明它是指向祖父数组的)，这样能通过
编译，但会运行错误，因为编译器在编译时不知道s是指向字符数组的，它以为是指向一个字符的，就
只为s所指向的内容分配一个字节的内存，这样当运行时，程序存那1000个字符是这样做的：先找到s
所指向的内存，也就是之前分配的一个字节，存入第一个字符，然后按这个内存地址的顺序继续往下
存余下的字符(因为数组是地址连续的)，但这时就可能出现错误，因为除了第一个内存是之前分配
了的，其他的内存都是未分配的，但又可能是已经存储了其他数据的，所以会出错。而且是可能出错，
因为是可能已经存储了其他数据。



对PyObject的认识
最近一直在看《python源码剖析》，现在将自己的认识一步步记录下来，既方便大家分享讨论，共同进步，也方便
我自己以后的回顾复习

对象是Python中非常重要的一个概念，需要明确的是在Python中任何事物都是对象(包括类型对象，yes,10是一个
对象，10的类型int也是一个对象)。我们知道，python是用c来实现的，那么具体这个对象在源代码里面是怎么样表示
的呢？
[object.h]
typedef struct _object{
	int ob_refcnt;
	struct _typeobject *ob_type;
}PyObject;

PyObject非常简单，这个struct只包含两个元素，一个是用来记录引用次数的(以此来做垃圾回收，但不是引用为0
就会释放空间，还有内存池这个玩意)，另一个用来指明这个对象的type。这是所有python object共有的一部分，所以
在源代码的内部相互传递对象的时候，所有对象都能用PyObject*来表示，非常简洁明了，同时这个ob_type指明了这
个对象的类型，从而实现了c语言不提供但c++提供的多态特性(里面用大量的函数指针实现)

Python对象分定长和不定长。定长的，可想而知，int这种肯定是，sizeof(1)和 sizeof(10)肯定是一样的，那么不定
长的呢，也很容易想到c++里面的string嘛，"x"和"world"这两个肯定长度不一样。那Python是怎么表示这两种类
型的呢？下面是不定长的源码：
[object.h]
#define PyObject_VAR_HEAD   \
	PyObject_HEAD   \
	int ob_size;   /* Number of items in variable part */

typedef 
