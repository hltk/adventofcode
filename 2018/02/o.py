N = 250
a = [input() for x in range(N)]
calc = {}
for i in range(len(a)):
	for j in range(i + 1, len(a)):
		dif = 0
		for h in range(len(a[i])):
			if a[i][h] != a[j][h]:
				dif += 1
		if dif == 1:
			for h in range(len(a[i])):
				if a[i][h] == a[j][h]: print(a[i][h], end="")
			print()
