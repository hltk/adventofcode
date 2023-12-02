from aocd import data
import re

lines = data.split("\n")

def f(n, l):
    return max(map(int, re.findall(f"(\\d+) {n}", l)))

def part1(l):
    return f("red", l) <= 12 and f("green", l) <= 13 and f("blue", l) <= 14

def part2(l):
    return f("red", l) * f("green", l) * f("blue", l)

print(sum(i+1 for i, line in enumerate(lines) if part1(line)))
print(sum(map(part2, lines)))
