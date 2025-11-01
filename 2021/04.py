def ints(s):
    from re import findall
    return list(map(int, findall("-?\d+", s)))

def flatten(l):
    from itertools import chain
    return list(chain.from_iterable(l))

from aocd import data

nums, *boards = data.split("\n\n")

nums = ints(nums)
*boards, = map(lambda x: list(map(ints, x.split("\n"))), boards)

def check(board, seen):
    if any(all(x in seen for x in row) for row in board):
        return True
    if any(all(x in seen for x in col) for col in zip(*board)):
        return True
    return False

seen = set()
won = []

for u in nums:
    seen.add(u)
    for b in boards:
        if b not in won and check(b, seen):
            won.append(b)
            unseen = sum(x for x in flatten(b) if x not in seen)
            print(u * unseen)
