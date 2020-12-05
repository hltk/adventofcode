import collections
import copy
import functools
import itertools
import math
import more_itertools
import networkx as nx
import operator
import re
import sys

from itertools import (
    accumulate,
    chain,
    combinations,
    count,
    cycle,
    filterfalse,
    groupby,
    islice,
    permutations,
    product,
    repeat,
    starmap,
    tee,
    zip_longest,
)

from more_itertools import (
    chunked,
    consume,
    first_true,
    flatten,
    grouper,
    ilen,
    ncycles,
    nth,
    pairwise,
    partition,
    powerset,
    quantify,
    repeatfunc,
    roundrobin,
    substrings,
    substrings_indexes,
    take,
    unique_everseen,
    unique_justseen,
    unzip,
    windowed,
)

from collections import (
    Counter,
    defaultdict,
    deque,
)


# Interact with queue using get, put, empty

from queue import (
    PriorityQueue,
    Queue,
)

from functools import (
    partial,
    reduce,
)

from math import (
    ceil,
    floor,
    sqrt,
)


sys.setrecursionlimit(100000)


def dotproduct(vec1, vec2):
    return sum(map(operator.mul, vec1, vec2))


def vec_add(vec1, vec2):
    return (a + b for a, b in zip(vec1, vec2))


def vec_sub(vec1, vec2):
    return (a - b for a, b in zip(vec1, vec2))


def gen_grid(*dims, default=None):
    if len(dims) == 1:
        return [default for x in range(dims[0])]
    v = gen_grid(*dims[1:], default=default)
    return [copy.deepcopy(v) for _ in range(dims[0])]


def ints(line, non_negative=False):
    if non_negative:
        reg = r"\d+"
    else:
        reg = r"-?\d+"
    return [int(x) for x in re.findall(reg, line)]


def starfilter(predicate, iterable):
    for t in iterable:
        if predicate(*t):
            yield t


def neighbours(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1


def valid_coords(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def adjacent_difference(it, f=operator.sub):
    return starmap(lambda x, y: f(y, x), pairwise(it))
