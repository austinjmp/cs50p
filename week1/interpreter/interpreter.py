# Math interpreter for CS50p week 1


# get user input and call calc function
def main():
    expression = input("Expression: ").strip()
    answer = calc(expression)
    print(f"{answer:.1f}")


# isolate the operator and do appropraite calc
def calc(n):
    components = n.split()
    operator = components[1]  # selects the operator

    match operator:
        case "+":
            result = float(components[0]) + float(components[2])
            return result
        case "-":
            result = float(components[0]) - float(components[2])
            return result
        case "*":
            result = float(components[0]) * float(components[2])
            return result
        case "/":
            result = float(components[0]) / float(components[2])
            return result


main()
