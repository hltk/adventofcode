from collections import defaultdict

from aocd import data

w = {}

def D(x): return 'xxx' + x

def exec(a, b, c):
    print(a)

for l in data.split("\n"):
    tokens = l.split()
    if "AND" in tokens: exec(f"{D(tokens[4])} = {D(tokens[0])} & {D(tokens[2])}", {}, w)
    elif "OR" in tokens: exec(f"{D(tokens[4])} = {D(tokens[0])} | {D(tokens[2])}", {}, w)
    elif "LSHIFT" in tokens: exec(f"{D(tokens[4])} = {D(tokens[0])} << {tokens[2]}", {}, w)
    elif "RSHIFT" in tokens: exec(f"{D(tokens[4])} = {D(tokens[0])} >> {tokens[2]}", {}, w)
    elif "NOT" in tokens: exec(f"{D(tokens[3])} = ~{D(tokens[1])} & 65535", {}, w)
    else: exec(f"{D(tokens[2])} = {D(tokens[0])}", {}, w)

print(w)

print(w[D('a')])
