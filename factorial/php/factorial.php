<?php
declare(strict_types=1);
function factorial($n = null)
{
    if (null === $n || !is_int($n) || $n < 0) {
        return 'Invalid input!';
    }
    return ($n < 2 ? 1 : $n * factorial($n - 1));
}

echo(factorial() . "\n");
echo(factorial('2') . "\n");
echo(factorial(3.4) . "\n");
echo(factorial(4) . "\n");
