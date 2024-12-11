#### ZADANIE 20

# Wczytaj dane z pliku zawodnicy.csv, wylicz dla każdej z osób współczynnik BMI.
# Całość posortuj po nazwisku i zapisz do pliku wyniki.csv.


# # konfiguracja
# nazwa_pliku_wejsciowego = "zawodnicy.csv"
# nazwa_pliku_wyjsciowego = "wyniki2.csv"
# separator = ";"

# # wczytanie danych
# dane = [
#     linia.strip().split(separator)
#     for linia in open(nazwa_pliku_wejsciowego, "r", encoding="utf-8")
# ]

# # oczyszczenie i wzbogacenie danych
# dane_wynikowe = []
# for rekord in dane:
#     waga = float(rekord[3])
#     wzrost = float(rekord[2])
#     imie = rekord[0].strip()
#     nazwisko = rekord[1].strip()
#     bmi = waga / (wzrost / 100) ** 2

#     dane_wynikowe.append([imie, nazwisko, wzrost, waga, bmi])


# # sortowanie listy po nazwisku
# dane_wynikowe = sorted(dane_wynikowe, key=lambda r: r[1])

# wyświetlenie na ekranie ładnych wyników
# for r in dane_wynikowe:
#     # print(f"{r[0]} {r[1]} ({r[2]} cm, {r[3]} kg) ma BMI = {r[4]:.2f}")
#     print(f"{r[0]};{r[1]};{r[2]};{r[3]};{r[4]}")

# wersja 1:
# plik = open(nazwa_pliku_wyjsciowego, "w", encoding="utf-8")
# for r in dane_wynikowe:
#     linia = f"{r[0]};{r[1]};{r[2]};{r[3]};{r[4]}\n"
#     plik.write(linia)
# plik.close()


# wersja 2:
# dane_do_zapisania = [f"{r[0]};{r[1]};{r[2]};{r[3]};{r[4]}\n" for r in dane_wynikowe]
# plik = open(nazwa_pliku_wyjsciowego, "w", encoding="utf-8")
# plik.writelines(dane_do_zapisania)
# plik.close()


# wersja 3:
# dane_do_zapisania = []
# for r in dane_wynikowe:
#     r_str = [str(element_r) for element_r in r]
#     linia = ";".join(r_str) + "\n"
#     dane_do_zapisania.append(linia)

# plik = open(nazwa_pliku_wyjsciowego, "w", encoding="utf-8")
# plik.writelines(dane_do_zapisania)
# plik.close()


# wersja 2' - context manager
# dane_do_zapisania = [f"{r[0]};{r[1]};{r[2]};{r[3]};{r[4]}\n" for r in dane_wynikowe]
# # plik = open(nazwa_pliku_wyjsciowego, "w", encoding="utf-8")
# with open(nazwa_pliku_wyjsciowego, "w", encoding="utf-8") as plik:
#     plik.writelines(dane_do_zapisania)
