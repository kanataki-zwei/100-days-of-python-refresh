# tip calculator
total_bill = float(input("What is the total bill?\n"))
tip_percentage = float(input("What is the percentage tip you want to give?\n\n"))/100
num_people = int(input("How many people are splitting the bill?\n"))
bill_per_person = (total_bill + total_bill*tip_percentage)/num_people
print(f"Each person should pay: {bill_per_person}")