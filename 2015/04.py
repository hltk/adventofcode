import hashlib
from itertools import count

from aocd import data

def md5(x):
    return hashlib.md5(x.encode('utf-8')).hexdigest()

print(next(x for x in count(1) if md5(data + str(x)).startswith("0" * 5)))

print(next(x for x in count(1) if md5(data + str(x)).startswith("0" * 6)))
