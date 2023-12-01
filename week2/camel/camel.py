# CS50p camelCase to snake_case converter


def main():
    camel = input("camelCase: ")
    snake = camel_to_snake(camel).lower()
    print(snake)


def camel_to_snake(n):
    snake = ""

    # iterate until uppercase then and an underscore
    for i in n:
        if i.isupper():
            snake += "_" + i
        else:
            snake += i

    return snake


main()
