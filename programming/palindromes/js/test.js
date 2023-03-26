const isPalindrome = require('./isPalindrome')
const assert = require('assert')

describe('isPalindrome', () => {
    it('returns a warning when no string or empty string is passed', () => {
        assert.strictEqual(isPalindrome(), 'Invalid input!')
        assert.strictEqual(isPalindrome(''), 'Invalid input!')
    })

    it('returns a warning when input is not a string', () => {
        assert.strictEqual(isPalindrome(3), 'Invalid input!')
        assert.strictEqual(isPalindrome(3.3), 'Invalid input!')
        assert.strictEqual(isPalindrome(false), 'Invalid input!')
        assert.strictEqual(isPalindrome(true), 'Invalid input!')
    })

    it('returns true when passed string is a palindrome', () => {
        assert.strictEqual(isPalindrome('abba'), true)
        assert.strictEqual(isPalindrome('a'), true)
        assert.strictEqual(isPalindrome('aa'), true)
        assert.strictEqual(isPalindrome('aAa'), true)
        assert.strictEqual(isPalindrome('a323a'), true)
        assert.strictEqual(isPalindrome('a3.3a'), true)
        assert.strictEqual(isPalindrome('abba'), true)
    })

    it('returns false when passed string is not a palindrome', () => {
        assert.strictEqual(isPalindrome('abb'), false)
        assert.strictEqual(isPalindrome('a.'), false)
        assert.strictEqual(isPalindrome('36'), false)
        assert.strictEqual(isPalindrome('3.4'), false)
    })
})
