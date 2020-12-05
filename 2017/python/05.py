def main():
    from aocd import data

    l = list(map(int, data.split("\n")))

    def simulate(d):
        inc = [0] * len(l)
        p, s = (0, 0)

        while 0 <= p < len(l):
            np = p + l[p] + inc[p]
            inc[p] += d.get(inc[p] + l[p], 1)
            p = np
            s += 1

        return s

    # part 1
    print(simulate({}))

    # part 2
    print(simulate({3: -1})) 

main()
