class Employee:
    def __init__(self, fullname, **kwargs):
        self.name, self.lastname = fullname.split(" ")
        for k, v in kwargs.items():
            self.__setattr__(k, v)


john = Employee('John Doe')
print(john.lastname)
mary = Employee('Mary Major', salary=120000)
print(mary.salary)
richard = Employee('Richard Roe', salary=110000, height=178)
print(richard.salary)
print(richard.height)

giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
print(giancarlo.name)
print(giancarlo.nationality)
