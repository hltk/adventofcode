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
	z = dc.keys()
	xmi = min([x[1]for x in z])
	ymi = min([x[0]for x in z])
	xma = max([x[1]for x in z])
	yma = max([x[0]for x in z])
	xsz = xma - xmi + 1
	ysz = yma - ymi + 1
	o=[[" "for x in range(xsz)] for y in range(ysz)]
	for u in z:
		o[u[0] - ymi][u[1] - xmi] = "#" if dc[(u[0],u[1])] else " "
	print("\n".join("".join(u)for u in o))
v = defaultdict(list)
amt = defaultdict(int)
for line in open("input").readlines():
	line = line.strip()
	a, b = line.split('=>')
	a = a.split(',')
	b = b.strip()
	b = b.split(' ')
	amt[b[1]] = int(b[0])
	for x in a:
		x = x.strip()
		x = x.split()
		x[0]=int(x[0])
		v[b[1]].append([x[1], int(x[0])])
used = defaultdict(int)
TULOS = 0
def hae(s):
	print(s)
	global TULOS
	tulos = 0
	for a, b in v[s]:
		if a == 'ORE':
			TULOS += b
			continue
		# tee (mahdollinen) uusi lapsi
		# lapsia tarvitaan b kpl
		k = 0
		while k < b:
			k += 1
			if used[a] == 0:
				print(s, " tarvitsee lisää ", a)
				hae(a)
			used[a] -= 1
	used[s] += amt[s]
	return tulos
hae('FUEL')
print(TULOS)
