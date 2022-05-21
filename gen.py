#!venv/bin/python
from random import *
from sys import argv
n = int(argv[1])
arr = [randint(-int(1e9), int(1e9)) for _ in range(n)]
print(n)
print(*arr)
