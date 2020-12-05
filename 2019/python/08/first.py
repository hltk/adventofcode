# math.gcd
# grid=defaultdict(lambda : defaultdict(int))
# @functools.lru_cache(maxsize=None)
import sys,typing,re,random,math,functools
from collections import defaultdict
from copy import deepcopy
sys.setrecursionlimit(100000)
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
def printgridfromddict(dc):
	z=dc.keys()
	xmi,ymi,xma,yma=min([x[1]for x in z]),min([x[0]for x in z]),max([x[1]for x in z]),max([x[0]for x in z])
	xsz,ysz=xma-xmi+1,yma-ymi+1
	o=[[" "for x in range(xsz)] for y in range(ysz)]
	for u in z:o[u[0]-ymi][u[1]-xmi]="#"if dc[(u[0],u[1])]else " "
	print("\n".join(["".join(u)for u in o]))
N = 6
M = 25
img = open("input").readlines()[0].strip()
res = [10 ** 9, 0]
for y in range(0, len(img), N * M):
	u = img[y : y + N * M]
	a = u.count("0")
	b = u.count("1")
	c = u.count("2")
	res = min(res, [a, b * c])
print(res)
