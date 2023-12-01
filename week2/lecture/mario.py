# for _ in range(3):
#     print("#")


# def main():
# print_column(3)
# print_row(4)


## Print columns
# def print_column(height):
#     for _ in range(height):
#         print("#\n" * height, end="")


## Print Rows
# def print_row(width):
#     print("?" * width)


def main():
    print_square(3)


def print_square(size):
    # Print i rows in square. For each row:
    # for i in range(size):

    # # Print J cols in square. For each col:
    # for j in range(size):
    #     #print("#", end="")

    # print() # Print to a new line after each row

    # for i in range(size):
    # print("#" * size)

    for i in range(size):
        print_row(size)


# Abstraction for printing rows
def print_row(width):
    print("#" * width)


main()
