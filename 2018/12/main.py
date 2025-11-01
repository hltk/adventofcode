u = "."*50000 + input()+"."*50000
N=32
L=[]
for x in range(N):
	a, b = input().split()
	L.append([a,b])
for t in range(2000):
	#print(u)
	Nx = len(u) * ["."]
	for x in range(2, len(u) - 2):
		for a, b in L:
			if u[x-2:x+3] == a:
				Nx[x] = b[0]
				break
	u = "".join(Nx)
	su=0
	for x in range(len(u)):
		if u[x] == "#": su += x-50000
	print(t + 1, u.count("#"), su)
exit()
print(u)
print(su)
