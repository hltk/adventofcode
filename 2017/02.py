from itertools import combinations

def main():
    from aocd import data

    rows = list(map(lambda x: list(map(int, x.split())), data.split("\n")))

    # part 1
    print(sum(max(r) - min(r) for r in rows))

    def ans(row):
        for x, y in combinations(sorted(row), 2):
            if y % x == 0:
                return y // x

    # part 2
    print(sum(ans(r) for r in rows))

main()
