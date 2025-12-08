from aocd import data

a, z = 0, 50
l = [z]
for x in data.split("\n"):
    y = 1 if x[0] == "L" else 99
    a += sum(not (z := (z + y) % 100) for _ in " " * int(x[1:]))
    l += [z]

print(l.count(0), a, sep='\n')
