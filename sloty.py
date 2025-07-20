"""
    gambling part 1
    """

import random

MAX_RADKU = 3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


class Sloty:
    def __init__(self) -> None:
        self.balance = self.deposit()

    @staticmethod
    def deposit():
        while True:
            try:
                amount = int(input("Kolik Kc chces do hry dat?: "))
                if amount > 0:
                    print(f"{amount} Kc vlozeno uspesne!")
                    return amount
                raise ValueError
            except ValueError:
                print("Neplatna hodnota")

    @staticmethod
    def volba_pokracovani():
        while True:
            volba = input(
                "Stiskni Enter pro hrani hry a k pro ukonceni: ").lower()
            if volba == "":
                return True
            elif volba == "k":
                return False
            else:
                print("Neplatna volba!")

    def get_bet(self):
        while True:
            try:
                pocet_radku = int(
                    input(f"Na kolik radku chces vsadit? (1-{MAX_RADKU}): "))
                if pocet_radku < 1 or pocet_radku > MAX_RADKU:
                    raise ValueError
                sazka = int(
                    input("Kolik Kc chces vsadit na kazdy radek?: "))
                if (sazka*pocet_radku) <= self.balance:
                    print(
                        f"Sazis {sazka} Kc na {pocet_radku} radky. Celkova sazka je {sazka*pocet_radku} Kc\n")
                    self.balance -= (sazka*pocet_radku)
                    return pocet_radku, sazka
                print("Nemuzes vsadit vice Kc nez mas!")
            except ValueError:
                print("Neplatna hodnota")

    @staticmethod
    def add_to_list():
        symbol_list = []
        for char, value in symbol_count.items():
            for _ in range(value):
                symbol_list.append(char)
        return symbol_list

    def choose_from_list(self, l):
        new_list = []
        for _ in range(9):
            item = random.choice(l)
            new_list.append(item)
            l.remove(item)
        random.shuffle(new_list)
        return new_list

    def print_board(self, new_l):
        rows = [new_l[i*3:(i+1)*3] for i in range(MAX_RADKU)]
        for row in rows:
            print(f"| {" | ".join(row)} |")

    def urci_vyhru(self, new_l, pocet, sazka):
        vyhrana_castka = 0
        winning_lines = []
        rows = [new_l[i*3:(i+1)*3] for i in range(MAX_RADKU)]
        for row in rows:
            pocet -= 1
            if len(set(row)) == 1:
                winning_char = row[0]
                vyhrana_castka += sazka * symbol_value[winning_char]
                winning_lines.append(str(rows.index(row) + 1))
            if pocet == 0:
                break
        print(f"\nVyhral jsi {vyhrana_castka} Kc! ")
        print(f"Vyhral jsi na radach: {", ".join(winning_lines)}")
        self.balance += vyhrana_castka


def hraj(hra):
    while hra.balance > 0:
        print(f"\n\nMas {hra.balance} Kc\n")
        if not hra.volba_pokracovani():
            break
        list1 = hra.add_to_list()
        list2 = hra.choose_from_list(list1)
        pocet_r, saz = hra.get_bet()
        hra.print_board(list2)
        hra.urci_vyhru(list2, pocet_r, saz)
    if hra.balance > 0:
        print(f"\nUkoncil jsi hru a odesel jsi s {hra.balance} Kc!")
    else:
        print("\nProhral jsi vsechny svoje penize a uz nemuzes dal hrat :(")


if __name__ == "__main__":
    h = Sloty()
    hraj(h)
