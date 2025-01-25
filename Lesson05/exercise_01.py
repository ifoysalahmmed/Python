# WAP to find the sum of first n numbers. (using while)
n = int(input("Enter your number: "))
count = 0
sum = 0
while count <= n:
    sum += count
    count += 1

print(sum)
