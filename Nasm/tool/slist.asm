; 程序操作说明：
; 1、本程序定义：姓名最多个20个字符，学号最多10个字符，成绩最多3位数字
; 2、输入学生信息时，各信息足位时，自动结束；不足位数时，按回车键结束
; 3、输入姓名时，若直接回车，表示结束学生信息输入，进入信息处理
; 本程序在MASMPlus 1.2集成环境下通过编译，经过调试，运行正确。
Assume  CS:Code,DS:Code
Code   Segment
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 功能：显示指定地址（Str_Addr）的字符串
; 入口：
; Str_Addr＝字符串地址（要求在数据段）
; 用法: Output Str_Addr
; 用法举例：Output PromptStr
Output  MACRO Str_Addr
   lea  dx,Str_Addr
   mov  ah,9
   int  21h
   EndM
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 功能：输出一个字符 
; 入口：dl=要显示的字符 
Output_Chr  proc  Near 
   push  ax 
   mov   ah,02h 
   int   21h 
   pop   ax 
   ret 
Output_Chr  endp 
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 功能：输出回车换行
Output_CTLF proc  Near
   push  ax 
   push  dx
   mov   ah,02h
   mov   dl,0dh 
   int   21h
   mov   dl,0ah
   int   21h 
   pop   dx
   pop   ax
   ret
Output_CTLF endp 
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 功能：取光标位置
; 入口：无
; 出口：DH=行号，DL=列号
GetCursor  Proc  Near
           PUSH  AX
           PUSH  BX
           PUSH  CX
           XOR   BX,BX
           MOV   AH,3
           INT   10H
           MOV  Cursor_Row,DH
           MOV  Cursor_Col,DL
           POP  CX
           POP   BX
           POP   AX
           RET
Cursor_Row DB  ?
Cursor_Col DB  ?
GetCursor  EndP
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 功能：置光标位置
; 入口：Cursor_Row=行坐标; Cursor_Col: 列坐标)
SetCursor   Proc  Near
           PUSH  CX
           PUSH  BX
           PUSH  AX
           MOV   DH,Cursor_Row
           MOV   DL,Cursor_Col
           XOR   BX,BX
           MOV   AH,2
           INT   10H
           POP   AX
           POP   BX
           POP  CX
           RET
SetCursor  EndP
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 功能：键盘输入一个指定位数的十进制数字，将其转换成二进制数并保存在指定的内存单元。
; 由于限定最大数据类型为字，所以，数字位数最多：5，最大无符号数：65536
; 约定：直接回车，视为数字0
; 入口：@@Digits=数字位数；di=保存输入的数字首地址
;       @@Type_Data=保存的数据类型，B=字节类型，W=字类型。
; 出口：转换后的二进制数保存在di所指的单元
Input_Digit Proc  Near
CR           equ   000DH
LF           equ   000AH
KBBack       equ   0008H
   push  dx
   push  cx
   push  bx
   push  di
   lea  di,@@Save_Tmp
   push  di
   cld
   mov  cl,@@Digits
   xor  ch,ch
   push  cx
@@Input:  call  GetCursor ;取光标位置
   mov  ah,1 ;从键盘接受一个字符
   int  21h
   cmp  al,CR ;若键入的是回车，已经键入的数字不足N位
   jz  @@ASC_Dec ;转去处理已经键入的数字
   cmp  al,KBBack
   jz  @@KB_Back ;若是回空键，重新输入
   cmp  al,'0'
   jb  @@KBBack ;若低于数字'0'，重新输入
   cmp  al,'9'
   ja  @@KBBack ;若低于数字'9'，重新输入
   jmp  @@Save_Dig
@@KB_Back: dec  Cursor_Col
   inc  cx
   dec  di
@@KBBack:  call  SetCursor ;置光标位置
   jmp  @@Input
@@Save_Dig: and  al,0fh ;转换成二进制数
   stosb ;保存
   loop  @@Input ;接受下一个数字
@@ASC_Dec: mov  ax,cx
   pop  cx
   pop  si
   sub  cx,ax ;实际输入的数字位数
   xor  bp,bp
   xor  dx,dx
   xor  ax,ax
   jcxz  @@Save_Ret ;若直接回车，没有输入任何数字，按输入'0'处理
   dec  cx ;实际输入的数字位数减1，准备把输入的这一串数字转换成二进制数
   jcxz  @@One_Digit ;若输入的数字只有一位，转去直接保存这个二进制数
   mov  bx,10
@@Mul_Ten: lodsb
   cbw
   add  ax,bp
   mul  bx
   mov  bp,ax
   loop  @@Mul_Ten
@@One_Digit: lodsb
   cbw
   add  ax,bp
@@Save_Ret: pop  di
   cmp  @@Type_Data,'B' ;字节类型？
   jz  $+5
   stosw
   jmp  $+3
   stosb
   pop  bx
   pop  cx
   pop  dx
   ret
@@Digits  db  ? ;十进制数字位数
@@Type_Data db  'B' ;保存的数据类型。B=字节类型，W=字类型
@@Save_Tmp db  16 dup(?)
Input_Digit EndP
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 功能：把AX中的二进制无符号数转换成显式的十进制ASCII码，并送显示屏显示
; 入口：AX=二进制数 
; 出口：在当前光标位置显示转换后的ASCII码数字 
Dec_ASCII  Proc  Near 
   push  dx 
   push  bx 
   push  di
   mov   bx,10 
   lea   di,@@Temp_Save[6] 
   mov   BYTE ptr [di],'$' 
   dec   di 
@@Divide:  xor   dx,dx 
   div   bx 
   or   dl,30h 
   mov   [di],dl 
   dec   di 
   test  ax,0ffffh 
   jnz   @@Divide 
   inc   di 
   push  di 
   pop   dx 
   mov   ah,9 
   int   21h 
   pop   di 
   pop   bx 
   pop   dx 
   ret 
@@Temp_Save  db   7 dup(?)
Dec_ASCII  EndP
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 功能：把AL中的二进制无符号数作为小数转换成显式的十进制ASCII码，
; 并送显示屏显示，未考虑四舍五入
; 入口：AH=二进制数，BH=除数，CX=保留小数位数
; 出口：在当前光标位置显示转换后的ASCII码数字 
Dec_Frac  Proc  Near
   push  ax
   mov  dl,'.'
   call  Output_Chr ;显示一个小数点
   pop  ax
   mov  bl,10 ;乘数
@@Dec_Frac: mov  al,ah ;余数不为0，处理小数部分
   mul  bl ;余数乘10，继续做除法
   div  bh ;除以除数，取商数作为结果的一位小数
   or  al,30h
   mov  dl,al
   call  Output_Chr ;显示一位小数
   loop  @@Dec_Frac
   ret
Dec_Frac  EndP
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
Name_Length  equ  20 ;姓名长度
ID_Length  equ  10 ;学号长度
Info_Students Struc ; 学生信息结构类型
Name_Student db  Name_Length dup(?) ;姓名
ID_Student db  ID_Length dup(?) ;学号
Score_Student db  ? ;成绩
Info_Students EndS
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
Prompt_Str  db    7,'Name',Name_Length-4+2 dup(20h) ;姓名标题字符串
   db  'Student ID',2 dup(20h) ;学号标题字符串
   db  'Score',CR,LF ;成绩标题字符串
   db  Name_Length dup('-'),2 dup(20h)
   db  ID_Length dup('-'),2 dup(20h)
   db  5 dup('-'),CR,LF,'$'
Temp_Cursor dw  ? ;输入、显示学生信息光标位置
prompt_Ave db  CR,LF,'Average: $' ;提示显示平均分
Buffer_Data db  ?,?,Name_Length+2 dup(?) ;姓名、学号输入缓冲区
Press_Key  db    CR,LF,CR,LF,'Press any key to exit...$' 
Start:    push  cs
   pop  ds
   push  cs
   pop  es ;使数据段、附加段与代码段同段
   mov  @@Digits,3 ;十进制数字位数
   mov  @@Type_Data,'B' ;保存的数据类型。B=字节类型，W=字类型
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 显示姓名、学号、成绩标题，提示输入学生信息
   Output Prompt_Str
   call  GetCursor ;取光标位置
   mov  Temp_Cursor,dx ;保存输入、显示学生信息光标位置
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 输入学生姓名、学号、成绩
   lea  di,Score_Table ;姓名、学号、成绩存放地址
Input_Name: call  GetCursor ;取光标位置
   mov  Buffer_Data,Name_Length+1 ;允许输入的最多字符数
   push di
   lea  di,Buffer_Data[2]
   mov  cx,(Name_Length+2)/2
   mov  ax,2020h ;填充空格
   rep  stosw
   pop  di
   lea  dx,Buffer_Data ;姓名输入缓冲区地址
   mov  ah,0ah
   int  21h
   lea  si,Buffer_Data[1]
   lodsb ;读入实际输入的字符个数
   test  al,al
   jz  @@L1 ;若输入学生姓名时，直接回车，认为学生姓名、学号、成绩等输入结束，转去计算输入的学生人数
   mov  cx,Name_Length ;姓名字符数
   rep  movsb ;写入学生信息缓冲区
   add  Cursor_Col,Name_Length+2 ;列号加姓名长度再加2，开始输入学号
   call  SetCursor ;置光标位置
   push di
   lea  di,Buffer_Data[2]
   mov  cx,(Name_Length+2)/2
   mov  ax,2020h ;填充空格
   rep  stosw
   pop  di
   lea  dx,Buffer_Data ;学号输入缓冲区地址
   mov  ah,0ah
   int  21h
   lea  si,Buffer_Data[2]
   mov  cx,ID_Length ;学号字符数
   rep  movsb ;写入学生信息缓冲区
   add  Cursor_Col,ID_Length+2 ;列号加学号长度再加2，开始输入成绩
   call  SetCursor ;置光标位置
   call  Input_Digit ;输入成绩
   call  Output_CTLF ;输出一个回车、换行
   jmp  Input_Name ;输入下一名学生信息
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 计算输入的学生人数
@@L1:  mov  ax,di
   sub  ax,offset Score_Table ;所有学生信息所占内存容量
   mov  bl,type Info_Students ;每名学生信息所占内存容量
   div  bl
   mov  cx,ax ;CX=输入的学生人数
   test  cx,cx
   jnz  @@L00
   jmp  Exit_Proc ;若未输入任何信息，直接结束程序
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 建立学生信息链表
@@L00:  push  di ;保存链表地址
   lea  ax,Score_Table ;学生信息起始地址
   push  cx
@@L2:  stosw ;保存学生信息地址
   add  ax,type Info_Students ;每名学生信息所占内存容量
   loop  @@L2
   pop  cx
   pop  si ;弹出链表地址给si
   cmp  cx,2
   jb  Exit_Proc ;若只输入了1名学生的信息，则无须排序和显示结果 
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 用冒泡排序法按成绩降序排序
   push  si ;入栈保存链表地址
   push  cx ;保存学生人数
   dec  cx ;准备用冒泡排序法排序
@@Sorting:  push  cx ;入栈保存外循环次数
     push  si ;入栈保存数组地址
@@Compare:   push  si
     pop   di ;当前数组元素地址赋给目的变址寄存器，以备交换之用
   lodsw ;将当前学生信息地址读入AX
   mov  bx,ax
   mov  al,[bx.Score_Student] ;将当前学生成绩读入AL
   mov  bx,[si] ;相邻的下一个学生信息地址
     cmp   al,[bx.Score_Student] ;当前学生成绩与相邻的下一个学生成绩相比较
   jae  @@NextOne ;若大于或等于，不作数据交换，处理下一个数组元素
         mov  ax,[di] ;若小于，读入当前学生信息链表节点
         xchg  ax,[si] ;交换链表元素
   mov  [di],ax ;保存数值较大者节点地址
@@NextOne:  loop  @@Compare ;处理下一个数组元素
   pop  si ;数组地址出栈
     pop   cx ;外循环次数出栈
     loop  @@Sorting ;下一趟比较
     call  Output_CTLF
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 按成绩降序显示所有学生信息
   Output Prompt_Str ;显示学生信息标题
   call  GetCursor ;取光标位置
   mov  Temp_Cursor,dx ;保存显示学生信息光标位置
     pop  cx ;弹出学生人数
     pop  si ;弹出链表地址
   push  cx ;保存学生人数
     xor  bx,bx ;总成绩初值
@@List_Info: push  cx ;保存学生人数
   call  GetCursor ;取光标位置
   lodsw ;读入链表的一个节点
   push  si ;入栈保存链表地址
   mov  si,ax
   push  si ;入栈保存学生信息地址
   lea  si,[si.Name_Student] ;姓名地址
   mov  cx,Name_Length ;姓名字符串长度
@@Dsip_Name: lodsb ;读入一个字符
   cmp  al,0dh ;回车符？
   jz  @@L3 ;是，姓名显示结束
   mov  dl,al
   call  Output_Chr ;显示一个字符
   loop  @@Dsip_Name ;下一个字符
@@L3:  add  Cursor_Col,Name_Length+2 ;列号加姓名长度再加2，开始显示学号
   call  SetCursor ;置光标位置
   pop  si ;弹出学生信息地址
   push  si ;入栈保存学生信息地址
   lea  si,[si.ID_Student] ;学号地址
   mov  cx,ID_Length ;姓名字符串长度
@@Dsip_ID: lodsb ;读入一个字符
   cmp  al,0dh ;回车符？
   jz  @@L4 ;是，学号显示结束
   mov  dl,al
   call  Output_Chr ;显示一个字符
   loop  @@Dsip_ID ;下一个字符
@@L4:  add  Cursor_Col,ID_Length+2 ;列号加学号长度再加2，开始显示成绩
   call  SetCursor ;置光标位置
   pop  si ;弹出学生信息地址
   lea  si,[si.Score_Student] ;成绩地址
   lodsb ;读入成绩
   xor  ah,ah
   add  bx,ax ;累加总成绩
   call  Dec_ASCII ;把AX中的二进制无符号数转换成显式的十进制ASCII码，并送显示屏显示
   call  Output_CTLF
   pop  si ;弹出链表地址
     pop  cx ;弹出学生人数
   loop  @@List_Info ;下一个节点（学生信息）
   call  Output_CTLF
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
; 计算并显示平均分
   Output prompt_Ave ;提示显示平均分
     mov  ax,bx
     pop  bx ;弹出学生人数
   div  bl ;平均分取整数部分
   mov  bh,ah ;保存余数
   xor  ah,ah
   call  Dec_ASCII ;显示平均分
   mov  ah,bh ;余数
   mov  bh,bl ;除数
   mov  cx,2 ;保留小数位数
   call  Dec_Frac ;把AL中的二进制无符号数作为小数转换成显式的十进制ASCII码
; －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
Exit_Proc: Output Press_Key ;提示操作完成，按任意键结束程序
   mov  ah,1
   int  21h
   mov  ah,4ch ;结束程序
   int  21h
Score_Table: ;学生成绩存储区
Code   ENDS
   END  Start ;编译到此结束
