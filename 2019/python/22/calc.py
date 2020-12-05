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
lines = reversed(lines)
L = []

# it = it * 1 + 0

A = 1
B = 0
N = 119315717514047
for l in lines:
    if 'cut' in l:
        B += ints(l)[0]
    elif 'deal into new stack' in l:
        A = -A
        B = -B
        B += N - 1
    elif 'deal with increment' in l:
        A *= pow(ints(l)[0], N - 2, N)
        B *= pow(ints(l)[0], N - 2, N)

print('it*',A%N,'+',B%N)
A %= N
B %= N

it=2020

# ax + b
# a(ax + b) + b
# a( a(ax + b) + b) + b
# a ^ 3 * x + b + a * b + b * a ^ 2

R = 101741582076661

# R = int(input())

#print('first',(A * it + B)%N)
#print('second',(A * (A * it + B) + B)%N)
#print('third',(A * ((A * (A * it + B) + B))+B)%N)

# S = a_0 * (1 - q ^ n) / (1 - q)
# = a_0 * (q ^ n - 1) / (q - 1)
S = B * (pow(A, R , N) - 1) % N * pow(A - 1, N - 2, N) % N

print((it * pow(A, R, N) % N + S) % N)
