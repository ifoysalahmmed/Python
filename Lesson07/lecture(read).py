# Reading a file
f = open("I:\Foysal\Programming\Python\Lesson07\demo.txt", "r")
# data = f.read()
# data = f.read(5)  # specify size text size to read
# print(data)
# print(type(data))
line1 = f.readline()  # reads one line at a time
print(line1)
line2 = f.readline()
print(line2)
f.close()
