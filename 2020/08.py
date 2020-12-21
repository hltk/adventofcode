from utils import *
from aocd import data

lines = data.split("\n")

seen = set()
it = 0
acc = 0
while it not in seen:
    seen.add(it)
    a, b = lines[it].split()
    if a == "acc":
        acc += int(b)
    elif a == "jmp":
        it += int(b) - 1
    it += 1
print(acc)

for i in range(len(lines)):
    seen = set()
    it = 0
    acc = 0
    while 0 <= it < len(lines) and it not in seen:
        seen.add(it)
        a, b = lines[it].split()
        if it == i:
            a = "jmp" if a == "nop" else "nop"
        if a == "acc":
            acc += int(b)
        elif a == "jmp":
            it += int(b) - 1
        it += 1
    if not (0 <= it < len(lines)):
        print(acc)
