# math.gcd
# grid=defaultdict(lambda : defaultdict(int))
# @functools.lru_cache(maxsize=None)
import sys,typing,re,random,math,functools
from collections import defaultdict
from copy import deepcopy
sys.setrecursionlimit(100000)
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
def print_grid(z):
    min_x = min(a[1] for a in z)
    max_x = max(a[1] for a in z)
    min_y = min(a[0] for a in z)
    max_y = max(a[0] for a in z)
    for i in range(min_y, max_y+1):
        s = ""
        for j in range(min_x, max_x+1):
            s += " #23456789"[z[(i,j)]]
        print(s)
def process(mem, ins, A = 0, B = 0, C = 0):
    if ins == 'addr':
        mem[C] = mem[A] + mem[B]
    elif ins == 'addi':
        mem[C] = mem[A] + B
    elif ins == 'mulr':
        mem[C] = mem[A] * mem[B]
    elif ins == 'muli':
        mem[C] = mem[A] * B
    elif ins == 'banr':
        mem[C] = mem[A] & mem[B]
    elif ins == 'bani':
        mem[C] = mem[A] & B
    elif ins == 'borr':
        mem[C] = mem[A] | mem[B]
    elif ins == 'bori':
        mem[C] = mem[A] | B
    elif ins == 'setr':
        mem[C] = mem[A]
    elif ins == 'seti':
        mem[C] = A
    elif ins == 'gtir':
        mem[C] = int(A > mem[B])
    elif ins == 'gtri':
        mem[C] = int(mem[A] > B)
    elif ins == 'gtrr':
        mem[C] = int(mem[A] > mem[B])
    elif ins == 'eqir':
        mem[C] = int(A == mem[B])
    elif ins == 'eqri':
        mem[C] = int(mem[A] == B)
    elif ins == 'eqrr':
        mem[C] = int(mem[A] == mem[B])
inp = open("input").readlines()
prog = []
for i in range(len(inp)):
    line = inp[i]
    prog.append([line.split()[0], ints(line)])
prog = prog[1:]
mem = [0] * 6
mem[0] = 1
inc = 1

while 0 <= mem[inc] < len(prog):
    u = mem[inc]
    #print(u, mem, prog[u])
    print(mem)
    # from time import sleep
    # sleep(0.05)
    process(mem, prog[mem[inc]][0], *prog[mem[inc]][1])
    mem[inc] += 1
print(mem)
