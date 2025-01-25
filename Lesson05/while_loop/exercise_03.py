# Print the multiplication table of a number n.
n = int(input("Enter your table number: "))
count = 1
while count <= 10:
    print(f"{n} x {count} = {n*count}")
    count += 1
