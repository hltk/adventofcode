from aocd import data
from parse import parse

p = 0 + 0j
w = 10 + 1j

for v in data.split():
    a, x = parse("{:l}{:d}", v)

    if a == "N": w += x * 1j
    if a == "S": w -= x * 1j
    if a == "E": w += x
    if a == "W": w -= x
    if a == "F": p += w * x
    if a == "R": w *= pow(-1j, x // 90)
    if a == "L": w *= pow(1j, x // 90)

print(int(abs(p.imag) + abs(p.real)))
