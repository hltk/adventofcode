from collections import *
from functools import *
from itertools import *
from math import *
from builtins import pow # has to come after math
import operator
import re
from pprint import pprint

from more_itertools import *
from parse import * # search, parse, findall
import networkx as nx
import pyperclip

def ints(line):
    return [int(r[0]) for r in findall("{:d}", line)]

# Taken from ecnerwala
def cprint(ans):
    print(ans)
    pyperclip.copy(ans)

def main(inp):
    inp = inp.strip()
    inp = inp.split('\n')
    pprint(inp)

sample = r"""
"""
print('sample:')
main(sample)

from aocd import data
print('actual:')
main(data)
