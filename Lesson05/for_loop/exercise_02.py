# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter your number: "))

for num in nums:
    if x == num:
        print(f"Found {x} in {num} index")
        break

    print("finding...")
