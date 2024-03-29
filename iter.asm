section .data
@formatin: db "%d", 0
@formatout: db "%d", 10, 0

section .text
global main
extern printf
extern scanf
extern malloc
extern free
extern memset
extern memcpy
extern memcmp

; avx2
%macro @avx2_add 0
pop eax
vmovdqu ymm1, [eax]
vpaddd ymm0, ymm0, ymm1
%endmacro

%macro @avx2_sub 0
pop eax
vmovdqu ymm1, [eax]
vpsubd ymm0, ymm0, ymm1
%endmacro

%macro @avx2_mul 0
pop eax
vmovdqu ymm1, [eax]
vpmulld ymm0, ymm0, ymm1
%endmacro

%macro @avx2_xor 0
pop eax
vmovdqu ymm1, [eax]
vpxor ymm0, ymm0, ymm1
%endmacro

%macro @avx2_and 0
pop eax
vmovdqu ymm1, [eax]
vpand ymm0, ymm0, ymm1
%endmacro

%macro @avx2_or 0
pop eax
vmovdqu ymm1, [eax]
vpor ymm0, ymm0, ymm1
%endmacro

%macro @avx2_min 0
pop eax
vmovdqu ymm1, [eax]
vpminsd ymm0, ymm0, ymm1
%endmacro

%macro @avx2_max 0
pop eax
vmovdqu ymm1, [eax]
vpmaxsd ymm0, ymm0, ymm1
%endmacro

%macro @avx2_cmpeq 0
pop eax
vmovdqu ymm1, [eax]
vpcmpeqd ymm0, ymm0, ymm1
%endmacro

%macro @avx2_cmpgt 0
pop eax
vmovdqu ymm1, [eax]
vpcmpgtd ymm0, ymm0, ymm1
%endmacro

%macro @avx2_load 0
pop eax
vmovdqu ymm0, [eax]
%endmacro

%macro @avx2_store 0
pop eax
vmovdqu [eax], ymm0
%endmacro

%macro @avx2_set1 0
pop eax
mov dword [@AVX2], eax
mov dword [@AVX2 + 4], eax
mov dword [@AVX2 + 8], eax
mov dword [@AVX2 + 12], eax
mov dword [@AVX2 + 16], eax
mov dword [@AVX2 + 20], eax
mov dword [@AVX2 + 24], eax
mov dword [@AVX2 + 28], eax
vmovdqu ymm0, [@AVX2]
%endmacro

; system
%macro @start 0
mov ebp, esp
mov esi, @MEM40
%endmacro

%macro @exit 0
mov esp, ebp
xor eax, eax
ret
%endmacro

; get
%macro @num 1
push %1
%endmacro

%macro @getvar 1
push dword [%1]
%endmacro

%macro @getaddr 1
push %1
%endmacro

%macro @getconst 1
push %1
%endmacro

%macro @getptr 0
pop eax
push dword [eax]
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

%macro @lsetptr 0
pop ebx
pop eax
mov dword [eax], ebx
%endmacro

%macro @rsetptr 0
pop ebx
pop eax
mov dword [ebx], eax
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

%macro @swapptr 0
pop ebx
pop eax
mov ecx, dword [ebx]
mov edx, dword [eax]
mov dword [ebx], edx
mov dword [eax], ecx
%endmacro

%macro @heap 0
shl dword [esp], 2
call malloc
add esp, 4
push eax
%endmacro

%macro @heaparr 1
shl dword [esp], 2
call malloc
add esp, 4
mov dword [%1], eax
%endmacro

%macro @free 0
call free
add esp, 4
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

%macro @mcmp 0
shl dword [esp + 8], 2
call memcmp
add esp, 12
push eax
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
sar dword [esp], 1
%endmacro

%macro @incptr 0
add dword [esp], 4
%endmacro

%macro @decptr 0
sub dword [esp], 4
%endmacro

%macro @bcnt 0
pop eax
popcnt ebx, eax
push ebx
%endmacro

%macro @bclz 0
pop ebx
bsr eax, ebx
xor eax, 31
push eax
%endmacro

%macro @bctz 0
pop ebx
bsf eax, ebx
push eax
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

; not working for negative number
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
push edi
%endmacro

%macro @save 0
mov edi, dword [esp]
%endmacro

%macro @pick 0
pop edi
%endmacro

%macro @drop 0
add esp, 4
%endmacro

%macro @kill 0
pop eax
mov dword [esp], eax
%endmacro

%macro @post 0
push dword @formatout
call printf
add esp, 8
%endmacro

%macro @dump 0
pop eax
pop ecx
shl ecx, 2
mov ebx, esp
push ecx
push ebx
push eax
call memcpy
add esp, 8
pop ecx
add esp, ecx
%endmacro

%macro @minc 0
pop eax
inc dword [eax]
%endmacro

%macro @mdec 0
pop eax
dec dword [eax]
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
