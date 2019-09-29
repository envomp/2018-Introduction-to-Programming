from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encode(a, b):
    p = rail_pattern(b)
    # this relies on key being called in order, guaranteed?
    return ''.join(sorted(a, key=lambda i: next(p)))


def decode(a, b):
    p = rail_pattern(b)
    indexes = sorted(range(len(a)), key=lambda i: next(p))
    result = [''] * len(a)
    for i, c in zip(indexes, a):
        result[i] = c
    return ''.join(result)


print(decode(encode("Some Random Text", 5), 5))
