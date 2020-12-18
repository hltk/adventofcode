def calc(s):
    while "(" in s:
        i = s.index("(")
        bal = 1
        j = i + 1
        while s[j] != ")" or bal != 1:
            if s[j] == ")":
                bal -= 1
            if s[j] == "(":
                bal += 1
            j += 1
        s = list(s)
        s[i:j+1] = str(calc(''.join(s[i+1:j])))
        s = ''.join(s)
    s = s.split()
    while "+" in s:
        i = s.index("+")
        a = s[i - 1]
        b = s[i + 1]
        s[i-1:i+2] = [str(int(a) + int(b))]
    return eval(' '.join(s))

def main(inp):
    print(sum(map(calc, inp.split("\n"))))
    
from aocd import data
main(data)
