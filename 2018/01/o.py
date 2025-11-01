N= 960
a =[]
s = 0
for x in range(N):
	u = input()
	a.append(int(u))
lol = {0 : 1}
cur = 0
while True:
	for x in a:
		cur += x
		if cur in lol.keys():
			print(cur)
			exit()
		lol[cur] = 1
	
