# WAP to find the factorial of first n numbers. (using for)
n = int(input("Enter your number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i

print(fact)
