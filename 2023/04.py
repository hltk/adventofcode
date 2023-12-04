from aocd import data

p1, p2 = 0, 0
t = []

for l in data.split('\n'):
    a, b = map(str.split, l.split("|"))
    s = len(set(a) & set(b))

    t = [x - 1 for x in t if x > 0]

    p1 += 2 ** (s - 1) if s > 0 else 0
    p2 += 1 + s * (len(t) + 1)

    t += [s] * (len(t) + 1)

print(p1, p2, sep='\n')
