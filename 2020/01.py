from utils import *
from aocd import data

nums = [int(x) for x in data.split("\n")]

def solve(k):
    for s in combinations(nums, k):
        if sum(s) == 2020:
            return reduce(operator.mul, s)

# part 1
print(solve(2))

# part 2
print(solve(3))
