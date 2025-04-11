# nested conditionals
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm"))
bill = 0

if height >= 170:
    age = int(input("What is your age:"))
    if age < 10:
        bill = 7
        print(f"The rollercoaster will cost you ${bill}")
    elif 10 <= age < 18:
        bill = 12
        print(f"The rollercoaster will cost you ${bill}")
    else:
        bill = 20
        print(f"The rollercoaster will cost you ${bill}")
    wants_photo = input("Do you want a photo? y/n")
    if wants_photo == "y":
        bill += 3
    print(f"Yor final bill is: {bill}")
else:
    print("Sorry but you're not tall enough for the rollercoaster! The required minimum height is 170 cm")