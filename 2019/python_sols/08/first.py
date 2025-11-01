N = 6
M = 25
img = open("input").readlines()[0].strip()
res = [10 ** 9, 0]
for y in range(0, len(img), N * M):
	u = img[y : y + N * M]
	a = u.count("0")
	b = u.count("1")
	c = u.count("2")
	res = min(res, [a, b * c])
print(res[1])
