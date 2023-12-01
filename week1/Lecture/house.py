name = input("What's your house? ")


## Initial
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

## Combine gets long fast
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")


## Using Match Initial
# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _: # catch all
#         print("Who?")

## Using match combining previous
match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # catch all
        print("Who?")
