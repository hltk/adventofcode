from functools import *
from itertools import *
from more_itertools import *
from parse import *
from math import *
from builtins import pow
import operator
import re

def ints(line):
    return [int(r[0]) for r in findall("{:d}", line)]

# Taken from ecnerwala
def cprint(ans):
    print(ans)
    import pyperclip
    pyperclip.copy(ans)

def main(inp):
    inp = inp.strip()
    inp = inp.split('\n')

sample = r"""
"""
print('sample:')
main(sample)

from aocd import data
print('actual:')
main(data)
