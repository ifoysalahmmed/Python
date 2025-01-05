# WAP to find the greatest of 3 numbers entered by the user.
first_num = int(input("enter your first number: "))
second_num = int(input("enter your second number: "))
third_num = int(input("enter your third number: "))

if first_num >= second_num and first_num >= third_num:
    print(f"First number is greater: {first_num}")
elif second_num >= third_num:
    print(f"Second number is greater: {second_num}")
else:
    print(f"Third number is greater: {third_num}")
