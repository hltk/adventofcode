S = ord("a") - ord("A")
BACK = input()
asd = "abcdefghijklmopqrstuvwqxz"
r = 10 ** 10
for u in asd:
	a = BACK
	a = a.replace(u, "")
	a = a.replace(u.upper(), "")
	del = 0
	jt = 0
	for it in range(1, len(a)):
		A = X[-1]
		B = Y[0]
		while :
			if A.lower() != B.lower() or A == B:
				break
			X.pop()
			Y.popleft()
	r = min(r, len(a) - del)
print(r)
