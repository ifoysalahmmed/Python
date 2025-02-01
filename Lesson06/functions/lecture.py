# function definition
def calc_sum(a, b):  # parameters
    return a + b


sum = calc_sum(12, 12)  # function call; arguments
# print(sum)


def print_hello():
    print("Hello")


# print_hello()
# print_hello()
# print_hello()


# average of 3 numbers
def avg_nums(a, b, c):
    return (a + b + c) / 3


# print(f"{avg_nums(23, 44, 12):.2f}")


# default value in parameters
def calc_prod(a=1, b=2):
    sum = a + b
    print(sum)
    return sum


calc_prod()
