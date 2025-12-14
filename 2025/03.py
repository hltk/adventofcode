from aocd import data


def f(l, k):
    n = len(l)
    d = [0 for _ in range(n + 1)]
    for k in range(k):
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                d[j] = max(d[j], int(str(d[i]) + l[j - 1]))

    return max(d)


for k in [2, 12]:
    print(sum(map(lambda l: f(l, k), data.split("\n"))))

