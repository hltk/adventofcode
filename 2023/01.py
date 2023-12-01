from aocd import data

for part in [1, 2]:
    numbers = "$ one two three four five six seven eight nine".split() if part == 2 else []

    ans = 0

    for l in data.split("\n"):
        i = 0
        while not (l[i].isdigit() or any(l[i:i+len(x)] == x for x in numbers)): i += 1
        j = len(l) - 1
        while not (l[j].isdigit() or any(l[j:j+len(x)] == x for x in numbers)): j -= 1
        i = l[i] if l[i].isdigit() else [str(v) for v, x in enumerate(numbers) if l[i:i+len(x)] == x][0]
        j = l[j] if l[j].isdigit() else [str(v) for v, x in enumerate(numbers) if l[j:j+len(x)] == x][0]
        ans += int(i + j)

    print(ans)
