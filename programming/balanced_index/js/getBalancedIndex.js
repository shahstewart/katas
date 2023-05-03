const getBalancedIndex = (numArray) => {
    const bIndex = numArray.findIndex((v,i) => {
        const left = numArray.slice(0, i+1).reduce((partSum, n) => partSum + n, 0)
        const right = numArray.slice(i+1).reduce((partSum, n) => partSum + n, 0)
        return left === right
    })

    return bIndex || -1
}

module.exports = getBalancedIndex
