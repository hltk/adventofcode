from aocd import data
import re, numpy as np

def read_monkey(s):
    d = re.match(
        r"""Monkey (?P<id>\d+):
  Starting items: (?P<items>.+)
  Operation: (?P<op>.+)
  Test: divisible by (?P<test>\d+)
    If true: throw to monkey (?P<True>\d+)
    If false: throw to monkey (?P<False>\d+)""",
        s,
    ).groupdict()
    d["id"] = int(d["id"])
    d["items"] = [int(item) for item in d["items"].split(", ")]
    d["op"] = lambda x, op=d["op"]: eval(op.split("=")[-1].replace("old", str(x)))
    d["test"] = int(d["test"])
    d["True"] = int(d["True"])
    d["False"] = int(d["False"])
    d["inspected"] = 0
    return d

monkeys = [
    read_monkey(m)
    for m in data.split("\n\n")
]

t = [m["test"] for m in monkeys]

for m in monkeys:
    m["items"] = [[v % d for d in t] for v in m["items"]]

monkeys = {
    m["id"]: m for m in monkeys
}

all_items = []

for m in monkeys.values():
    old_size = len(all_items)
    all_items.extend(m["items"])
    m["items"] = list(range(old_size, len(all_items)))

for _ in range(10 ** 4):
    for i in sorted(monkeys.keys()):
        m = monkeys[i]
        it = m["items"].copy()
        m["items"].clear()
        for item_id in it:
            m["inspected"] += 1
            v = all_items[item_id]
            all_items[item_id] = [m["op"](x) % d for x, d in zip(v, t)]
            divisibility = any(x == 0 and m["test"] == d for x, d in zip(all_items[item_id], t))
            monkeys[m[str(divisibility)]]["items"].append(item_id)

times = [m["inspected"] for m in monkeys.values()]
print(np.prod(sorted(times)[-2:]))
