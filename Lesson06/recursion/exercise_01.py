# Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


print(sum(6))
