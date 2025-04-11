# check for even or uneven numbers
print("Welcome to the number checker!")
number = int(input("Please enter a random whole number:"))
result = number%2
if result != 0:
    print(f"{number} is an odd number")
else:
    print(f"{number} is an even number")