# math.gcd
# grid=defaultdict(lambda : defaultdict(int))
# @functools.lru_cache(maxsize=None)
# Queue()
# PriorityQueue()
# Queue().put()
# Queue().get()
# while not Queue().empty():
# itertools:
#    cycle
#    chain
#    product, permutations, combinations, combinations_with_replacement
# deque():
#     append, appendleft, pop, popleft
# Counter():
#     most_common(3)
#     elements
import sys,typing,re,random,math,functools
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
q = Queue()
grid = open("input").readlines()
grid = [x.replace('\n', '') for x in grid]
adj = defaultdict(list)
pos = defaultdict(int)
fnd = {}
AA = None
ZZ = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            continue
        for h in range(-1, 2):
            for z in range(-1, 2):
                if int(h != 0) + int(z != 0) != 1:
                    continue
                if h + i < 0: continue
                if z + j < 0: continue
                if h + i >= len(grid): continue
                if z + j >= len(grid[i]): continue
                ai = h + i
                aj = z + j
                if grid[ai][aj] == '.':
                    adj[(i, j)].append((0, (ai, aj)))
                if grid[ai][aj] in ascii_uppercase:
                    other_letter = None
                    cur_letter = deepcopy(grid[ai][aj])
                    if h != 0:
                        other_letter = grid[i + h * 2][j]
                        if h == -1:
                            cur_letter, other_letter = other_letter, cur_letter
                    else:
                        other_letter = grid[i][j + z * 2]
                        if z == -1:
                            cur_letter, other_letter = other_letter, cur_letter
                    cur_letter += other_letter
                    if i == 2 or j == 2 or i + 3 == len(grid) or j + 3 == len(grid[i]):
                        pos[(i, j)] = 1
                        if cur_letter == 'AA':
                            AA = (i, j)
                        if cur_letter == 'ZZ':
                            ZZ = (i, j)
                    else:
                        pos[(i, j)] = 2
                    if cur_letter in fnd:
                        if pos[(i, j)] == 2:
                            adj[(i, j)].append((1, fnd[cur_letter]))
                            adj[fnd[cur_letter]].append((-1, (i, j)))
                        else:
                            adj[(i, j)].append((-1, fnd[cur_letter]))
                            adj[fnd[cur_letter]].append((1, (i, j)))
                    fnd[cur_letter] = (i, j)
q.put((0, AA))
vis = set()
dist = {}
dist[(0, AA)] = 0
while not q.empty():
    u = q.get()
    if u == (0, ZZ):
        print(dist[u])
        exit()
    for a in adj[u[1]]:
        dest = (u[0] + a[0], a[1])
        if dest[0] < 0:
            continue
        if dest in vis:
            continue
        vis.add(dest)
        dist[dest] = dist[u] + 1
        q.put(dest)
