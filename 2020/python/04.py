import re
from aocd import data

ALL = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

p1, p2 = 0, 0

for p in data.split("\n\n"):
    F = dict(map(lambda x: x.split(":"), p.split()))
    if ALL.issubset(set(F.keys())):
        locals().update(F)
        ok = True
        ok &= 1920 <= int(byr) <= 2002
        ok &= 2010 <= int(iyr) <= 2020
        ok &= 2020 <= int(eyr) <= 2030
        ok &= (hgt.endswith("cm") and 150 <= int(hgt[:-2]) <= 193) or \
              (hgt.endswith("in") and 59 <= int(hgt[:-2]) <= 76)
        ok &= bool(re.fullmatch(r"#[0-9a-f]{6}", hcl))
        ok &= bool(re.fullmatch(r"[0-9]{9}", pid))
        ok &= ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        p1 += 1
        p2 += ok

print(p1)

print(p2)
