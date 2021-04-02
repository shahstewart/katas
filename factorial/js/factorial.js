const factorial = (n) => {
  if (undefined === n || isNaN(n) || n < 0 || !Number.isInteger(n)) {
    throw new Error('Invalid input!')
  }

  if (n < 2) {
    return 1
  }
  return (n * factorial(n-1))
}

module.exports = factorial
