"""
budík
    """

from datetime import datetime
from dateutil.relativedelta import relativedelta
from playsound import playsound


def vyber_dne():
    while True:
        try:
            d = int(
                input("Vyber den:\n0 - dnes\n1 - zitra\n2 - za 2 dny\n.....\n"))
            if d >= 0:
                return d
            raise ValueError
        except ValueError:
            print("Neplatna hodnota")


def vyber_h_m():
    while True:
        h_m_list = input(
            "Zadejte cas budiku v hodinach a minutach (hh:mm): ").split(":")
        if len(h_m_list) == 2:
            h = h_m_list[0].rstrip().lstrip()
            m = h_m_list[1].rstrip().lstrip()
            if len(h) == 2 and len(m) == 2:
                if 0 <= int(h) <= 23 and 0 <= int(m) <= 59:
                    return int(h), int(m)
        print("Jedna z hodnot je spatne zadana. Zkus znovu")


def urceni_casu(d, h, m):
    ted = datetime.now().replace(second=0, microsecond=0)
    days_left = d
    hours_left = h-ted.hour
    mins_left = m-ted.minute
    if hours_left < 0:
        days_left -= 1
        hours_left += 24
    if mins_left < 0:
        hours_left -= 1
        mins_left += 60
    cas_budiku = ted + relativedelta(days=days_left) + \
        relativedelta(hours=hours_left) + relativedelta(minutes=mins_left)
    return cas_budiku


def vytvoreni_budiku(cas_budiku):
    while True:
        if datetime.now() >= cas_budiku:
            print("\n\nHraje budik")
            playsound(
                "C:/Users/Adam/Documents/python_projekty/morning_flower.mp3")
        print(
            f"Zbyvajici cas: {cas_budiku - datetime.now().replace(microsecond=0)}", end="\r")


den = vyber_dne()
hod, mi = vyber_h_m()
cas = urceni_casu(den, hod, mi)
vytvoreni_budiku(cas)
