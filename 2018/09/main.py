N = int(input("Pelaajien määrä: "))
M = int(input("suurin mahdollinen kuula: "))
circ = [0]
prev = 0
cur = 1
x=0
scores = [0] * N
def cut(x):
	global circ
	if x == 0: circ = circ[1:]
	elif x + 1 == len(circ): circ = circ[: -1]
	else: circ = circ[:x]+circ[x+1:]
while cur <= M:
	it = 0
	while circ[it] != prev: it = (it + 1) % len(circ)
	if cur % 23 == 0:
		scores[x] += cur
		it = (it - 7 + len(circ)) % len(circ)
		scores[x] += circ[it]
		prev = circ[(it+1+len(circ))%len(circ)]
		cut(it)
		
	else:
		it=(it+1)%len(circ)
		if it + 1 == len(circ): circ = circ + [cur]
		else: circ = circ[:it+1]+[cur]+circ[it+1:]
		prev = cur
	cur += 1
	# print(cur)
	# print(circ)
	x = (x + 1) % N
print(max(scores))
