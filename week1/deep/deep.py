def main():
    answer = (
        input(
            "What is the Answer to the Greatest Question of Life, the Universe and Everyhting? "
        )
        .lower() # set to lowercase
        .strip() # remove spaces
    )
    match answer:
        case 42 | "42" | "forty-two" | "forty two": 
            print("Yes")
        case _:
            print("No")


main()
