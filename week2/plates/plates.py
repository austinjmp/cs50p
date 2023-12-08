def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    print(s)
    if checklength(s) is False:
        return False
    elif first_two_chars(s[0:2]) is False:
        return False
    elif punctuation(s) is False:
        return False
    else:
        return True


def checklength(plate_length):
    if 2 <= len(plate_length) <= 6:
        return True
    else:
        return False


def first_two_chars(n):
    return not n.isnumeric()


def punctuation(plate_punc):
    punc = ".,!?'  "
    for character in plate_punc:
        if character in punc:
            return False

    return True


main()
