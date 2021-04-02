def factorial(n=None):
    if n is None or not str(n).isnumeric() or n < 0:
        return 'Invalid input!'

    if n < 2:
        return 1

    return n * factorial(n - 1)
