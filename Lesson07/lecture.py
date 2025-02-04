# https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function

""" # Writing to a file
f = open("c:/Users/Foysal/OneDrive/Documents/Python/Lesson07/demo.txt", "w")
f.write("I am also learning Java")
f.close() """

""" # Reading a file
f = open("c:/Users/Foysal/OneDrive/Documents/Python/Lesson07/demo.txt", "r")
# data = f.read()
# data = f.read(5)  # specify size text size to read
# print(data)
# print(type(data))
line1 = f.readline()  # reads one line at a time
print(line1)
line2 = f.readline()
print(line2)
f.close() """

""" # Append to a file
f = open("c:/Users/Foysal/OneDrive/Documents/Python/Lesson07/demo.txt", "a")
f.write("\nI am learning Python \nAnd it's good to leaning new technology")
f.close() """

""" # Read+ to a file
f = open("c:/Users/Foysal/OneDrive/Documents/Python/Lesson07/demo.txt", "r+")
f.write("abc")
print(f.read())
f.close() """

""" # with Syntax
with open("c:/Users/Foysal/OneDrive/Documents/Python/Lesson07/demo.txt", "r") as f:
    data = f.read()
    print(data) """

# Deleting a file
import os

os.remove("c:/Users/Foysal/OneDrive/Documents/Python/Lesson07/sample.txt")
