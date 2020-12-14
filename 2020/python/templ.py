from functools import *
from itertools import *
from more_itertools import *
from parse import *
from math import *
from builtins import pow
import operator
import re

def ints(line, non_neg=False):
    reg = r"\d+" if non_neg else r"-?\d+"
    return [int(x) for x in re.findall(reg, line)]

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
