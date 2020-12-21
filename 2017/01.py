def main():
    from aocd import data

    d = list(map(int, data))

    # part 1
    print(sum(x for x, y in zip(d, d[1:] + d[0:1]) if x == y))

    # part 2
    k = len(d) // 2
    print(sum(x for x, y in zip(d, d[k:] + d[0:k]) if x == y))

main()
