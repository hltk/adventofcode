from itertools import count, combinations

from aocd import data

def good_1(x):
    if any(y in x for y in ["ab", "cd", "pq", "xy"]):
        return False
    if not any(x == y for x, y in zip(x, x[1:])):
        return False
    if sum(c in "aeiou" for c in x) < 3:
        return False
    return True


print(sum(map(good_1, data.split("\n"))))

def good_2(x):
    if not any(x == z for x, y, z in zip(x, x[1:], x[2:])):
        return False
    P = list((x + y, i) for x, y, i in zip(x, x[1:], count(0)))
    if not any(x == y and j - i > 1 for (x, i), (y, j) in combinations(P, 2)):
        return False
    return True

print(sum(map(good_2, data.split("\n"))))
