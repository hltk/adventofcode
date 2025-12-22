from aocd import data


data = data.split("\n")
g = {(i, j) for i, r in enumerate(data) for j, d in enumerate(r) if d == '@'}


def access(p):
    i, j = p
    return sum((i + di, j + dj) in g for di in [-1, 0, 1] for dj in [-1, 0, 1]) < 5


a = []

while not a or a[-1]:
    a.append(len(x := {p for p in g if access(p)}))
    g -= x

print(a[0])
print(sum(a))
