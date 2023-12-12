from aocd import data

lines = data.split("\n")

def count(x, t):
    a, b = x.split()
    a = "?".join([a] * t)
    b = ",".join([b] * t)

    dp = [1] + [0] * (len(a))
    for k, x in enumerate(map(int, b.split(","))):
        ndp = [0] * (len(a) + 1)
        for i in reversed(range(len(a) - x + 1)):
            if not a[i:i+x].count("."):
                for j in reversed(range(i + (k == 0))):
                    if a[j:i].count("#"):
                        break
                    ndp[i + x] += dp[j]
        dp = ndp
    return sum(x for i, x in enumerate(dp) if not a[i:].count("#"))

for t in [1, 5]:
    print(sum(map(lambda l: count(l, t), lines)))
