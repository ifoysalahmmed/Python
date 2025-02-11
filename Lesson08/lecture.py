# Class & Object in Python
""" class Student: # creating a class
    name = "Foysal Ahmmed"


s1 = Student() # creating an object
print(s1.name) """


""" class Car: # creating a class
    color = "Red"
    brand = "ToyotaCar"


c1 = Car() # creating an object
print(c1.color)
print(c1.brand) """

# -------------------------------------------------------------------------------------

# creating a class with constructor (__init__ function)
""" class Student:
    # default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database")


s1 = Student("Foysal Ahmmed", 95)
print(s1.name, s1.marks)
s2 = Student("Foysal Ahmmed", 78)
print(s2.name, s2.marks) """

# -------------------------------------------------------------------------------------

# Class & Instance Attributes
""" class Student:
    # class attribute
    college_name = "Daffodil International University"  # common for all instances
    name = "anonymous"  # common for all instances

    def __init__(self, name, marks):  # instance attribute
        self.name = name  # object attr >> class attr
        self.marks = marks
        print("Adding new student in Database")


s1 = Student("Foysal Ahmmed", 95)
# print(s1.name, s1.marks, s1.college_name)
# print(s1.name, s1.marks, Student.college_name)  # can call class attribute using class name
print(s1.name) """

# -------------------------------------------------------------------------------------

# Methods
""" class Student:
    college_name = "Daffodil International University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("Foysal Ahmmed", 95)
s1.welcome()
print(s1.get_marks()) """

# -------------------------------------------------------------------------------------

# Static Methods
""" class Student:
    college_name = "Daffodil International University"

    @staticmethod  # decorator
    def welcome():
        print("welcome student")


s1 = Student()
s1.welcome() """

# -------------------------------------------------------------------------------------

# Important
# Abstraction & Encapsulation
""" class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")


car1 = Car()  # Encapsulation
car1.start() """

# -------------------------------------------------------------------------------------

# del keyword
""" class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Foysal Ahmmed")
print(s1.name)
del s1
print(s1) """

# -------------------------------------------------------------------------------------

# Private(like) attributes & methods
""" class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account(101, 1234)
print(acc1.acc_no)
acc1.reset_pass()
print(acc1.__acc_pass)  # error """


""" class Person:
    __name = "anonymous"  # private attribute

    def __hello(self):
        print("Hello Person!")  # private method

    def welcome(self):
        self.__hello()


p1 = Person()
# print(p1.__name)  # error
p1.welcome() """

# -------------------------------------------------------------------------------------


# Inheritance
# Single Inheritance
""" class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.color) """


# Multi-level Inheritance
""" class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("SUV")
car1.start() """


# Multiple Inheritance
""" class A:
    varA = "welcome to class A"


class B:
    varB = "welcome to class B"


class C(A, B):
    varC = "welcome to class C"


c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA) """

# -------------------------------------------------------------------------------------

# Super() method
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        super().start()
        self.name = name


car1 = ToyotaCar("fortuner", "SUV")
print(car1.type)


# Class Method
""" class Person:
    name = "anonymous"

    def change_name(self, name):
        # Person.name = name  # one way to access class attribute
        self.__class__.name = name  # another way to access class attribute

    @classmethod  # decorator for class method
    def change_name(cls, name):
        cls.name = name


p1 = Person()
p1.change_name("Foysal Ahmmed")
print(p1.name)
print(Person.name) """


# Property
""" class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = f"{(self.phy + self.chem + self.math) / 3:.2f}%"

    # def calc_percentage(self):
    #     return f"{(self.phy + self.chem + self.math) / 3:.2f}%"

    # better way to calculate percentage
    @property
    def calc_percentage(self):
        return f"{(self.phy + self.chem + self.math) / 3:.2f}%"  # getter


stu1 = Student(90, 80, 70)
print(stu1.calc_percentage)

stu1.chem = 85
print(stu1.chem)
print(stu1.calc_percentage) """

# -------------------------------------------------------------------------------------
# Polymorphism: Operator Overloading
""" print(5 + 6)  # 11
print("Foysal" + "Ahmmed")  # concatenate two string
print(type("Foysal"))  # <class 'str'>
print([1, 2, 3] + [4, 5, 6])  # merge two list """


""" class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(f"{self.real}i + {self.img}j")

    def __add__(self, other):  # dunder method
        newReal = self.real + other.real
        newImg = self.img + other.img
        return Complex(newReal, newImg)
        # return Complex(self.real+other.real, self.img+other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)


num1 = Complex(5, 4)
num1.show_number()
num2 = Complex(3, 2)
num2.show_number()

# num3 = num1.add(num2)
num3 = num1 + num2
print("After addition:")
num3.show_number()

num4 = num1 - num2
print("After subtraction:")
num4.show_number() """
