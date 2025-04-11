# pizza shop
print("Welcome to Mangione's Pizza")
size = input("Which size pizza do you want? (s/m/l):\n")
pepporoni = input("Do you want extra pepporoni? y/n")
extra_cheese = input("Do you want extra cheese? y/n")
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("Please select a legit size")

if pepporoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}")