# name = input("What is your name? ")
# print("Hello", name, sep="")
# print("Hello, ", end="")
# print(name)
# print(f"hello, {name}")

# Remove whitespace
# name = name.strip()
# name = name.capitalize()
# print(f"Hello, {name}")

# Remove whitespace and capitalize name 
# name = name.strip().title()
# print(f"Hello, {name}")

# Do all in one line
# name = input("What is your name? ").strip().title()

# #split user name into first and last names
# first, last = name.split(" ")

# print(f"Hello, {name}")
# print(f"Hello, {first}")
# print(f"Hello, {last}")

### Function section of lecture
## Hide functions by placing at bottom of program
# call the parameter 'to' as in hello 'to' someone
# def hello(to="world"): # assign 'world' as argument if no argument is provided
#     print("Hello,", to)
def main():
    name = input("What is your name? ")
    hello(name)     # Pass name as argument for 'to'




def hello(to="world"): 
    print("Hello,", to)


main()