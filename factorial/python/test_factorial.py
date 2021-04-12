from factorial import factorial


def test_factorial():
    assert factorial(-1) == 'Invalid input!'
    assert factorial('a') == 'Invalid input!'
    assert factorial(-3) == 'Invalid input!'
    assert factorial(2.9) == 'Invalid input!'
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(4) == 24
    assert factorial(10) == 3628800
