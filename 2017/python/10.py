from operator import mul
from itertools import repeat, chain
from operator import xor
from functools import reduce

N = 256

def process(nums, p, l):
    for i in range(l // 2):
        a = (p + i) % N
        b = (p + l - i - 1) % N
        nums[a], nums[b] = nums[b], nums[a]

def knot_hash(lenghts):
    lenghts = list(map(ord, lenghts)) + [17, 31, 73, 47, 23]
    nums = list(range(N))
    p, s = (0, 0)
    for l in chain(*repeat(lenghts, 64)):
        process(nums, p, l)
        p, s = p + l + s, s + 1
    return ''.join(f'{reduce(xor, nums[i:i+16]):02x}' for i in range(0, N, 16))

def main():
    from aocd import data

    lenghts = list(map(int, data.split(",")))

    nums = list(range(N))
    p, s = (0, 0)
    for l in lenghts:
        process(nums, p, l)
        p, s = p + l + s, s + 1

    # part 1
    print(mul(*nums[:2]))

    # part 2
    print(knot_hash(data))

main()
