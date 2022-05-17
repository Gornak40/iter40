section .data
@formatin: db "%d", 0
@formatout: db "%d", 10, 0

section .text
global main
extern printf
extern scanf
extern malloc
extern memset
extern memcpy

; system
%macro @start 0
mov ebp, esp
mov esi, @MEM40
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
mov ecx, dword [%1]
push dword [ecx + eax * 4]
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

%macro @setlvar 1
pop dword [%1]
%endmacro

%macro @lsetarr 1
pop ebx
pop eax
mov ecx, dword [%1]
mov [ecx + eax * 4], ebx
%endmacro

%macro @rsetarr 1
pop ebx
pop eax
mov ecx, dword [%1]
mov [ecx + ebx * 4], eax
%endmacro

%macro @heaparr 1
shl dword [esp], 2
call malloc
add esp, 4
mov dword [%1], eax
%endmacro

%macro @mset 0
shl dword [esp + 8], 2
call memset
add esp, 12
%endmacro

%macro @mcpy 0
shl dword [esp + 8], 2
call memcpy
add esp, 12
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

%macro @mul2 0
shl dword [esp], 1
%endmacro

%macro @div2 0
shr dword [esp], 1
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

%macro @rarrow 0
pop eax
shl eax, 2
add dword [esp], eax
%endmacro

%macro @larrow 0
pop eax
shl eax, 2
sub dword [esp], eax
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
push dword [esp + 4]
%endmacro

%macro @prew 0
push dword[esp + 8]
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

%macro @cmp0 0
pop eax
cmp eax, 0
%endmacro

; mem stack
%macro @meminit 0
pop dword [esi]
add esi, 4
%endmacro

%macro @memgetvar 1
mov eax, dword [%1]
mov [esi], eax
add esi, 4
%endmacro

%macro @memsetvar 1
sub esi, 4
mov eax, dword [esi]
mov dword [%1], eax
%endmacro

%macro @memexit 0
sub esi, 4
push dword [esi]
ret
%endmacro
