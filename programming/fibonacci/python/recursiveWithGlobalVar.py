fibs = {0: 0, 1: 1}


def fib(n=None):
    if n is None or not str(n).isnumeric() or n < 0:
        return 'Invalid Input!'

    if n in fibs:
        return fibs[n]
    else:
        if n-2 in fibs:
            fibs2 = fibs[n-2]
        else:
            fibs2 = fib(n-2)
            fibs[n-2] = fibs2

        if n-1 in fibs:
            fibs1 = fibs[n-1]
        else:
            fibs1 = fib(n-1)
            fibs[n-1] = fibs1

        fibs[n] = fibs1 + fibs2
        return fibs1 + fibs2
