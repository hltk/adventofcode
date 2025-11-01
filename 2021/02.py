from aocd import data

lines = data.split("\n")

d = x = z = 0

for a, b in map(lambda x: x.split(), lines):
    if "for" in a:
        x += int(b)
        z += d * int(b)
    if "down" in a:
        d += int(b)
    if "up" in a:
        d -= int(b)

print(x * d)
print(x * z)
