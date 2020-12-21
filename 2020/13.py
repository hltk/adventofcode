from aocd import data

from sympy.ntheory.modular import crt

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
    print(crt(n, a)[0])
    
main(data)
