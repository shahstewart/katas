<?php
declare(strict_types=1);
function is_palindrome($str)
{
    if (!$str | !is_string($str)) return 'Invalid input!'; 

    $len = strlen($str);
    $mid = (int) ($len / 2);
    $reverse_first_half = strrev(substr($str, 0, $mid));  # string indices are 0 based in php
    $second_half = substr($str, $len % 2 == 0 ? $mid : $mid + 1);

    return $reverse_first_half == $second_half;
}
