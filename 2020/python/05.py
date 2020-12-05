from aocd import data

trans = dict(zip(map(ord, "FLBR"), "0011"))

seats = {int(line.translate(trans), 2) for line in data.split("\n")}

print(max(seats))

for x in seats:
    if x + 1 not in seats and x + 2 in seats:
        print(x + 1)
