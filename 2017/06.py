def process(state):
    seen = set()
    while tuple(state) not in seen:
        seen.add(tuple(state))
        i = state.index(max(state))
        v = state[i]
        state[i] = 0
        while v:
            i += 1
            state[i % len(state)] += 1
            v -= 1

    return len(seen)

def main():
    from aocd import data

    l = list(map(int, data.split()))

    # part 1
    print(process(l))

    # part 2
    print(process(l))

main()
