def calc(s):
    while "(" in s:
        i = s.index("(")
        bal = 1
        j = i + 1
        while s[j] != ")" or bal != 1:
            bal += {"(": 1, ")": -1}.get(s[j], 0)
            j += 1
        s = s[:i] + str(calc(s[i+1:j])) + s[j+1:]
    s = s.split()
    while "+" in s:
        i = s.index("+")
        s[i-1:i+2] = [f"{int(s[i - 1]) + int(s[i + 1])}"]
    return eval(' '.join(s))

def main(inp):
    print(sum(map(calc, inp.split("\n"))))
    
from aocd import data
main(data)
