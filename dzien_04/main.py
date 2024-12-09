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


def nazwa_funkcji():
    # ciałko funkcji
    print("Dzień dobry")
    for i in range(5):
        print(i)
    print("Kończę funkcję")


for licznik in range(4):
    print(licznik)
    nazwa_funkcji()
