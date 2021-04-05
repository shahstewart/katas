const assert = require('assert')
let fibonacci
const tests = [
  {
    name: 'throws error when n is not a positive integer',
    test: () => {
      assert.throws(() => fibonacci(), Error, 'Invalid input!')
      assert.throws(() => fibonacci('a'), Error, 'Invalid input!')
      assert.throws(() => fibonacci(4.6), Error, 'Invalid input!')
      assert.throws(() => fibonacci(-3), Error, 'Invalid input!')
    }},
    {
    name: 'should return 0 when n is 0',
    test: () => {
      assert.strictEqual(fibonacci(0), 0)
    }},
    {
      name: 'should return 1 when n is 1',
      test: () => {
      assert.strictEqual(fibonacci(1), 1)
    }},
    {
      name:'should return 1 when n is 2',
      test: () => {
        assert.strictEqual(fibonacci(2), 1)
    }},
    {
      name: 'should return 13 when n is 7',
      test: () => {
        assert.strictEqual(fibonacci(7), 13)
    }},
    {
      name: 'should return 144 when n is 12',
      test: () => {
      assert.strictEqual(fibonacci(12), 144)
    }},
    {
    name: 'should return 354224848179262000000  when n is 100',
    test: () => {
      assert.strictEqual(fibonacci(100), 354224848179262000000 )
    }},
    {
    name: 'should return valid number when n is 1000',
    test: () => {
      assert.strictEqual(true, Number.isInteger(fibonacci(1000)))
    }}
]

// simple recursive
fibonacci = require('./simpleRecursive')
describe('simple recursive Fibonacci', () => {
  tests.forEach(test => {
    if (! test.name.match('100')) { // do not run the tests for F100 and F1000 with simple recursive. May time out/ run out of memory.
      it(test.name, test.test)
    }
  })
})

// recursive with global var
fibonacci = require('./recursiveWithGlobalVar')
describe('simple recursive Fibonacci', () => {
  tests.forEach(test => {
    it(test.name, test.test)
  })
})

// forward recursive
fibonacci = require('./forwardRecursive')
describe('simple recursive Fibonacci', () => {
  tests.forEach(test => {
    it(test.name, test.test)
  })
})

// forward recursive using Array.reduce()
fibonacci = require('./forwardRecursiveWithReduce')
describe('simple recursive Fibonacci', () => {
  tests.forEach(test => {
    it(test.name, test.test)
  })
})
