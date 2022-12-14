# Interact with the queues using the get, put, empty methods
# from queue import PriorityQueue, Queue,

# sys.setrecursionlimit(100000)
#

from functools import partial
import operator
import math

class V:
    def __init__(self, *x):
        self.v = tuple(x)
    def __sub__(self, v):
        return V(*map(operator.sub, self, v))
    def __add__(self, v):
        return V(*map(operator.add, self, v))
    def __mul__(self, v):
        if isinstance(v, V):
            return V(*map(operator.mul, self, v))
        return V(*map(lambda x: x * v, self))
    def __truediv__(self, v):
        return self.checkints(self.__mul__(1 / v))
    def __floordiv__(self, v):
        return V(*map(lambda x: x // v, self))
    def dot(self, v):
        return sum(self * v)
    @property
    def x(self):
        return self.v[0]
    @property
    def y(self):
        return self.v[1]
    @property
    def z(self):
        return self.v[2]
    @property
    def len(self):
        l = math.sqrt(self.dot(self))
        if round(l) ** 2 == self.dot(self):
            return round(l)
        return l
    @property
    def dist(self):
        return self.len
    @property
    def norm(self):
        return self.checkints(self / self.len)
    def __repr__(self):
        return f"V({', '.join(str(x) for x in self.v)})"
    def __str__(self):
        return self.__repr__()
    def __iter__(self):
        yield from self.v.__iter__()
    def __eq__(self, oth):
        return self.v == oth.v
    def __hash__(self):
        return self.v.__hash__()
    @staticmethod
    def checkints(v):
        return V(*map(int, v)) if all(math.isclose(round(x), x) for x in v) else v
    @staticmethod
    def interpolate(p1, p2, num=None):
        if not num:
            num = (p2 - p1).dist + 1
        for i in range(num):
            yield p1 + V.checkints((p2 - p1) / (num - 1)) * i


def dotproduct(vec1, vec2):
    return sum(map(operator.mul, vec1, vec2))


def zip_func(vec1, vec2, func):
    return tuple(func(a, b) for a, b in zip(vec1, vec2))


vec_add = partial(zip_func, func=operator.add)
vec_sub = partial(zip_func, func=operator.sub)
vec_mul = partial(zip_func, func=operator.mul)

def vec_floordiv(v, s):
    return tuple(x // s for x in v)

def vec_div(v, s):
    return tuple(x / s for x in v)

def vec_scale(v, s):
    return tuple(x * s for x in v)

def vec_norm(v):
    if sum(map(abs, v)) == 0:
        return v
    l = math.sqrt(sum(vec_mul(v, v)))
    if round(l) ** 2 == sum(vec_mul(v, v)):
        return vec_floordiv(v, round(l))
    return vec_div(v, l)



def tensor(*dims, default=None):
    if len(dims) == 1:
        return [default for x in range(dims[0])]
    v = tensor(*dims[1:], default=default)
    return [copy.deepcopy(v) for _ in range(dims[0])]


def starfilter(predicate, iterable):
    for t in iterable:
        if predicate(*t):
            yield t


def neighbours4(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1

def neighbours5(i, j):
    yield i, j
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1

def neighbours8(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1
    yield i - 1, j + 1
    yield i - 1, j - 1
    yield i + 1, j + 1
    yield i + 1, j - 1

def neighbours9(i, j):
    yield i, j
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1
    yield i - 1, j + 1
    yield i - 1, j - 1
    yield i + 1, j + 1
    yield i + 1, j - 1


valid_coords = lambda i, j: i in range(n) and j in range(m)
