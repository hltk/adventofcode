r = 0
for x in range(171309, 643603 + 1):
	u = str(x)
	ok = 1
	b = 0
	for j in range(1, len(u)):
		if u[j] < u[j - 1]:
			ok = 0
		if u[j] == u[j - 1]:
			b = 1
	if ok and b:
		r += 1
print(r)
