from itertools import starmap

def main():
    from aocd import data

    def dist(x, y):
        return (abs(x) + abs(y) + abs(x + y)) // 2

    movs = {
        'n': lambda x, y: (x, y + 1),
        's': lambda x, y: (x, y - 1),
        'nw': lambda x, y: (x - 1, y + 1),
        'sw': lambda x, y: (x - 1, y),
        'ne': lambda x, y: (x + 1, y),
        'se': lambda x, y: (x + 1, y - 1)
    }

    pos = (0, 0)
    vis = {pos}

    for mov in data.split(","):
        pos = movs[mov](*pos)
        vis.add(pos)

    # part 1
    print(dist(*pos))

    # part 2
    print(max(starmap(dist, vis)))

main()
