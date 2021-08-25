function checkAdult(age) {
    try {
        if (typeof age == "undefined") {
            throw Error('Please, enter your age')
        } else if (age < 0) {
            throw Error("Please, enter positive number")
        } else if (typeof age != 'number') {
            throw Error('Please, enter number')
        } else if (!Number.isInteger(age)) {
            throw Error('Please, enter Integer number')
        } else if (age < 18){
            throw Error('Access denied - you are too young!')
        } else {
            console.log('Access allowed')
        }
    }

    catch (error){
        console.log(error.name +" "+ error.message)
    }
    finally {
        console.log("Age verification complete")
    }
}

console.log(checkAdult(25))
console.log(checkAdult(12))