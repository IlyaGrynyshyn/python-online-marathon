const sumOfLen = (...strint ) => {
    let sum = []
    for (let i = 0; i<strint.length; i++){
        sum = sum + strint[i]
    }
    return sum.length;
}
console.log(sumOfLen('hello', 'hi'));