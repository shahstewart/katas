# This is the most simple solution, but the worst in terms of performance and complexity.
# On a common PC, you will slow terribly/ run out our memory as you go close to 3 digits since this
# solution has an exponential complexity.
#
def fib(n=None):
    if n is None or not str(n).isnumeric() or n < 0:
        return 'Invalid Input!'

    return n if n < 2 else fib(n-2) + fib(n - 1)
