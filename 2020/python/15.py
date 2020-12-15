def ints(line):
    from parse import findall
    return [int(r[0]) for r in findall("{:d}", line)]

def main(inp, t):
    inp = ints(inp)
    age = {}
    lnum = None
    for i in range(t):
        if i < len(inp):
            num = inp[i]
        else:
            num = 0 if lnum not in age else (i - 1) - age[lnum]
        age[lnum] = i - 1
        lnum = num
    print(num)
        

from aocd import data
main(data, 2020)
main(data, 30000000)
