const factorial = require('./factorial')
const assert = require('assert')

describe('factorial', () => {
  it('throws error when n is not a number', () => {
    assert.throws(() => factorial('a'), Error, 'Invalid input!')
  })
  it('throws error when n is not an integer', () => {
    assert.throws(() => factorial(4.6), Error, 'Invalid input!')
  })
  it('throws error when n is negative', () => {
    assert.throws(() => factorial(-3), Error, 'Invalid input!')
  })
  it('should return 1 when n is 0', () => {
    assert.strictEqual(factorial(0), 1)
  })
  it('should return 1 when n is 1', () => {
    assert.strictEqual(factorial(1), 1)
  })
  it('should return 2 when n is 2', () => {
    assert.strictEqual(factorial(2), 2)
  })
  it('should return 24 when n is 4', () => {
    assert.strictEqual(factorial(4), 24)
  })
  it('should return 3628800 when n is 10', () => {
    assert.strictEqual(factorial(10), 3628800)
  })
  it('should return 9.33262154439441e+157 when n is 100', () => {
    assert.strictEqual(factorial(100), 9.33262154439441e+157)
  })
})
