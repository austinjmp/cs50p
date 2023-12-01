# Meal Time for CS50p week 1


def main():
    tod = input("What time is it? ").strip()  # time of day in 24hr format
    meal = convert(tod)

    # Return appropriate meal
    if 7.0 <= meal <= 8.0:
        # print(f"{meal:.1f}")
        print("breakfast time")
    elif 12.0 <= meal <= 13.0:
        # print(f"{meal:.1f}")
        print("lunch time")
    elif 18.0 <= meal <= 19.0:
        # print(f"{meal:.1f}")
        print("dinner time")


def convert(time):
    time_split = time.split(":")  # split time at :
    hours = float(time_split[0])  # isolate hours
    mins = float(time_split[1])  # isolate mins
    dmin = mins / 60  # convert to time with decimals
    dtime = hours + dmin  # total time

    return dtime


if __name__ == "__main__":
    main()
