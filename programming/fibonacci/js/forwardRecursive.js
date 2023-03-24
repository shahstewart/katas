const fib = (n, curr = 2, v1 = 0, v2 = 1) => {
  if (n < 0 || !Number.isInteger(n)) {
    throw new Error('Invalid Input!')
  }
  return n < 2 ? n : (n <= curr ? (v1 + v2) : fib(n, curr + 1, v2, (v1 + v2)))
}
module.exports = fib
