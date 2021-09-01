/*
Implement the Student class, the constructor of which accepts 2 parameters fullName - the name and surname of the student,
direction - the direction in which he studies.
Create a showFullName() method that returns the student's first and last name.
Create a nameIncludes(data) method that, using the showFullName() method, checks for the text data argument in the student’s name and returns true if a match is found or false if not found.
Create a static studentBuilder() method that returns a new instance of the class named ‘Ihor Kohut’ and the direction ‘qc’.
Create a getter and setter direction() to read and specify the direction field.
Create an instance of class stud1 named 'Ivan Petrenko' and direction 'web'.
Create an instance of class stud2 named 'Sergiy Koval' and direction 'python'.
Create an instance of the stud3 class named ‘Ihor Kohut’ and the direction ‘qc’ using the static studentBuilder() method.

Usage example:

const stud1 = new Student('Ivan Petrenko', 'web');
stud1.nameIncludes('Ivan');   // true
stud1.nameIncludes('Denysenko'); // false
*/

// const Checker = require('./Checker.js');

class Student {

    constructor(fullName, direction) {
        this._fullName = fullName;
        this._direction = direction;
    };

    showFullName() {
        return this._fullName
    };

    nameIncludes(data) {
        return this.showFullName().includes(data)
    };

    static studentBuilder() {
        return new Student('Ihor Kohut', 'qc')
    };

    get direction() {
        return this._direction
    }

    static studentBuilder() {
        return new Student('Ihor Kohut', 'qc')
    }
}

let stud1 = new Student('Ivan Petrenko', 'web')
let stud2 = new Student('Sergiy Koval', 'python')
let stud3 = Student.studentBuilder()
console.log(stud1)
console.log(stud2)
console.log(stud3)

