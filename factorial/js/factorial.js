const factorial = (n) => {
  if (undefined === n || isNaN(n) || n < 0 || !Number.isInteger(n)) {
    throw new Error('Invalid input!')
  }

  return n < 2 ? 1 : n * factorial(n-1)
}

module.exports = factorial
