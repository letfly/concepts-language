assume cs:code
code segment
    ;将ffff:0006单元中的数赋值到ax寄存器中
    mov ax,0ffffh
    mov ds,ax
    mov bx,6        ;以上，设置ds:bx指向ffff:6
    mov al,[bx]
    mov ah,0        ;以上，设置(al) = ((ds*16)+(bx)),(ah)=0

    ;循环3次，结果存储在dx中
    mov cx,3
s:add dx,ax
    loop s

    ;将程序返回
    mov ax,4c00h
    int 21h

code ends
end
