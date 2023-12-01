### Convert emoticons to emojis for cs50p week 0


def main():
    user_input = input("Enter: ")
    emoji = convert(user_input)  # call funtion convert with argument user_input
    print(emoji)


# replace emoticons from argument with emojis, retutn converted string
def convert(words):
    words = words.replace(":/", "😐")
    words = words.replace(":)", "🙂")
    words = words.replace(":(", "🙁")

    return words


main()
