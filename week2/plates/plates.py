def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# check if plate is valid, returns invalid if a test is failed
def is_valid(s):
    if checklength(s) is False:
        return False
    elif first_two_chars(s[0:2]) is False:
        return False
    elif punctuation(s) is False:
        return False
    elif num_check(s) is False:
        return False
    else:
        return True


# check the length of the plate (2-6) characters
def checklength(plate_length):
    if 2 <= len(plate_length) <= 6:
        return True
    else:
        return False


# check if first two characters are letters
def first_two_chars(n):
    return not n.isnumeric()


# check if there is any punctuation
def punctuation(plate_punc):
    punc = ".,!?'  "
    for character in plate_punc:
        if character in punc:
            return False

    return True


# check that the first number is 0 and there are no trailing letters
def num_check(plate_nums):
    plate_nums = plate_nums.lower()
    remove_letters = plate_nums.lstrip("abcdefghijklmnopqrstuvwxyz")
    if remove_letters[0] == "0":  # check for leading 0
        return False
    else:
        return remove_letters.isnumeric()  # check for trailing letters


main()
