lines = open("input").readlines()
L = []
for x in lines:
	y = x.split()
	y = list(map(int, y))
	L.append([y[0], y[1], y[2], y[3]])

best = [10 ** 20,set(),0]
for t in range(15000):
	u = set()
	for x in range(len(L)):
		L[x][0] += L[x][2]
		L[x][1] += L[x][3]
		u.add((L[x][0], L[x][1]))
	best = min(best, [len(u), u, t])

u=best[1]
mi_y = min([x[1] for x in u])
ma_y = max([x[1] for x in u])
mi_x = min([x[0] for x in u])
ma_x = max([x[0] for x in u])
ysz = ma_y - mi_y + 1
xsz = ma_x - mi_x + 1
grid = [["."for x in range(xsz)]for y in range(ysz)]
for x in u: grid[x[1] - mi_y][x[0] - mi_x] = "#"
print("\n".join(["".join(z) for z in grid]))

print(best[2])
