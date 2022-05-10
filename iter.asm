section .data
@formatin: db "%d", 0
@formatout: db "%d", 10, 0

section .text
global main
extern printf
extern scanf
extern malloc

; system
%macro @start 0
mov ebp, esp
%endmacro

%macro @exit 0
mov esp, ebp
xor eax, eax
%endmacro

; get
%macro @num 1
push %1
%endmacro

%macro @getvar 1
push dword [%1]
%endmacro

%macro @getconst 1
push %1
%endmacro

%macro @getarr 1
pop eax
push dword [%1 + eax * 4]
%endmacro

%macro @read 0
sub esp, 4
mov [esp], esp
push dword @formatin
call scanf
add esp, 4
%endmacro

; set
%macro @setvar 1
pop dword [%1]
%endmacro

%macro @lsetarr 1
pop ebx
pop eax
mov [%1 + eax * 4], ebx
%endmacro

%macro @rsetarr 1
pop ebx
pop eax
mov [%1 + ebx * 4], eax
%endmacro

%macro @heaparr 1
shl dword [esp], 2
call malloc
add esp, 4
mov [%1], eax
%endmacro

; (a)
%macro @inc 0
inc dword [esp]
%endmacro

%macro @dec 0
dec dword [esp]
%endmacro

%macro @not 0
not dword [esp]
%endmacro

; (a, b)
%macro @add 0
pop ebx
add [esp], ebx
%endmacro

%macro @sub 0
pop ebx
sub [esp], ebx
%endmacro

%macro @mul 0
pop ebx
pop eax
imul ebx
push eax
%endmacro

%macro @div 0
xor edx, edx
pop ebx
pop eax
idiv ebx
push eax
%endmacro

%macro @mod 0
xor edx, edx
pop ebx
pop eax
idiv ebx
push edx
%endmacro

%macro @xor 0
pop ebx
xor [esp], ebx
%endmacro

%macro @and 0
pop ebx
and [esp], ebx
%endmacro

%macro @or 0
pop ebx
or [esp], ebx
%endmacro

%macro @shl 0
pop ecx
shl dword [esp], cl
%endmacro

%macro @shr 0
pop ecx
shr dword [esp], cl
%endmacro

; (a, b, c)
%macro @muldiv 0
pop ecx
pop ebx
pop eax
imul ebx
idiv ecx
push eax
%endmacro

%macro @mulmod 0
pop ecx
pop ebx
pop eax
imul ebx
idiv ecx
push edx
%endmacro

; stack
%macro @copy 0
push dword [esp]
%endmacro

%macro @prev 0
push dword [esp+4]
%endmacro

%macro @swap 0
pop ebx
pop eax
push ebx
push eax
%endmacro

%macro @push 0
pop ebx
pop eax
push ebx
push eax
push ebx
%endmacro

%macro @drop 0
add esp, 4
%endmacro

%macro @post 0
push dword @formatout
call printf
add esp, 8
%endmacro

; conditions
%macro @cmp 0
pop ebx
pop eax
cmp eax, ebx
%endmacro

main:
@start