# typecasting
print(int("123"))

print("The number of letters in your name is: " + str(len(input("enter you name"))))

# rounding
height=float(input("what is your height in cm?"))/100
weight=float(input("what is your weight in kgs?"))
bmi = weight/height**2
print("your bmi is"+ str(round(bmi)))

# fstrings
print(f"Your weight is: {weight}, your height is: {height} and your BMI is: {bmi}")