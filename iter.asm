section .data
	_formatin: db "%d", 0
	_formatout: db "%d", 10, 0

section .bss
	_stackptr: resd 1

section .text
	global main
	extern printf
	extern scanf
	extern malloc

; system
%macro _start 0
	mov [_stackptr], esp
%endmacro

%macro _exit 0
	mov esp, [_stackptr]
	xor eax, eax
%endmacro

; get
%macro _num 1
	push %1
%endmacro

%macro _getvar 1
	push dword [%1]
%endmacro

%macro _const 1
	push dword [%1]
%endmacro

%macro _getarr 1
	pop eax
	push dword [%1 + eax * 4]
%endmacro

%macro _read 0
	sub esp, 4
	mov [esp], esp
	push dword _formatin
	call scanf
	add esp, 4
%endmacro

; set
%macro _setvar 1
	pop dword [%1]
%endmacro

%macro _setarr 1
	pop ebx
	pop eax
	mov [%1 + eax * 4], ebx
%endmacro

%macro _heaparr 1
	shl dword [esp], 2
	call malloc
	add esp, 4
	mov [%1], eax
%endmacro

; (a)
%macro _inc 0
	inc dword [esp]
%endmacro

%macro _dec 0
	dec dword [esp]
%endmacro

%macro _not 0
	not dword [esp]
%endmacro

; (a, b)
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
	pop ecx
	shl dword [esp], cl
%endmacro

%macro _shr 0
	pop ecx
	shr dword [esp], cl
%endmacro

; (a, b, c)
%macro _muldiv 0
	pop ecx
	pop ebx
	pop eax
	imul ebx
	idiv ecx
	push eax
%endmacro

%macro _mulmod 0
	pop ecx
	pop ebx
	pop eax
	imul ebx
	idiv ecx
	push edx
%endmacro

; stack
%macro _copy 0
	push dword [esp]
%endmacro

%macro _prev 0
	push dword [esp+4]
%endmacro

%macro _swap 0
	pop ebx
	pop eax
	push ebx
	push eax
%endmacro

%macro _push 0
	pop ebx
	pop eax
	push ebx
	push eax
	push ebx
%endmacro

%macro _drop 0
	add esp, 4
%endmacro

%macro _post 0
	push dword _formatout
	call printf
	add esp, 8
%endmacro

; conditions
%macro _cmp 0
	pop ebx
	pop eax
	cmp eax, ebx
%endmacro

main:
	_start

	_exit
