from aocd import data

def t(s, *_):
    js = s.count(st.index("J")) if st[-1] == "J" else 0
    s = [x for x in s if x != st.index("J")] if st[-1] == "J" else s
    u = [s.count(x) for x in {*s}]
    z = (max(u) if len(u) else 0) + js
    if z > 4: return 0
    if z > 3: return 1
    if len(u) < 3: return 2
    if z > 2: return 3
    if u.count(2) > 1 or (js > (2 not in u)): return 4
    return 5 + (z < 2)

for st in ["AKQJT98765432", "AKQT98765432J"]:
    l = map(str.split, data.split("\n"))
    l = [(list(map(st.index, a)), int(b)) for a, b in l]

    print(sum(
        (len(l) - i) * b for i, (_, b) in enumerate(sorted(l, key=lambda x: (t(*x), *x))))
    )
