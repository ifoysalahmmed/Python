# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.
def print_elem(lst, idx=0):
    if idx == len(lst):
        return
    print(lst[idx])
    print_elem(lst, idx + 1)


my_list = ["apple", "mango", "banana", "orange"]
print_elem(my_list)
