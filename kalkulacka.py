"""
    kalkulacka
    """

import operator


def calc(c1, c2, operation):
    answer = operations[operation](c1, c2)
    return answer


operations = {"+": operator.add, "-": operator.sub,
              "*": operator.mul, "/": operator.truediv,
              "%": operator.mod, "^": operator.pow}


def main():
    operation_list = ["+", "-", "*", "/", "%", "^"]
    while True:
        try:
            c1_r = int(input("Zadejte prvni cislo: "))
            while True:
                operation_r = input("Zadejte operaci (+, -, *, /, %, ^): ")
                if operation_r not in operation_list:
                    print("Neplatna operace")
                else:
                    break
            c2_r = int(input("Zadejte druhe cislo: "))
            break
        except ValueError:
            print("Neplatna hodnota")

    answer_r = calc(c1_r, c2_r, operation_r)
    print(f"{c1_r} {operation_r} {c2_r} = {answer_r}")


if __name__ == "__main__":
    main()
