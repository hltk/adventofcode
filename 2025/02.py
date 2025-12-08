from aocd import data

pairs = [tuple(map(int, p.split("-"))) for p in data.split(",")]


def is_invalid(x, part):
    n = len(x := str(x))
    for i in range(1, n) if part == 2 else [n // 2] if n % 2 == 0 else []:
        if n % i == 0 and len({x[k:k+i] for k in range(0, n, i)}) == 1:
            return True

for part in [1, 2]:
    print(sum(sum(filter(lambda x: is_invalid(x, part), range(l, r + 1))) for l, r in pairs))
