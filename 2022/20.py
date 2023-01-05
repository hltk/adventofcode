from aocd import lines
from collections import deque
numbers = list(enumerate(map(lambda x: int(x) * 811589153, lines)))
N = len(numbers)
for p in numbers * 10:
    x = p[1]
    i = numbers.index(p)
    numbers = numbers[i:] + numbers[:i]
    tail = numbers[1:]
    deq = deque(numbers[1:])
    deq.rotate(-x % (N - 1))
    numbers = [p, *deq]

elem = next(p for p in numbers if p[1] == 0)
zp = numbers.index(elem)
a = numbers[(zp + 1000) % N][1]
b = numbers[(zp + 2000) % N][1]
c = numbers[(zp + 3000) % N][1]
print(a + b + c)
