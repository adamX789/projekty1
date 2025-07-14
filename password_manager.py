"""
    password manager
    """

from cryptography.fernet import Fernet


"""def ziskej_klic():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""


def nacti_klic():
    f = open("key.key", "rb")
    key = f.read()
    f.close()
    return key


key_r = nacti_klic()
fer = Fernet(key_r)


def pridat():
    jmeno = input("Uzivatelske jmeno: ")
    heslo = input("Heslo: ")
    with open("hesla.txt", "a", encoding="utf-8") as moje_hesla:
        encrypted_pass = fer.encrypt(heslo.encode()).decode()
        moje_hesla.write(f"{jmeno} || {encrypted_pass}\n")


def zobrazit():
    with open("hesla.txt", "r", encoding="utf-8") as moje_hesla:
        for radek in moje_hesla:
            data = radek.rstrip()
            user, passw = data.split(" || ")
            decrypted_pass = fer.decrypt(passw.encode()).decode()
            print(
                f"Uzivatelske jmeno: {user} | Heslo: {decrypted_pass}")


while True:
    choice = input(
        "Chcete pridat nove heslo, nebo jen zobrazit hesla, nebo ukoncit program (p/z/u): ").lower()
    if choice == "p":
        pridat()
    elif choice == "z":
        zobrazit()
    elif choice == "u":
        break
    else:
        print("Spatne zadana hodnota")
