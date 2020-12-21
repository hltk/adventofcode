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

#    ===== =========================================== ========
#    Type  Characters Matched                          Output
#    ===== =========================================== ========
#    l     Letters (ASCII)                             str
#    w     Letters, numbers and underscore             str
#    W     Not letters, numbers and underscore         str
#    s     Whitespace                                  str
#    S     Non-whitespace                              str
#    d     Digits (effectively integer numbers)        int
#    D     Non-digit                                   str
#    n     Numbers with thousands separators (, or .)  int
#    %     Percentage (converted to value/100.0)       float
#    f     Fixed-point numbers                         float
#    F     Decimal numbers                             Decimal
#    e     Floating-point numbers with exponent        float
#          e.g. 1.1e-10, NAN (all case insensitive)
#    g     General number format (either d, f or e)    float
#    b     Binary numbers                              int
#    o     Octal numbers                               int
#    x     Hexadecimal numbers (lower and upper case)  int
#    ti    ISO 8601 format date/time                   datetime
#          e.g. 1972-01-20T10:21:36Z ("T" and "Z"
#          optional)
#    te    RFC2822 e-mail format date/time             datetime
#          e.g. Mon, 20 Jan 1972 10:21:36 +1000
#    tg    Global (day/month) format date/time         datetime
#          e.g. 20/1/1972 10:21:36 AM +1:00
#    ta    US (month/day) format date/time             datetime
#          e.g. 1/20/1972 10:21:36 PM +10:30
#    tc    ctime() format date/time                    datetime
#          e.g. Sun Sep 16 01:03:52 1973
#    th    HTTP log format date/time                   datetime
#          e.g. 21/Nov/2011:00:07:11 +0000
#    ts    Linux system log format date/time           datetime
#          e.g. Nov  9 03:37:44
#    tt    Time                                        time
#          e.g. 10:21:36 PM -5:30
#    ===== =========================================== ========
