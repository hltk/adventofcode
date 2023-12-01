from aocd import data

for part in [1, 2]:
    numbers = "$ one two three four five six seven eight nine".split() if part == 2 else []

    def digit(x):
        if x[0].isdigit(): return x[0]
        nums = (str(v) for v, n in enumerate(numbers) if x[:len(n)] == n)
        return next(nums, None)

    ans = 0

    for l in data.split("\n"):
        c = [x for i in range(len(l)) if (x := digit(l[i:]))]
        ans += int(c[0] + c[-1])

    print(ans)
