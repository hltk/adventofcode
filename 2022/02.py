from aocd import lines


def score(line):
    a, b = line.strip().split()
    a, b = (ord(a) + 1) % 3, (ord(a) + ord(b) + 2) % 3
    return b + 1 + (a == b) * 3 + ((b + 2) % 3 == a) * 6


print(sum(map(score, lines)))
