# list-comprehention

# lista = [ wyrazenie(element) for element in kolekcja ]

# dict comprehention

# slownik = { el:el**2 for el in range(10) }
# print(slownik)

# slownik = {"kwadrat_"+str(el): el**2 for el in range(10)}
# print(slownik)


#### ZADANIE 26

# Wczytaj konfigurację z pliku konfiguracja.txt.
# Budowa pliku to klucz=wartość w każdej linii.
# Wynikowo kofiguracja powinna być słownikiem.
# Użyj dict-comprehention

# rozwiązanie zgodne z treścią zadania:
# linie = {
#     linia.strip().split("=")[0]: linia.strip().split("=")[1]
#     for linia in open("konfiguracja.txt", "r", encoding="utf-8")
# }
# print(linie)


# rozwiązanie czytelniejsze
# linie = [
#     linia.strip().split("=")
#     for linia in open("konfiguracja.txt", "r", encoding="utf-8")
# ]
# konfiguracja = dict(linie)
# print(konfiguracja)


# zip() - przechodzenie po wielu listach na raz

# l1 = [1, 2, 3, 4]
# l2 = ["a", "b", "c", "d"]

# for i, el1 in enumerate(l1):
#     print(el1, l2[i])

# można krócej:

# for el1, el2 in zip(l1, l2):
#     print(el1, el2)


# co z długością list? - brana jest długość najkrótszej listy
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ["a", "b", "c", "d"]

# for el1, el2 in zip(l1, l2):
#     print(el1, el2)

# from itertools import zip_longest, cycle

# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ["a", "b", "c"]

# print("zip_longest():")
# for el1, el2 in zip_longest(l1, l2):
#     print(el1, el2)

# print("zip() + cycle():")
# for el1, el2 in zip(l1, cycle(l2)):
#     print(el1, el2)


# Zadanie 25 rozwiązanie z użyciem gotowych elementów z Pythona
# from collections import Counter

# tekst = open("pan-tadeusz.txt", "r", encoding="utf-8").read()
# tekst = tekst.lower()

# biale_znaki = ',.?!-:;…—*()%-+"«»/'
# for bz in biale_znaki:
#     tekst = tekst.replace(bz, " ")

# wszystkie_slowa = tekst.split()

# zliczenie = Counter(wszystkie_slowa)
# zliczenie = dict(sorted(zliczenie.items(), key=lambda kv:kv[1], reverse=True))

# # słowa występujące nie więcej niż 100 razy
# for k,v in zliczenie.items():
#     print(k,v)
#     if v < 100:
#         break


# wyjątki

# try:
#     spróbuj coś zrobić
# except:
#     zrób to, jesli nie udało się tego wyżej

# liczba = 0
# wynik = 1/liczba
# print(wynik)


# liczba = 0
# try:
#     print("spróbuję podzielić")
#     wynik = 1 / liczba
#     print("podzieliłem")
#     print("wynik:", wynik)
# except:
#     print("błąd")

# print("program idzie dalej")


# d = {}
# liczba = 0
# try:
#     # print(zmienna) # NameError
#     # print(d["zmiena"]) # KeyError
#     print(1 + "auagu") # TypeError
#     print("spróbuję podzielić")
#     wynik = 1 / liczba # ZeroDivisionError
#     print("podzieliłem")
#     print("wynik:", wynik)
# except NameError:
#     print("wystąpił błąd NameError")
# except TypeError:
#     print("wystąpił Type error")
# except ZeroDivisionError:
#     print("nie dziel przez zero")
# except Exception as e:
#     print("błąd", e, type(e))

# print("program idzie dalej")

# try:
#     raise ZeroDivisionError
# except Exception as blad:
#     print(blad, type(blad))

# raise TypeError


#### ZADANIE 27

# Wyświetl wynik dzielenia jedynki przez kolejne liczby z zakresu od -10 do 10.
# Jeżeli zajdzie jakiś błąd - napisz na konsoli co to za błąd i działaj dalej.

# for i in range(-10, 10):
#     try:
#         wynik = 1 / i
#         print(wynik)
#     except Exception as e:
#         print("BLAD : ", type(e))


# funkcje => DRY = Don't Repeat Yourself

# funkcje bez parametrów:
# def nazwa_funkcji():
#     # ciałko funkcji
#     print("Dzień dobry")
#     for i in range(5):
#         print(i)
#     print("Kończę funkcję")
# użycie funkcji
# for licznik in range(4):
#     print(licznik)
#     nazwa_funkcji()


# funkcje z parametrami
# def dodawanie(a, b):
#     wynik = a + b
#     print(f"{a} + {b} = {wynik}")


# dodawanie(10, 5)
# dodawanie(50, 100)


# funkcje z parametrami i zwracające wartość
# def mnozenie(a: float | int, b: float | int) -> float:
#     wynik = a * b
#     print(f"{a} * {b} = {wynik}")
#     return float(wynik)


# print("wywołuję funkcję:")
# wynik_z_funkcji = mnozenie(4,6)
# print("funkcja wykonana")
# print(f"funkcja zwróciła wartość {wynik_z_funkcji}")

# wynik_dodawania = dodawanie(1, 2)
# wynik_mnozenia = mnozenie(5, 3)

# print("wynik_dodawania:", wynik_dodawania)
# print("wynik_mnozenia:", wynik_mnozenia)


# mnozenie([1, 2, 3], [6, 7, 8])

# zasięg zmiennych
# a = 10
# def

# def mnozenie(a: float | int, b: float | int) -> float | None:
#     if not isinstance(a, (int, float)):
#         print(f"a ({a}) musi być float")
#         return None

#     if not isinstance(b, (int, float)):
#         print(f"b ({b}) musi być float")
#         return None

#     wynik = a * b
#     print(f"{a} * {b} = {wynik}")
#     return float(wynik)

# mnozenie( [1,2,3] , 67.7)
# mnozenie(1, 34.56)


#### ZADANIE 28

# Przygotuj funkcję, która wyliczy na podstawie wagi i wzrostu (parametry) BMI z dokładnością
# do 2 miejsc po przecinku.
# W przypadku pojawienia się wyjątku - wypisze na konsoli błąd i zwróci wartość -1

# bmi = waga / wzrost^2


# def bmi_calc(masa, wzrost):
#     try:
#         bmi = float(masa) / float(wzrost / 100) ** 2
#         print(f"Twoje BMI to: {bmi:.2f}")
#         return bmi
#     except Exception as e:
#         print("wystąpił błąd:", e)
#         return -1


# bmi_calc(70, 167)

# po co to wszytko?


# try:
#     ...
# except Exception as blad:
#     print("błąd:", blad)
#     return -1


# for osoba in lista:

#     wskaznik_bmi = bmi(osoba['wzrost'], osoba['waga'])
#     if wskaznik_bmi == -1:
#         zapis_do_pliku_z_bledami(osoba)
#         continue

#     zapis_do_pliku_konkretnej_osoby(osoba, wskaznik_bmi)


# zasięg zmiennych
# def foo(a, b):
#     print(f"w ciele funkcji: {a=}, {b=}, {c=}")

# a = 0
# b = 0
# c = 3
# print(f"przed wywołaniem funkcji: {a=}, {b=}, {c=}")
# foo(1, 2)
# print(f"po wywołaniu funkcji: {a=}, {b=}, {c=}")


# def foo(a, b):
#     c = a+b
#     print(f"w ciele funkcji: {a=}, {b=}, {c=}")

# a = 0
# b = 0
# c = 0
# print(f"przed wywołaniem funkcji: {a=}, {b=}, {c=}")
# foo(1, 2)
# print(f"po wywołaniu funkcji: {a=}, {b=}, {c=}")


# nadpisanie zmiennej globalnej
# def foo(a, b):
#     global c
#     c = 5
#     print(f"w ciele funkcji: {a=}, {b=}, {c=}")

# a = 0
# b = 0
# c = 1000
# print(f"przed wywołaniem funkcji: {a=}, {b=}, {c=}")
# foo(1, 2)
# print(f"po wywołaniu funkcji: {a=}, {b=}, {c=}")


# argumenty domyślne


# def funkcja(a=1, b=2, c=3):
#     suma = a + b + c
#     print(f"{a=} + {b=} + {c=} = {suma}")


# funkcja(10, 20, 5)
# funkcja(b=10)
# # a, b, c
# funkcja(b=10, c=45, a=50)
# funkcja(5, c=1000)


# dowolna liczba argumentów pozycyjnych
# def fun(*args):
#     print(args)
#     for a in args:
#         print(a)
#     print("koniec\n")
        
# fun(1)
# fun(1,2,3)
# fun([1,23,4,5,7])

# dowolna liczba argumentów nazwanych
# def fun(**kwargs):
#     print(kwargs)
#     for k,v in kwargs.items():
#         print(k, v)
    
#     if "a" in kwargs.keys():
#         print(f"Robię czynność zależą od a {kwargs['a']=}")
#     print("koniec\n")


# fun(b=123, c="aequg", d={"o": 5})

# def rysuj(dane, *args, **kwargs):
#     if kwargs['typ'] == 'linia':
#         rysuj_wykres_liniowy(dane)

        
# moduły = zbiory funkcji -> zobacz plik obliczenia.py

# # import całego modułu
# import obliczenia

# a = 10
# b = 20

# suma = obliczenia.dodawanie(a,b)
# roznica = obliczenia.odejmowanie(a, b)
# iloczyn = obliczenia.mnozenie(a,b)
# iloraz = obliczenia.dzielenie(a, b)

# print(f"{suma=}")
# print(f"{roznica=}")
# print(f"{iloczyn=}")
# print(f"{iloraz=}")


# # # import pojedynczych funkcji
# from obliczenia import dodawanie, odejmowanie
# from klasa import Auto
# import pusty_modul

# # print(pusty_modul.imie)
# # print(pusty_modul.wynik)


# a = 10
# b = 20

# suma = dodawanie(a,b)
# roznica = odejmowanie(a, b)
# # iloczyn = mnozenie(a,b)
# # iloraz = dzielenie(a, b)

# print(f"{suma=}")
# print(f"{roznica=}")
# # print(f"{iloczyn=}")
# # print(f"{iloraz=}")

# a = Auto()
# a.kolor = "beżowy"
# a.opis()



# import testowy
# print("plik main.py", __name__)

# if __name__ == "__main__":
#     print("Uruchomiłeś skrypt main.py")



# pakiet = zbiór modułów
# import pakiet.calc
# from pakiet import db

# pakiet.calc.dodawanie(1,3)
# db.open_db()


#### ZADANIE 29

# Zbuduj pakiet utils, w którym znajdzie się moduł calc. W module calc przygotuj funkcję bmi() wyliczającą
# ten współczynnik z podanych parametrów.


# from utils.calc import bmi

# w = bmi(180, 80)
# print(w)



# kod który wykorzystuje napisane pakietty/moduły:
# from utils.file import load_data, clean_data

# zaladowane_dane = load_data("zawodnicy.csv")
# gotowe_dane = clean_data(zaladowane_dane)
# print(gotowe_dane)

#### ZADANIE 30

# Uzupełnij moduł utils.file o funkcję zapisującą dane do pliku JSON. Dane pochodzą z wyniku działania funkcji clean_data().

# funkcja 1:
# osoby = [
#     {
#         "imie": "Tom",
#         "nazwisko": "Cruise",
#         "wzrost": 170.0,
#         "waga":68.0,
#         "bmi": 23.529
#     },
#     {},
#     {}
# ]

# funkcja 2:
# json.dump(osoby, plik)