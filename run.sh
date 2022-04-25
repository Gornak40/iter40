#!/usr/bin/sh
nasm -f elf32 $1 -o main.o && gcc -m32 main.o -o main && ./main

