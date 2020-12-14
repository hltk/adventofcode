# Interact with the queues using the get, put, empty methods
#from queue import PriorityQueue, Queue,

#sys.setrecursionlimit(100000)

def dotproduct(vec1, vec2):
    return sum(map(operator.mul, vec1, vec2))

def zip_func(vec1, vec2, func):
    return tuple(func(a, b) for a, b in zip(vec1, vec2))

zip_add = partial(zip_func, func=operator.add)
zip_sub = partial(zip_func, func=operator.sub)
zip_mul = partial(zip_func, func=operator.mul)

def tensor(*dims, default=None):
    if len(dims) == 1:
        return [default for x in range(dims[0])]
    v = tensor(*dims[1:], default=default)
    return [copy.deepcopy(v) for _ in range(dims[0])]

def starfilter(predicate, iterable):
    for t in iterable:
        if predicate(*t):
            yield t

def neighbours(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1
    #yield i - 1, j + 1
    #yield i - 1, j - 1
    #yield i + 1, j + 1
    #yield i + 1, j - 1

valid_coords = lambda i, j: i in range(n) and j in range(m)
