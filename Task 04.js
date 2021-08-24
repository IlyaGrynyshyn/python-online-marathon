function factorial(n) {
   if (n === 0 && n === 1 ){
       return 1;
   }
   else{
       return n * (n-1);
   }
}
// console.log(factorial(5))

// function processArray(arr, factorial) {
//     return arr.map(function(el){return factorial(el)});
// }
//
// console.log(processArray([1,2,4,5,6],5))

function pr(arr,factorial) {
    let ab = [];
    for ( let i=0; i<arr.length; i+=1 ) {
        return ab.push(arr[i]);
    }
    return factorial(ab)
}

console.log(pr([1,3,4,5,6,7],factorial))