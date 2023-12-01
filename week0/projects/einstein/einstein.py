# CS50 Week 0 Einstein assignment


# Ask for mass input in kg and call funciton energy calc
def main():
    kilos = int(input("Mass: "))
    energy = energy_calc(kilos)
    print(f"E: {energy:,}")


# Calculate energy based on mass argument and return energy in J
def energy_calc(emc2):
    c = int(300000000)
    emc2 = emc2 * c**2
    return emc2


main()
