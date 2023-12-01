def main():
    # Get input and remove all commas and extra spaces. Set to lowercase
    greeting = input("Greeting: ").replace(","," ").strip().lower()
    words = greeting.split() # split words to check for 'hello'

    # check conditions
    if words[0] == "hello":
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")


main()

