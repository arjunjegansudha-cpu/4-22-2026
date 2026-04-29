a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

print(f"Before swap: a = {a}, b = {b}, c = {c}")

a, b, c = b, c, a

print(f"After swap:  a = {a}, b = {b}, c = {c}")