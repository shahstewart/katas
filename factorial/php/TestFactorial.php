<?php
declare(strict_types=1);
use PHPUnit\Framework\TestCase;

require('factorial.php');

final class TestFactorial extends TestCase
{
    public function testReturnsExpectedResponsesWhenInputIsInvalid():void
    {
        $this->assertEquals('Invalid input!', factorial());
        $this->assertEquals('Invalid input!', factorial(-1));
        $this->assertEquals('Invalid input!', factorial(4.8));
        $this->assertEquals('Invalid input!', factorial('abd'));
    }

    public function testReturnsExpectedResponsesWhenInputIsValid():void
    {
        $this->assertEquals(1, factorial(1));
        $this->assertEquals(1, factorial(1));
        $this->assertEquals(2, factorial(2));
        $this->assertEquals(6, factorial(3));
        $this->assertEquals(24, factorial(4));
        $this->assertEquals(3628800, factorial(10));
    }
}
