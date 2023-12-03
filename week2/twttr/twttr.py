def main():
    tweet = input("Input: ").strip()  # get users tweet
    print(remove_vowels(tweet))  # call function to remove vowels


def remove_vowels(user_input):
    # vowels list
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # initiate empty vowels string
    no_vowels = str()

    # for each letter in the tweet, if it is not part of [vowels], add letter to return. Otherwise skip.
    for letter in user_input:
        if letter not in vowels:
            no_vowels = no_vowels + letter

    return no_vowels


main()
