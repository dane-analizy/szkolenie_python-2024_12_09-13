import json
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


def change_data(dane):
    wynikowe_dane = []
    for r in dane:
        temp_dict = {
            "imie": r[0],
            "nazwisko": r[1],
            "wzrost": r[2],
            "waga": r[3],
            "bmi": r[4],
        }
        wynikowe_dane.append(temp_dict)

    return wynikowe_dane


def save_data_to_json(dane, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as f:
        json.dump(dane, f, indent=4)
