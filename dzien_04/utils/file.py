from pathlib import Path

from utils.calc import bmi


def load_data(nazwa_pliku, separator=";", enc="utf-8"):
    if not Path(nazwa_pliku).exists():
        print(f"Plik {nazwa_pliku} nie istnieje")
        return []

    return [
        linia.strip().split(separator) for linia in open(nazwa_pliku, "r", encoding=enc)
    ]


def clean_data(dane):
    # oczyszczenie i wzbogacenie danych
    dane_wynikowe = []
    for rekord in dane:
        waga = float(rekord[3])
        wzrost = float(rekord[2])
        imie = rekord[0].strip()
        nazwisko = rekord[1].strip()
        wbmi = bmi(wzrost, waga)

        dane_wynikowe.append([imie, nazwisko, wzrost, waga, wbmi])

    return dane_wynikowe
