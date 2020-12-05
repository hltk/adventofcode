# math.gcd
# grid=defaultdict(lambda : defaultdict(int))
# @functools.lru_cache(maxsize=None)
# Queue(), PriorityQueue()
# Queue:
#    put, get
#     while not Queue().empty():
# itertools:
#    cycle
#    chain
#    product, permutations, combinations, combinations_with_replacement
# deque
#     append, appendleft, pop, popleft
# Counter:
#     most_common(3)
#     elements
# nonlocal, global, copy, deepcopy!!
# B, Z = 0, 1 << 21
# while Z:
#     if ok(B + Z): B += Z
#     Z //= 2
# functools.reduce(f, [1, 2, 3]) = f(f(1, 2), 3)
# See itertools.accumulate() for an iterator that yields all intermediate values.
import sys, typing, re, random, math, functools, cmath
from string import ascii_lowercase, ascii_uppercase
from queue import Queue, PriorityQueue
from collections import defaultdict, deque, Counter
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
lines = open("input").readlines()
L = []
for l in lines:
    if 'cut' in l: L.append([0, ints(l)[0]])
    elif 'deal into new stack' in l: L.append([1, 0])
    elif 'deal with increment' in l: L.append([2, ints(l)[0]])
def simulate(N, it):
    global L
    for a, b in L:
        if a == 0: it = (it - b + N) % N
        elif a == 1: it = (N - it - 1)
        elif a == 2: it = (it * b) % N
        else: assert False
    return it
N = 119315717514047
it = 2020
vis = set()
amt = 0
z = 0
A = int(input())
while 1:
    z += 1
    vis.add(it)
    it = simulate(N, it)
    if z == A:
        print(it)
        exit()
