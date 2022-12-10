from aocd import lines
from more_itertools import flatten, chunked
from itertools import accumulate, count

d = lambda line: [0] if "noop" in line else [0, int(line.split()[-1])]

instructions = [1] + list(flatten(map(d, lines)))
preSum = [0] + list(accumulate(instructions))

print(sum(preSum[i] * i for i in range(20, 221, 40)))

draw_row = lambda v: "".join("#" if abs(i - j) <= 1 else "." for i, j in zip(count(0), v))
print("\n".join(draw_row(vals) for vals in chunked(preSum[1:-1], 40)))
