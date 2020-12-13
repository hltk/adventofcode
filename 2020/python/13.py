from utils import *
from aocd import data

# crt from https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a):
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
    s = 0
    prod = reduce(operator.mul, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % prod
 
def main(inp):
    inp = inp.strip()
    _, b = inp.split("\n")
    a, n = [], []
    for i, x in enumerate(b.split(",")):
        if x == 'x':
            continue
        x = int(x)
        a.append(x - i % x)
        n.append(x)
    print(chinese_remainder(n, a))
    
main(data)
