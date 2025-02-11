# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        avg = sum / self.marks.__len__()
        print(f"Hi, {self.name}. Your average score is: {avg}")


s1 = Student("Foysal Ahmmed", [95, 85, 75])
s1.print_avg()

s1.name = "Ironman"
s1.print_avg()
