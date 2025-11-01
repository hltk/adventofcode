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
for line in open("input").readlines():
	pass
