# Tresure finder
print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
first_step = input("where do you want to go? (left/right): ").lower()

if first_step == "left":
    print("Going to the left ....")
    status = input("Do you want to swim or wait? (swim/wait): ").lower()
    if status == "swim":
        print("Attacked by trout. Game Over!")
    elif status == "wait":
        door = input("Will you take the red, blue, or blue door? (red/blue/yellow): ").lower()
        if door == "yellow":
            print("You Win!")
        elif door == "blue":
            print("Eaten by beasts. Game Over!")
        elif door == "red":
            print("Burned by fire. Game Over!")
        else:
            print("Please enter a valid choice")
    else:
        print("Please enter a valid choice")
elif first_step == "right":
    print("You fell into a hole. Game over!")
else:
    print("Please enter a valid direction")