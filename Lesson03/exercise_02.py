# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
num_list = [1, 2, 3, 2, 1]
str_list = [1, "abc", "abc", 1]

copy_num_list = num_list.copy()
copy_num_list.reverse()
copy_str_list = str_list.copy()
copy_str_list.reverse()

if num_list == copy_num_list:
    print("Number list is palindrome")
else:
    print("Number list is not palindrome")


if str_list == copy_str_list:
    print("String list is palindrome")
else:
    print("String list is not palindrome")
