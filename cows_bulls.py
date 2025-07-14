"""
    cows and bulls game
    """

import random


def get_valid_number():
    while True:
        number_list = []
        number_list.append(random.randint(1, 9))
        for _ in range(3):
            number_list.append(random.randint(0, 9))

        new_list = []
        for item in number_list:
            if item not in new_list:
                new_list.append(item)
        if len(new_list) == 4:
            return new_list


def get_response(number_list, guess_list):
    cows = 0
    bulls = 0
    for number in number_list:
        if number in guess_list:
            if number_list.index(number) == guess_list.index(number):
                bulls += 1
            else:
                cows += 1
    return cows, bulls


def main():
    number_list_r = get_valid_number()
    while True:
        while True:
            try:
                guess = int(input("Guess: "))
                guess_list_r = list(map(int, str(guess)))
                if len(guess_list_r) == 4:
                    break
                print("Guess has to be 4 digits")
            except ValueError:
                print("Invalid value")

        cows_r, bulls_r = get_response(number_list_r, guess_list_r)
        if bulls_r == 4:
            break
        print(f"Response: {bulls_r} bulls, {cows_r} cows")

    print("You guessed right!")


if __name__ == "__main__":
    main()
