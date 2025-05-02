# using kwargs in defining function input
# using kwargs
def greet(**kwargs):
    name = kwargs.get("name", "Guest")
    location = kwargs.get("location", "Mombasa")
    print(f"Hello {name}, how is it like in {location}")

greet(name="Patrick", location="Delaware", age=30, mood="happy")  
