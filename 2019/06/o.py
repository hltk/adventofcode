import sys
import typing
import re
from collections import defaultdict
sys.setrecursionlimit(100000)
def lmap(func, *iterables):
	return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]:
	return lmap(int, re.findall(r"-?\d+", s))
