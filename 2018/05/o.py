def ok(a, b):
	return a != b and a.lower() == b.lower()
def calc(c):
	B=[]
	for ch in c:
		if len(B) > 0 and ok(B[-1], ch):
			B.pop()
		else:
			B += [ch]
	return len(B)
a=input()
print(calc(a))
print(min([calc(a.replace(c, "").replace(c.upper(), "")) for c in set([z.lower() for z in a])]))
