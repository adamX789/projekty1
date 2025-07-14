"""
    program na generovani prvocisel
    """


def generovat_prvocislo(i):
    pocet_delitelu = 0
    for num in range(1, i+1):
        if i % num == 0:
            pocet_delitelu += 1
    if pocet_delitelu <= 2:
        return i
    else:
        return None


def main():
    i_r = 0
    while True:
        volba = input("Chcete vygenerovat dalsi prvocislo? (a/n): ")
        if volba == "n":
            break
        if volba == "a":
            while True:
                i_r += 1
                prvocislo = generovat_prvocislo(i_r)
                if prvocislo:
                    print(prvocislo)
                    break
        else:
            print("Neplatna volba!")


if __name__ == "__main__":
    main()
