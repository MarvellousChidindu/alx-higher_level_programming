#!/usr/bin/python3

from sys import argv

# add = __import__ ("main").add
# sub = __import__ ("main").sub
# mul = __import__ ("main").mul
# div = __import__ ("main").div

# from main import add, sub, mul, div
from main import *

print(argv)

operant = argv[1]
a = argv[2]
b = argv[3]

if (operant == "add"):
    print(add(int(a), int(b)))
elif (operant == "sub"):
    print(sub(int(a), int(b)))
elif (operant == "mul"):
    print(mul())
else:
    print(div(int(a), int(b)))
