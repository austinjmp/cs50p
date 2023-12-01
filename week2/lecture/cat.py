# Loops Lecture

# i = 3

## Initial
# while i != 0:
#     print("Meow")
#     i = i - 1


## Same as previous
# while i <= 3:
#     print("Meow")
#     i = i + 1


# # While loop. Same as above use i = 0 (standard).
# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# # using a list and for loop.
# for i in [0, 1, 2]:
#     print("meow")


# # with pythonic variable
# for _ in range(3) # _ is for a variable that is irrelavent
#     print("meow")


# # using only print
# print("meow\n" * 3, end="")


# # using a force infinite loop while true
# while True:
#     n = int(input("Whats n? "))
#     if n > 0:
#         break
# for i in range(n):
#     print("meaow")

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
