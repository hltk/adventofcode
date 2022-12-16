from aocd import lines
from utils import *
from itertools import combinations

inp = [ints(line) for line in lines]
inp = [(V(*v[0:2]), V(*v[2:4])) for v in inp]

ranges = []
y = 2000000
max_coord = 4000000

for sensor, beacon in inp:
    ydist = (sensor - V(sensor.x, y)).manhattan
    left = (sensor - beacon).manhattan - ydist
    if left >= 0:
        ranges.append(V(sensor.x - left, sensor.x + left))

ranges.sort(key=lambda x: (x.x, -x.y))
seen = set()
prev = None
ans = 0

for r in ranges:
    if any(a.x <= r.x and r.y <= a.y for a in seen):
        continue
    if prev:
        if r.x <= prev.y:
            ans -= prev.y - r.x + 1
    seen.add(r)
    ans += r.y - r.x + 1
    prev = r

print(ans - len({beacon.y == y for s, b in inp}))

def could_be_beacon(p):
    if not (0 <= p <= max_coord) or any(p == b for s, b in inp):
        return False
    return all((p - s).manhattan > (b - s).manhattan for s, b in inp)

for sensor, beacon in inp:
    d = (sensor - beacon).manhattan + 1
    for dx in [1, -1]:
        for dy in [1, -1]:
            for i in range(d + 1):
                p = sensor + V(dx * i, dy * (d - i))
                if could_be_beacon(p):
                    print(p.x * 4000000 + p.y)
                    exit()
