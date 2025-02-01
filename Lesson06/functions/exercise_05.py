# WAP to define even or odd
def check_even_odd(n):
    if n > 0:
        if n % 2 == 0:
            print(f"{n} is a even number")
        else:
            print(f"{n} is a odd number")
    else:
        print("Enter a number that is greater than 0")


check_even_odd(10)
