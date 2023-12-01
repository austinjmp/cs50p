# % modulo operator. Calculate remainder (not division)


## Initial
# x = int(input("x: "))

# if x / 2 == 0:
#     print("even")
# else:
#     print("odd")


## Using Main function
def main():
    x = int(input("x: "))
    if is_even(x): # if true
        print("even")
    else: #if false
        print("odd")


def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    ## Pythonic
    #return True if n % 2 == 0 else False

    ## If boolean is itself true or false. Most concise. if true: returns true
    return n % 2 == 0


main()
