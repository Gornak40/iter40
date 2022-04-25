section .data
	_formatin: db "%d", 0
	_formatout: db "%d", 10, 0

section .bss
	_stackptr: resd 1
	arr: resd 10

section .text
	global main
	extern printf
	extern scanf

%macro _start 0
	mov [_stackptr], esp
%endmacro

%macro _exit 0
	mov esp, [_stackptr]
	xor eax, eax
%endmacro

%macro _num 1
	push %1
%endmacro

%macro _var 1
	push dword [%1]
%endmacro

%macro _const 1
	push dword [%1]
%endmacro

%macro _get 1
	pop eax
	push dword [%1 + eax * 4]
%endmacro

%macro _add 0
	pop ebx
	add [esp], ebx
%endmacro

%macro _sub 0
	pop ebx
	sub [esp], ebx
%endmacro

%macro _mul 0
	pop ebx
	pop eax
	imul ebx
	push eax
%endmacro

%macro _div 0
	xor edx, edx
	pop ebx
	pop eax
	idiv ebx
	push eax
%endmacro

%macro _mod 0
	xor edx, edx
	pop ebx
	pop eax
	idiv ebx
	push edx
%endmacro

%macro _xor 0
	pop ebx
	xor [esp], ebx
%endmacro

%macro _and 0
	pop ebx
	and [esp], ebx
%endmacro

%macro _or 0
	pop ebx
	or [esp], ebx
%endmacro

%macro _shl 0
	pop ebx
	shl [esp], ebx
%endmacro

%macro _shr 0
	pop ebx
	shr [esp], ebx
%endmacro

%macro _inc 0
	inc dword [esp]
%endmacro

%macro _dec 0
	dec dword [esp]
%endmacro

%macro _read 0
	sub esp, 4
	mov [esp], esp
	push dword _formatin
	call scanf
	add esp, 4
%endmacro

%macro _post 0
	push dword _formatout
	call printf
	add esp, 8
%endmacro

%macro _cmp 0
	pop ebx
	pop eax
	cmp eax, ebx
%endmacro

%macro _set 1
	pop ebx
	pop eax
	mov [%1 + eax * 4], ebx
%endmacro

%macro _copy 0
	push [esp]
%endmacro

%macro _swap 0
	pop ebx
	pop eax
	push ebx
	push eax
%endmacro

main:
	_start

	_read
	_read
;	_shr
	_post

	_exit
