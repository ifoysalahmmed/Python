# Qs
# Define an Employee class with attributes role, department & salary. This class also has a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        return (
            f"Role: {self.role}\nDepartment: {self.department}\nSalary: {self.salary}"
        )


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Manager", "HR", 50000)

    def employeeDetails(self):
        return f"Name: {self.name}\nAge: {self.age}\n{self.showDetails()}"


eng1 = Engineer("John", 30)
print(eng1.employeeDetails())
