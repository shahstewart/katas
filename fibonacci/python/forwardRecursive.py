def fib(n=None, curr=2, v1=0, v2=1):
    if n is None or not str(n).isnumeric() or n < 0:
        return 'Invalid Input!'

    if n < 2:
        return n

    return (v1 + v2) if n <= curr else fib(n, curr+1, v2, v1+v2)
