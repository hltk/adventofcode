import re

def main():
    from aocd import data

    # removes all escaped characters
    data = re.sub(r'!.', '', data)

    # for part 2
    olen, cnt = len(data), data.count('>')

    data = re.sub(r'<[^>]*>', '', data)

    s = h = 0
    for c in data:
        if c == '{':
            h += 1
            s += h
        elif c == '}':
            h -= 1

    # part 1
    print(s)

    # part 2
    # amount of removed characters excluding the brackets
    print(olen - len(data) - cnt * 2)

main()
