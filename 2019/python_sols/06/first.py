from collections import defaultdict
links = {}
for line in open('input').readlines():
	links[line[4 : 7]] = line[0 : 3]
import functools
@functools.lru_cache(maxsize=None)
def hae(s):
	if s not in links.keys():
		return [s]
	return hae(links[s]) + [s] if s != "COM" else ["COM"]
sz = defaultdict(int)
nodes = set(links.values()) | set(links.keys())
for a in nodes:
	for u in hae(a):
		sz[u] += 1
print(sum(sz.values()) - len(nodes))
