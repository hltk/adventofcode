# ---> math.gcd
# grid=defaultdict(lambda : defaultdict(int))
# Queue(), PriorityQueue()
# Queue:
#    put, get
#     while not Queue().empty():
# itertools:
#    cycle
#    chain
#    product, permutations, combinations, combinations_with_replacement
#    accumulate
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
# @functools.lru_cache(maxsize=None)
# functools.reduce(f, [1, 2, 3]) = f(f(1, 2), 3)
# See itertools.accumulate() for an iterator that yields all intermediate values.
import sys, typing, re, random, math, functools, cmath
from string import ascii_lowercase, ascii_uppercase
from queue import Queue, PriorityQueue
from collections import defaultdict, deque, Counter
from copy import deepcopy
from time import sleep
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
            s += " #x3456789"[z[(i,j)]]
        print(s)
class IntCode:
    def __init__(self, prog):
        self.mem= defaultdict(int, enumerate(prog))
        self.numpars = {99: 0, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
        self.pc = 0
        self.off = 0
        self.halted = False
        self.inp = []
    def run(self, addinp):
        self.inp.extend(addinp)
        self.out = []
        #  break when there's no input
        A = ""
        while self.mem[self.pc] != 99 and (len(self.inp) or self.mem[self.pc] % 100 != 3):
            self.vals, self.locs = [], []
            self.op = self.mem[self.pc]
            self.pc += 1
            self.md = self.op // 100
            for i in range(self.numpars[self.op % 100]):
                self.mode = self.md % 10
                self.md //= 10
                if self.mode == 0:
                    self.vals += [self.mem[self.mem[self.pc]]]
                    self.locs += [self.mem[self.pc]]
                elif self.mode == 1:
                    self.vals += [self.mem[self.pc]]
                    self.locs += [None]
                elif self.mode == 2:
                    self.vals += [self.mem[self.mem[self.pc] + self.off]]
                    self.locs += [self.mem[self.pc] + self.off]
                else: assert False
                self.pc += 1
            self.op %= 100
            if self.op == 1:
                self.mem[self.locs[2]] = self.vals[0] + self.vals[1]
            elif self.op == 2:
                self.mem[self.locs[2]] = self.vals[0] * self.vals[1]
            elif self.op == 3:
                self.mem[self.locs[0]] = self.inp.pop(0)
            elif self.op == 4:
                try:
                    print(chr(self.vals[0]), end='')
                    A += chr(self.vals[0])
                except:
                    print('unprintable:',self.vals[0])
            elif self.op == 5:
                if self.vals[0]: self.pc = self.vals[1]
            elif self.op == 6:
                if not self.vals[0]: self.pc = self.vals[1]
            elif self.op == 7:
                self.mem[self.locs[2]] = int(self.vals[0] < self.vals[1])
            elif self.op == 8:
                self.mem[self.locs[2]] = int(self.vals[0] == self.vals[1])
            elif self.op == 9:
                self.off += self.vals[0]
            else: assert False
        if self.mem[self.pc] == 99:
            self.halted = True
        return A


z = ints(open('input').readlines()[0])
comp = IntCode(z)
def lol(s):
    global comp
    s += "\n"
    s = [ord(x) for x in s]
    return comp.run(s)
lol("")
pos = (0, 0)
grid = defaultdict(int)
while True:
    dir = input()
    out = lol(dir)
    if 'Doors here lead' in out and dir in ['north','south','east','west'] and 'loud, robotic voice says' not in out:
        pos = list(pos)
        if dir == 'north': pos[0] -= 1
        if dir == 'south': pos[0] += 1
        if dir == 'west': pos[1] -= 1
        if dir == 'east': pos[1] += 1
        pos = tuple(pos)
    grid[pos] = 1
    print('you\'re at', pos)
    grid[pos] = 2
    print_grid(grid)
    grid[pos] = 1
