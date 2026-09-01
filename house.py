name=input("What's your name? ")

# if name=="Harry" or name=="Hermione" or name =="Ron" :
#     print("Gryffindor")
# elif name=="Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# using match condition
match name:
    case "Harry" | "Hermione"|"Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")