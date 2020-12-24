def main(inp):
    inp = [int(x) - 1 for x in inp]
    inp.extend([*range(max(inp) + 1, 10 ** 6)])
    nxt = [None for x in inp]
    mx = max(inp) + 1
    for a, b in zip(inp, inp[1:] + inp[:1]):
        nxt[a] = b
    cur = inp[0]
    for _ in range(10 ** 7):
        vals = []
        orig = cur
        cur = nxt[cur]
        for _ in range(3):
            vals.append(cur)
            cur = nxt[cur]
        nxt[orig] = cur
        dest = orig
        while dest in {*vals, orig}:
            dest = (dest - 1 + mx) % mx
        vals = [dest, *vals, nxt[dest]]
        for a, b in zip(vals, vals[1:]):
            nxt[a] = b
    print((nxt[0] + 1) * (nxt[nxt[0]] + 1))

from aocd import get_data
main(get_data(day=23))
