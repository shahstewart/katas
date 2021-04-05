/**
 * This is the most simple solution, but the worst in terms of complexity.
 * On a common PC, you will slow terribly/ run out our memory as you go close to 3 digits since this
 * solution has an exponential complexity.
 **/

const fib = (n) => {
  if (undefined === n || !Number.isInteger(n) || n < 0 ) {
    throw new Error( 'Invalid Input!')
  }

  return (n < 2 ? n : fib(n - 2) + fib(n - 1))
}

module.exports = fib
