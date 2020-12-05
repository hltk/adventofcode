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
class IntCode:
    def __init__(self, prog):
        self.mem = defaultdict(int, enumerate(prog))
        self.numpars = {99: 0, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
        self.pc = 0
        self.off = 0
        self.halted = False
        self.inp = []
        self.out = []
    def step(self):
        if self.mem[self.pc] != 99:
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
                if len(self.inp) == 0:
                    self.mem[self.locs[0]] = -1
                else: self.mem[self.locs[0]] = self.inp.pop(0)
            elif self.op == 4:
                self.out.append(self.vals[0])
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
z = ints(open('input').readlines()[0])
comps = [IntCode(deepcopy(z)) for x in range(50)]
for i in range(50): comps[i].inp.append(i)
i = 0
nat = None
while True:
    comps[i].step()
    if len(comps[i].out) == 3:
        a, b, c = comps[i].out
        if a == 255:
            nat = [b, c]
        else:
            comps[a].inp.append(b)
            comps[a].inp.append(c)
        comps[i].out = []
    i = (i + 1) % 50
    
    
    if nat != None and all(len(x.inp) == 0 for x in comps) and all(len(x.out) == 0 for x in comps):
        comps[0].inp.append(nat[0])
        comps[0].inp.append(nat[1])
        print("nat!", nat[1])
        nat = None
