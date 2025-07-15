"""
    piskvorky
    """

symbol_list = ["X", "O"]
vitez = False


def ziskej_spravny_tah():
    while True:
        try:
            tah_f = int(input("Zadej cislo pole, kam chces tahnout (1-9): "))
            if tah_f in seznam_tahu:
                print("Tohle pole uz je obsazene")
                continue
            if 1 <= tah_f <= 9:
                return tah_f
        except ValueError:
            print("Spatna hodnota")


def nekdo_vyhral(tahy_f, symbol_list):
    for radek in tahy_f:  # hledani stejnych symbolu v radcich
        if len(set(radek)) == 1 and radek[0] in symbol_list:
            return True

    for x in range(3):  # hledani stejnych symbolu ve sloupcich
        tahy_set = set()
        for y in range(3):
            tahy_set.add(tahy_f[y][x])
        if len(tahy_set) == 1 and tahy_f[y][x] in symbol_list:
            return True
    if (tahy_f[0][0] == tahy_f[1][1] == tahy_f[2][2] or tahy_f[2][0] == tahy_f[1][1] == tahy_f[0][2]) and tahy_f[1][1] in symbol_list:  # diagonaly
        return True
    return False


print(f"Hrac 1: {symbol_list[0]}\nHrac 2: {symbol_list[1]}")

print("Pokyny ke hre: policka jsou ocislovana od 1 do 9, napiste cislo, aby jste vykonali tah na dane policko:")
print("""1 | 2 | 3
_   _   _
4 | 5 | 6
_   _   _
7 | 8 | 9 \n""")

tahy = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

seznam_tahu = []

while not vitez:
    for i in range(len(symbol_list)):
        print(f"Hraje hrac {i+1} ({symbol_list[i]})")
        tah = ziskej_spravny_tah()
        if 1 <= tah <= 3:
            tahy[0][tah-1] = symbol_list[i]
        elif 4 <= tah <= 6:
            tahy[1][tah-4] = symbol_list[i]
        else:
            tahy[2][tah-7] = symbol_list[i]
        seznam_tahu.append(tah)
        print("Hraci deska:")
        for j in range(3):
            print(" | ".join(tahy[j]))
        vitez = nekdo_vyhral(tahy, symbol_list)
        if vitez:
            break
        if len(seznam_tahu) >= 9:
            print("Hra skoncila remizou")
            quit()

print(f"Vyhral hrac {i+1} ({symbol_list[i]})! Gratuluji!")
