# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter your number: "))
idx = 0
while idx < len(nums):
    if x == nums[idx]:
        print(f"Found {x} in {idx} index")
        break
    else:
        print("finding...")
    idx += 1
