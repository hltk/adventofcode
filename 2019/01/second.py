f = lambda x : max(0, (x // 3) - 2)
u = list(map(lambda x : int(x.strip()), open('input').readlines()))
su = 0
for x in u:
	while x > 0:
		x = f(x)
		su += x
print(su)
