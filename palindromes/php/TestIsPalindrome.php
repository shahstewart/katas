<?php
declare(strict_types=1);
use PHPUnit\Framework\TestCase;

require('is_palindrome.php');

final class TestIsPalindrome extends TestCase
{
    public function testReturnsWarningWhenInputIsInvalid(): void 
    {
        $this->assertEquals('Invalid input!', is_palindrome(3));
        $this->assertEquals('Invalid input!', is_palindrome(4.4));
        $this->assertEquals('Invalid input!', is_palindrome(''));
    }

    public function testReturnsTrueWhenPalindrome(): void 
    {
        $this->assertTrue(is_palindrome('x'));
        $this->assertTrue(is_palindrome('xx'));
        $this->assertTrue(is_palindrome('xXx'));
        $this->assertTrue(is_palindrome('3.3'));
        $this->assertTrue(is_palindrome('abccba'));
    }

    public function testReturnsFalseWhenNotPalindrome(): void 
    {
        $this->assertFalse(is_palindrome('xa'));
        $this->assertFalse(is_palindrome('abcabc'));
        $this->assertFalse(is_palindrome('334'));
        $this->assertFalse(is_palindrome('xX'));
    }
}


