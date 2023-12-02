# Calculated amount owned for purchasing coke


def main():
    price = int(50)
    denominations = ["5", "10", "25"]
    remainder = price

    # while there is still an amount owed, request coins (within denominations)
    while remainder > 0:
        coins = input("Insert Coins: ")

        if coins in denominations:
            remainder = remainder - int(coins)

        if remainder > 0:
            print("Amount Due:", remainder)
        else:
            print("Change Owed:", abs(remainder))


main()
