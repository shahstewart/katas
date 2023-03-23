from is_palindrome import is_palindrome

def test_returns_invalid_input_when_input_is_invalid():
    assert is_palindrome('') == 'Invalid input!'
    assert is_palindrome(3) == 'Invalid input!'
    assert is_palindrome(True) == 'Invalid input!'
    assert is_palindrome(False) == 'Invalid input!'
    assert is_palindrome(3.4) == 'Invalid input!'

def test_returns_true_when_palindrome():
    assert is_palindrome('3.3') is True
    assert is_palindrome('aaabbbaaa') is True
    assert is_palindrome('x') is True
    assert is_palindrome('xx') is True
    assert is_palindrome('xXx') is True
    assert is_palindrome('xxx') is True

def test_returns_false_when_not_palindrome():
    assert is_palindrome('3.4') is False
    assert is_palindrome('xX') is False
    assert is_palindrome('xX') is False
    assert is_palindrome('asdfsadfs f') is False



