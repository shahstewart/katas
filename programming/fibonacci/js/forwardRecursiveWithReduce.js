const fib = (n) => {
  if (n < 0 || !Number.isInteger(n)) {
    throw new Error('Invalid Input!')
  } else if (n < 2) {
    return n
  } else {
    const last2Fibs = new Array(n).fill(1).reduce(
      (acc, val, ind) => ind < 2 ? acc : [acc[1], acc[0] + acc[1]],
      [0, 1])

    return last2Fibs[0] + last2Fibs[1]
  }
}

module.exports = fib
