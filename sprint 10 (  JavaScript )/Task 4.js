function factorial(n) {
   if (n === 0){
       return 1;
   }
   else{
       return n * factorial(n-1);
   }
}


function processArray(arr, factorial) {
    const fac_arr = []
    for (let i =0; i<arr.length; i++){
        fac_arr.push(factorial(arr[i]));
    }
    return fac_arr
}

console.log(processArray([1,2,4,5,6],factorial))

