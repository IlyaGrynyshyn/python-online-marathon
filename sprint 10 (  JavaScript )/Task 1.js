function modifyArray(array) {
    array[0] = 'Start'
    array[array.length-1] = 'End'
    return array
}

console.log(modifyArray([1,2,5,3,4]))