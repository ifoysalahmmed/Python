# From a file containing numbers separated by comma, print the count of even numbers.
with open("practice.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    count = 0
    for num in nums:
        if int(num) % 2 == 0:
            count += 1
    print(count)
