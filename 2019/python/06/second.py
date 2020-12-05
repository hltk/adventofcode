from collections import defaultdict
links = {}
for line in open('input').readlines():
	line = line.strip()
	a, b = line.split(')')
	links[b] = a
import functools
@functools.lru_cache(maxsize=None)
def hae(s):
	if s not in links.keys():
		return [s]
	return hae(links[s]) + [s] if s != "COM" else ["COM"]
def get_dists(s):
	r = {}
	h = reversed(hae(s))
	for i, x in enumerate(h):
		r[x] = i
	return r
A = get_dists('SAN')
B = get_dists('YOU')
nds = set(A.keys()) & set(B.keys())
dists = (A[nd] + B[nd] for nd in nds)
print(min(dists) - 2)
