# single input
def greet(name):
    print(f"Hello {name}") 
greet("Iron man")

# optional input
def greet2(name="Guest"):
    print(f"Hello {name}") 
greet2()

# using multiple inputs
def addnumbers(a,b):
    print(a+b)
addnumbers(3,5)

# using type hinted input
def greet3(name: str):
    print(f"Howdy {name}")
greet3("Patrick")

# using multiple type hinted inputs
def multiply(a:int, b:float)-> float:
    multiplied = a*b 
    return multiplied
multiply(3, 5.4)
