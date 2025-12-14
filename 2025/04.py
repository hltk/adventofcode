from aocd import data


data = data.split("\n")
g = {(i, j): d for i, r in enumerate(data) for j, d in enumerate(r)}


def access(p):
    i, j = p
    return sum(g.get((i + di, j + dj), ".") == "@" for di in [-1, 0, 1] for dj in [-1, 0, 1]) < 5


a = []

while not a or a[-1]:
    a.append(len(x := [p for p, d in g.items() if d == "@" and access(p)]))
    g |= {u: "." for u in x}

print(a[0])
print(sum(a))
