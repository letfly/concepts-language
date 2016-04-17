assume cs:code
code segment
    ;将ffff:0000单元中的数赋值到ax寄存器中
    mov ax,0ffffh
    mov ds,ax
    mov bx,0

    ;循环将ffff:0000-ffff:000B单元中的数赋值到ax寄存器，并加至dx
    mov cx,12
s:  mov al,[bx]
    mov ah,0
    add dx,ax
    inc bx
    loop s

    ;将程序返回
    mov ax,4c00h
    int 21h
code ends
end
