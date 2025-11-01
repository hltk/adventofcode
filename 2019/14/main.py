from collections import defaultdict
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
def ok(x):
	used = defaultdict(int)
	TULOS = 0
	def hae(s, kerroin=1):
		nonlocal TULOS
		for a, b in v[s]:
			if a == 'ORE':
				TULOS += b * kerroin
				continue
			k = b * kerroin
			z = min(k, used[a])
			k -= z
			used[a] -= z
			if k:
				hae(a, k // amt[a] + bool(k % amt[a]))
				used[a] -= k
		used[s] += amt[s] * kerroin
	hae('FUEL', x)
	return TULOS <= 1000000000000
B = 0
Z = 1 << 21
while Z:
	if (ok(B + Z)): B += Z
	Z //= 2
print(B)
