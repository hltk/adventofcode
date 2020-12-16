from collections import *
from functools import *
from itertools import *
from math import *
from builtins import pow # has to come after math
import operator
import re

from more_itertools import *
from parse import *
import networkx as x

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
