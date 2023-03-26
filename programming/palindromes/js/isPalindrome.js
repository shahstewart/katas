// noinspection JSCheckFunctionSignatures

const isPalindrome = (str) => {
    if (!str || typeof str !== 'string') return 'Invalid input!'

    const reverseStr = (s) => s === '' ? '' : reverseStr(s.substr(1)) + s.charAt(0)
    const len = str.length
    const mid = parseInt(len / 2)  // will coerce float to string
    let firstHalf = str.substring(0, mid)
    const secondHalf = str.substring(len % 2 === 0 ? mid : mid + 1)  // js has 0-based index
    firstHalf = reverseStr(firstHalf)

    return firstHalf === secondHalf
}

module.exports = isPalindrome
