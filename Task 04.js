function factorial(n) {
   if (n === 0){
       return 1;
   }
   else{
       return n * factorial(n-1);
   }
}


function processArray(arr, factorial) {
    return arr.map(function(x){
        return factorial(x)
    });
}

console.log(processArray([1,2,4,5,6],factorial))

