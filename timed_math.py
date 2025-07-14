"""
    timed math challenge
    """

import random
import operator
import time
from playsound import playsound

operations = {"+": operator.add, "-": operator.sub,
              "*": operator.mul, "%": operator.mod}


def get_numbers():
    lower = 3
    upper = 15
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, upper)
    return num1, num2


def get_operation():
    operation_list = ["+", "-", "*", "%"]
    operation = random.choice(operation_list)
    return operation


pocet_otazek = 4
while True:
    start = input("Stiskni Enter pro spusteni vyzvy: ")
    if start == "":
        print("-------------------------------------------\n")
        t = time.time()
        for i in range(pocet_otazek):

            num1_r, num2_r = get_numbers()
            operation_r = get_operation()
            answer = operations[operation_r](num1_r, num2_r)

            while True:
                try:
                    user_guess = int(
                        input(f"Otazka #{i+1}: {num1_r} {operation_r} {num2_r} = "))
                    if user_guess == answer:
                        break
                except ValueError:
                    print("Zadana hodnota neni cislo!")

        current_timer = time.time() - t
        playsound("get_out.mp3")
        print(f"""\n-------------------------------------------
        Gratuluji, zodpovedel jsi vsechny otazky spravne za {current_timer:.2f}s""")
        break
