#### ZADANIE 20

# Wczytaj dane z pliku zawodnicy.csv, wylicz dla każdej z osób współczynnik BMI.
# Całość posortuj po nazwisku i zapisz do pliku wyniki.csv.


# nazwa_pliku = "zawodnicy.csv"
# sep = ";"

# # wczytanie danych
# dane = [linia.strip().split(sep) for linia in open(nazwa_pliku, "r", encoding="utf-8")]


# # oczyszczenie i wzbogacenie danych
# dane_wynikowe = []
# for rekord in dane:
#     waga = float(rekord[3])
#     wzrost = float(rekord[2])
#     imie = rekord[0].strip()
#     nazwisko = rekord[1].strip()
#     dane_wynikowe.append([imie, nazwisko, wzrost, waga, bmi])

# # wyświetlenie na ekranie ładnych wyników
# for r in dane_wynikowe:
#     print(f"{r[0]} {r[1]} ({r[2]} cm, {r[3]} kg) ma BMI = {r[4]:.2f} ({r[5]})")
