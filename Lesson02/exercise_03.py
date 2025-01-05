# Grade students based on marks
marks = float(input("enter your marks: "))

if marks >= 90:
    print("A")
elif marks < 90 and marks >= 80:
    print("B")
elif marks < 80 and marks >= 70:
    print("C")
else:
    print("D")
