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


### Krotki = tuple

# lista = [1,2,3, "abc", "def"]
# krotka = (1, 2, 3, "abc", "def", "abc")
# print(lista)
# print(krotka)

# krotka_z_listy = tuple(lista)
# print(krotka_z_listy)


# ile czasu wykonuje się program?
# import time

# l = list(range(100_000))
# start_time = time.perf_counter()
# suma = 0
# for el in range(10_000):
#     suma = suma + l[el*10]
# end_time = time.perf_counter()
# print(end_time - start_time)

# k = tuple(range(100_000))
# start_time = time.perf_counter()
# suma = 0
# for el in range(10_000):
#     suma = suma + k[el*10]
# end_time = time.perf_counter()
# print(end_time - start_time)

# scalenie dwóch list
# l1 = [1,2,3]
# l2 = ["a", "b", "c"]
# l3 = l1 + l2
# print(l3)

# scalenie listy i krotki
# l1 = [1, 2, 3]
# k2 = ("a", "b", "c")
# k3 = tuple(l1) + k2
# print(k3)

# l3 = l1 + list(k2)
# print(l3)

# l = [i**2 for i in range(10)]
# k = tuple(l)

# sortowanie krotek, sorted() zwraca listę!
# k = (1,3,4,2)
# print(sorted(k))


# 100 losowych liczb od 0 do 100
# import random
# for _ in range(100):
#     print(random.randint(0, 100))


#### ZADANIE 21

# Stwórz dwie krotki:
# - jedna ma zawierać 10 losowych liczb zakresu 1-10,
# - druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek.
# Trzecią krotkę wypisz na konsoli.
# Stwórz czwartą krotkę, która będzie posortowaną malejąco trzecią krotką. Też wypisz ją na konsoli.

# import random

# k1 = tuple([random.randint( 1, 10) for _ in range(10)])
# k2 = tuple([random.randint(11, 20) for _ in range(10)])

# k3 = k1 + k2
# print(k3)

# k4 = tuple(sorted(k3, reverse=True))
# print(k4)

# czy lista jest pusta?
# l = [1]
# if l:
#     print("lista nie pusta")
# else:
#     print("lista jest pusta")


# iterowanie po pustej kolekcji:
#  l = ["a", "b", "c"]
# l = []
# for i, el in enumerate(l):
#     print(i, el)


# lista plików: os.walk vs pathlib

# listowanie rekurencyjne plików i katalogów

# import os

# for s in os.walk(".."):
#     # print(s) (aktualny katalog, lista katalogów, lista plików)
#     print(f"ŚCIEŻKA: {s[0]}")
#     print("=== Pliki:")
#     for p in s[2]:
#         nazwa_pliku = os.path.join(s[0], p)
#         print(f"\t{nazwa_pliku}")

#     print("=== Katalogi:")
#     for k in s[1]:
#         nazwa_katalogu = os.path.join(s[0], k)
#         print(f"\t{nazwa_katalogu}")

#     print()


# podobnie z wykorzystaniem pathlib

# from pathlib import Path

# sciezka = Path("..")
# print(sciezka.anchor)
# print(sciezka.absolute())
# print(sciezka.exists())
# print(sciezka.is_dir())
# print(sciezka.is_file())
# print(sciezka.name)
# print(sciezka.as_posix())
# print(sciezka.stat())

# for s in sciezka.rglob("*"):
#     typ = "PLIK" if s.is_file() else "KATALOG"
#     # ta jedna linijka odpowiada:
#     # if s.is_file():
#     #     typ = "PLIK"
#     # else:
#     #     typ = "KATALOG"

#     print(s, typ, s.stat().st_size)


# czy string kończy się albo zaczyna na podany ciąg:
# s = "napis"
# print(s.endswith("is"))
# print(s.startswith("NA"))


#### ZADANIE 22

# Pobierz od użytkownika nazwę katalogu i rozszerzenie pliku. Wyświetl wszystkie pliki, które
# znajdują się we wskazanym katalogu (i jego w głąb) z podanym rozszerzeniem WIĘKSZE niż 1000 bajtów.

# from pathlib import Path

# nazwa_katalogu = input("Gdzie szukać? ")
# rozszerzenie = input("Jakich plików szukać (rozszerzenie)? ")

# for s in Path(nazwa_katalogu).rglob("*"):
#     if s.as_posix().endswith(rozszerzenie) and s.stat().st_size > 15_000:
#         print(s, s.stat().st_size)

# wykorzystując możliwości Path()

# from pathlib import Path

# nazwa_katalogu = input("Gdzie szukać? ")
# rozszerzenie = input("Jakich plików szukać (rozszerzenie)? ")

# for s in Path(nazwa_katalogu).rglob(f"*{rozszerzenie}"): # bierzemy pliki pasujące do maski
#     if s.stat().st_size > 10:
#         print(s, s.stat().st_size)


# grep - wyszukiwanie tekstu w pliku
# grep -irn ciag katalog

# import sys
# from pathlib import Path

# if len(sys.argv) < 3:  # ile podano parametrów
#     katalog = input("Gdzie szukać?:")
#     ciag = input("Czego szukać?: ")
# else:
#     katalog = sys.argv[1]
#     ciag = sys.argv[2]

# for s in Path(katalog).rglob("*"):
#     # wczytujemy plik linia po linii
#     if s.is_dir():
#         continue
#     try:
#         for nr_linii, linia in enumerate(open(s.as_posix(), "r", encoding="utf-8"), start=1):
#             # jedziemy przez linie i sprawdzamy czy istnieje poszukany ciąg - wyświeltamy jeśli tak
#             if ciag.lower() in linia.lower():
#                 print(f"{s.as_posix():<30} : {nr_linii:>6} > {linia.strip()}")
#     except Exception:
#         pass


# zbiory = set

# l = [1, 2, "a", "b", "c", 5, 1, 2, "a"]
# k = (10, 20, "abc", "bdg", 20)

# ls = set(l)
# ks = set(k)

# print(set(ls))
# print(set(ks))


# l = [1,1,2,3,4,1,2,5]
# ls = set(l)
# ks = {4,5,6,7,8}
# print(ls)
# print(ks)

# ls.add(1)
# print(ls)

# # część wspólna
# print(ls.intersection(ks))

# # różnica zbiorów
# print(ls.difference(ks))
# print(ks.difference(ls))

# # suma zbiorów
# print(ks.union(ls))


# lista = [1, 1, 2, 3, 4, 1, 2, 5]
# lista_unikalna = list(set(lista))
# print(lista_unikalna)


# lista = [ [1, 2], ["a", "b", "c"], [10, "xyz"]]
# s = set(lista)
# print(s)

# import hashlib

# print(hashlib.sha256(b"alamakota123").hexdigest())
# print(hashlib.sha256(b"Alamakota123").hexdigest())
# print(hashlib.sha256(b"alamakota123").hexdigest())

# # alamakota123 => 082faf35398a2e2659fc38bb6be004ae7133bcc0f0f8464380206341cb95793e
# print("alamakota123".__hash__())
# l = [123, 123]
# l.__hash__()

#  komis = [Auto(64u4ju), Auto(aqgqg)]


#### ZADANIE 23

# Przygotuj listę 100 losowych liczb z zakresu 1-50.
# Wyświetl na konsoli unikalne liczby w kolejności rosnącej.

# import random

# losowe_liczby = [random.randint(1, 50) for _ in range(100)]
# print(sorted(set(losowe_liczby)))


# pakiety zewnętrzne
# https://pypi.org/


# pakiet Faker - tworzy sztuczne dane
# pip install faker
# albo:
# python -m pip install faker

# import faker
# f = faker.Faker()

# albo:

# from faker import Faker

# f = Faker('pl_PL')

# print("f.name():", f.name())
# print("f.address():", f.address())
# print("f.phone_number():", f.phone_number())
# print("f.street_name():", f.street_name())
# print("f.first_name():", f.first_name())
# print("f.last_name():", f.last_name())
# print("f.city():", f.city())
# print("f.company():", f.company())
# print("f.email():", f.email())
# print("f.building_number():", f.building_number())


#### ZADANIE 24

# Korzystając z pakietu Faker wygeneruj plik CSV zawierający 10 tysięcy rekordów zawierających:
# id będące liczbą porządkową, imię, nazwisko, nazwa firmy, email, telefon, miasto, ulica i numer domu

# 1. import Fakera
from faker import Faker

# 2. inicjalizacja klasy
f = Faker("pl_PL")

# 3. w pętli 10 tysięcy razy generujemy odpowiednie "składkowe"
lista_osob = []
for id in range(10_000):
    osoba = [
        str(id + 1),
        f.first_name(),
        f.last_name(),
        f.company(),
        f.email(),
        # f.postalcode(), ###
        f.phone_number(),
        f.city(),
        f.street_name(),
        f.building_number(),
    ]
    lista_osob.append(osoba)

# 4. scalamy w jedną linię rozdzieloną ;
dane_wyjsciowe = []
for o in lista_osob:
    linia = f"{o[0]};{o[1]};{o[2]};{o[3]};{o[4]};{o[5]};{o[6]};{o[7]};{o[8]}\n"
    dane_wyjsciowe.append(linia)

# 5. lista nazw kolumn
kolumny = "id;first_name;last_name;company;email;phone_number;city;street_name;building_number\n"

# 6. zapisujemy do pliku
with open("spoleczenstwo.csv", "w", encoding="utf-8") as f:
    f.write(kolumny)
    f.writelines(dane_wyjsciowe)
