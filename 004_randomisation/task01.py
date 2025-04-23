# import random module
import random

# print random int between a number range
print(random.randint(1,11))

# print a random item in a list
list_var = [1,2,3,4,5]
print(random.choice(list_var))

# shuffle a deck
deck = list(range(1,53))
random.shuffle(deck)
print(deck)