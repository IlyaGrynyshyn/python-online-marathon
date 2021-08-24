class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(self, string):
        data = string.split('-')
        self.firstname = data[0]
        self.lastname = data[1]
        self.salary = data[2]
        return self


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp2.firstname)
print(emp2.salary)
print(emp2.lastname)
print(emp1.firstname)
print(emp1.salary)