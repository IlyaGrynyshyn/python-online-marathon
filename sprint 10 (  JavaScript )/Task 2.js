function combineArray(arr1, arr2) {
    let isnumber = function (value){
        return typeof  value == "number";
    }
    arr3 = arr1.concat(arr2)
    return arr3.filter(isnumber)
}
console.log(combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]))