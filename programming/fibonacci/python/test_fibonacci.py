from simpleRecursive import fib
from recursiveWithGlobalVar import fib as fib_l
from forwardRecursive import fib as fib_f
from forwardRecursiveWithReduce import fib as fib_fr


def run_tests(func):
    assert func() == 'Invalid Input!'
    assert func('a') == 'Invalid Input!'
    assert func(-3) == 'Invalid Input!'
    assert func(5.7) == 'Invalid Input!'
    assert func(0) == 0
    assert func(1) == 1
    assert func(2) == 1
    assert func(7) == 13
    assert func(12) == 144


def run_large_n_tests(func):
    assert func(100) == 354224848179261915075
    assert isinstance(func(1000), int) is True


def test_fibonacci_r():
    run_tests(fib)


def test_fibonacci_l():
    run_tests(fib_l)
    run_large_n_tests(fib_l)


def test_fibonacci_f():
    run_tests(fib_f)
    run_large_n_tests(fib_l)


def test_fibonacci_fr():
    run_tests(fib_fr)
    run_large_n_tests(fib_l)
