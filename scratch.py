import datetime

# Python Object-Oriented Programming

# Classes and Instances

# data and functions associated with a particular class are called attributes and methods

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

        # the init method sets up the attributes automatically for each instance, the class receives the instance
        # as the first argument automatically

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    #   self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

    @property  # allows the method to be accessed like an attribute
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f'Deleted {self.first} {self.last}')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def __repr__(self):  # is meant to be an unambigous representation of the object, and should be used for
        return f"Employee({self.first}, {self.last}, {self.pay})"  # logging, debugging, etc.

    def __str__(self):  # is meant to be a readble version of an object, used as a display to the end user
        return f"{self.fullname()}, {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

# class methods can be used as alternate constructors

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f'----> {emp.fullname()}')

# my_date = datetime.date(2023, 4, 5)



print("\n" + "Classes and Instances" + "\n")


#emp1 = Employee("Robert", "LaBreche", 85000)
# emp2 = Employee("Test", "User", 50000)

# printing each employee will show they are stored at different locations in memory
# print(emp1)
# print(emp2)

# instances contain data that is unique to each instance

# emp1.first = "Robert"
# emp1.last = "LaBreche"
# emp1.email = "Robert.LaBreche@company.com"
# emp1.pay = 50000
#
# emp2.first = "Test"
# emp2.last = "User"
# emp2.email = "Test.User@company.com"
# emp2.pay = 50000
#
# print(emp1.email)
# print(emp2.email)
#
# emp1.fullname()
# emp2.fullname()
#
# Employee.fullname(emp1)
# Employee.fullname(emp2)

print("\n" + "-------------------------------------------------------" + "\n")
print("Class Variables" +" \n")
# Class Variables

# class variables are not the same as instance variables and should be the same for all instances
# class variables can only be accessed by the class itself or an instance of the class

# Changing the raise amount at the class level effects all instances of the class, changing the raise amount at the
# instance level only changes it for that instance

# print(emp1.pay)
# print(emp1.raise_amount)
# Employee.apply_raise(emp1)
# print(emp1.pay)
#
# print(emp2.pay)
# print(emp2.raise_amount)
# Employee.apply_raise(emp2)
# print(emp2.pay)
#
# print(Employee.num_of_emps)

# Class methods and static methods

# regular methods in a class automatically take the instance as the first argument
# class methods take the class in as the first argument
# to turn a regular method in a class method you add a decorator to the top called @classmethod
print("\n-------------------------------------------------------\n")
print("Class Methods and Static Methods \n")


# Employee.set_raise_amount(1.05)  # Changes the value for the class variable with the amount passed to the function
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print("\n")

# emp_str_1 = "John-Doe-70000"
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.fullname())
# print(new_emp_1.pay)
# print(new_emp_1.email)

#  static methods don't pass anything automatically, they don't pass the instance or the class
#  so they behave like regular functions, they are included in the class because they have a logical
#  connection to the class

# print(Employee.is_workday(my_date))

print("\n-------------------------------------------------------\n")

#  Inheritance: Creating Subclasses

print("Inheritance: Creating Subclasses\n")
#
# dev1 = Developer('Cindy', 'Eisenberger', 85000, 'HTML')
# print(dev1.email)
#
# # print(help(Developer))
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
#
# dev2 = Developer('Lily', 'LaBreche', 120000, 'Python')
# print(dev2.email)
# print(dev2.prog_lang)
#
#
#
# mgr1 = Manager('Sue', 'Smith', 90000, [dev1])
#
# mgr1.print_emps()
# print('\n')
#
# mgr1.add_emp(dev2)
# print(mgr1.email)
#
# print('\n')
# mgr1.print_emps()
# print('\n')
#
# mgr1.remove_emp(dev1)
# mgr1.print_emps()
#
# print(isinstance(mgr1, Manager))
# print(issubclass(Developer, Employee))


print("\n-------------------------------------------------------\n")
# Magic/Dunder Methods

# print("Magic/Dunder Methods\n")
#
# emp1 = Employee('Spike', 'Spiegel', 40000000)
#
# print(emp1)
#
# print(int.__add__(1, 2)) # we can change the behavior of the add built-in function
#
# print("\n-------------------------------------------------------\n")

print("Property Decorators: Getters, Setters, and Deleters\n")

emp4 = Employee('Holly', 'LaBreche', 100000)
emp4.fullname = 'Holly Dora'

dev1 = Developer('Ace', 'Ventura', 56000, 'SQL')



print(emp4.fullname)
print(emp4.email + '\n')

print(dev1.fullname)
print(dev1.email + '\n')

del dev1.fullname
