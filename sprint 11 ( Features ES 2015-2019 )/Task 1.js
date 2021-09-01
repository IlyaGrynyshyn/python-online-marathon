const filterNums = (nums,number=0,parameter="greater") => {
    return nums.filter(value => parameter === 'greater' ? value > number : value < number);
};



console.log(filterNums([-1, 2, 4, 0, 55, -12, 3], 11, 'greater'))
console.log(filterNums([-2, 2, 3, 0, 43, -13, 6], -33, 'less'))
