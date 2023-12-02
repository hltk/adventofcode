from aocd import data

for part in [1, 2]:
    numbers = "$ one two three four five six seven eight nine".split() if part == 2 else []

    def digit(x):
        nums = (str(v) for v, n in enumerate(numbers) if x[:len(n)] == n)
        return x[0] if x[0].isdigit() else next(nums, None)

    ans = 0

    for l in data.split("\n"):
        c = [x for i, _ in enumerate(l) if (x := digit(l[i:]))]
        ans += int(c[0] + c[-1])

    print(ans)
