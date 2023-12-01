# x = input("x: ")
# y = input("y: ")

# z = int(x) + int(y)

## Integer
# x = int(input("x: "))
# y = int(input("y: "))

#Decimal
# x = float(input("x: "))
# y = float(input("y: "))

# # # Round to nearest number
# # z = round(x + y)

# #Round division to 2 decimals
# z = round(x / y, 2)

# #print(z)

# # # Format z with coma
# # print(f"{z:,}")

# #Round to 2 decimals with f string
# print(f"{z:.2f}")

### Functions and return

def main():
    x = int(input("x: "))
    print("x squared is", square(x))

def square(n):
    return n * n # To do the same: pow(x, 2); n ** 2
    

main()




