from aocd import data
import re, math

def ans(t, d):
    return math.prod(sum(i * (a - i) > b for i in range(a)) for a, b in zip(t, d))

def i(x): return [*map(int, re.findall(r"\d+", x))]
def ii(x): return [int(''.join(re.findall(r"\d+", x)))]
print(ans(*map(i, data.split("\n"))))
print(ans(*map(ii, data.split("\n"))))
