# place1 = input("Tell me a place: ")
# obj1 = input("Give me an object: ")
# madLib = f"Just as I arrived at {place1}, I realized I had forgotten my {obj1}"
# print(madLib)

def madLib():
    place1 = input("Tell me a place: ")
    obj1 = input("Give me an object: ")
    madLibString = f"Just as I arrived at {place1}, I realized I had forgotten my {obj1}"
    return(madLibString)


print(madLib())
