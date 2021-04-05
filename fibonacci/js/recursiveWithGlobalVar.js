const fibs = []

const fib = (n) => {
  if (n < 0 || !Number.isInteger(n)) {
    throw new Error('Invalid Input!')
  } else if (n < 2) {
    return n
  } else {
    let fib1, fib2
    if (fibs[n - 1] === undefined) {
      fib1 = fib(n - 1)
      fibs[n - 1] = fib1
    } else {
      fib1 = fibs[n - 1]
    }
    if (fibs[n - 2] === undefined) {
      fib2 = fib(n - 2)
      fibs[n - 2] = fib2
    } else {
      fib2 = fibs[n - 2]
    }

    fibs[n] = fib1 + fib2
    return fib1 + fib2
  }
}

module.exports = fib
