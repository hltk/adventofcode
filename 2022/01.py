from aocd import data

def f(n):
    s = [sum(map(int, e.split("\n"))) for e in data.split("\n\n")]
    return sum(sorted(s, reverse=True)[:n])

print(f(1))
print(f(3))
