def factorial(n=None):
    if n is None or not str(n).isnumeric() or n < 0:
        return 'Invalid input!'

    return 1 if n < 2 else n * factorial(n - 1)
