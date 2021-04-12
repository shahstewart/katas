from functools import reduce


def fib(n=None):
    if n is None or not str(n).isnumeric() or n < 0:
        return 'Invalid Input!'

    if n < 2:
        return n

    ret = reduce(lambda acc, val: acc if val < 2 else [acc[1], acc[0] + acc[1]], range(n), [0, 1])
    return ret[0] + ret[1]
