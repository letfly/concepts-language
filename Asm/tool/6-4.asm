assume cs:code,ds:data,ss:stack
data segment
    dw 0123h,0456h,0789h,0abch,0defh,0fedh,0cbah,0987h
data ends
stack segment
    dw 0,0,0,0,0,0,0,0
stack ends
code segment
start:  mov ax,stack
        mov ss,ax
        ;设置栈顶ss:sp指向stack:16
        mov sp,16
        mov ax,data
        ;ds指向data段
        mov ds,ax
        ;ds:bx指向data段中的第一个单元
        mov bx,0

        ;以上data段中的0-16但愿中的8个字型数据依次入栈
        mov cx,8
    s:  push [bx]
        add bx,2
        loop s

        mov bx,0
        mov cx,8
    s0: pop [bx]
        add bx,2
        loop s0

        mov ax,4c00h
        int 21h
code ends
end start
