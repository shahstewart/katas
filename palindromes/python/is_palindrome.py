def is_palindrome(string):
    if not string or type(string) != str:
        return 'Invalid input!'

    str_len = len(string)
    mid = str_len // 2
    reverse_first_half = string[: mid][::-1]
    second_half = string[(mid if str_len % 2 == 0 else mid + 1):]

    return reverse_first_half == second_half
