const getBalancedIndex = require('./getBalancedIndex')
const assert = require('assert')

describe('getBalancedIndex', () => {
    it('returns the balanced index', () => {
        assert.strictEqual(getBalancedIndex([4, 6, 7, 10, 7]), 2)
        assert.strictEqual(getBalancedIndex([12, 8, 18, 2, 9, 7, 10, 4, 3, 7]), 3)
    })

    it('returns minus 1 when no index meets the condition', () => {
        assert.strictEqual(getBalancedIndex([[4, 6, 7, 10, 7, 13]]), -1)
    })

    it('left and right sums are equal when balanced index is returned', () => {
        const arr = [12, 8, 18, 2, 9, 7, 10, 4, 3, 7]
        const bInd = getBalancedIndex(arr)
        const left = arr.slice(0, bInd+1).reduce((partSum, n) => partSum + n, 0)
        const right = arr.slice(bInd+1).reduce((partSum, n) => partSum + n, 0)

        assert.strictEqual(left, right)
    })
})
