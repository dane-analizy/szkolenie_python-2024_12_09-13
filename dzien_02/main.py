# otwarcie pliku
# tryby - r, w, a, rb, wb, ab

# plik = open("test.txt", "r", encoding="utf-8")
# print(type(plik))

# print(plik)
# plik.close()


# wczytanie zawartości pliku - wszystko na raz do jednej zmienniej

# plik = open("test.txt", "r", encoding="utf-8")
# zawartosc_pliku = plik.read()
# print(zawartosc_pliku)

# print(len(zawartosc_pliku))
# plik.close()

# i = 0
# for znak in zawartosc_pliku:
#     print(f"|{znak}|")
#     i += 1  # i = i + 1
#     if i > 25:
#         break


# wczytanie zawartości pliku linia po linii
# plik = open("test.txt", "r", encoding="utf-8")
# zawartosc_pliku = plik.readlines()
# print(zawartosc_pliku)

# print(len(zawartosc_pliku))
# plik.close()

# for linia in zawartosc_pliku:
#     linia_oczyszczona = linia.rstrip()
#     print(f"|{linia_oczyszczona}|")


# analogicznie:
# for element in open("test.txt", "r", encoding="utf-8"):
#     element_clean = element.strip()
#     print(f"|{element_clean}|")


# for element in open("test.txt", "r", encoding="utf-8").read():
#     element_clean = element.strip()
#     print(f"|{element_clean}|")


# open().read() -> cały plik wczytany na raz do pamięci, do jednej zmiennej
# open().readlines() = open() -> wczytanie linia po linii, do jednej zmiennej która jest listą


# tekst => https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt


#### ZADANIE 11

# Napisz program, który zliczy ilość wystąpień małej lub dużej wersji ciągu podanego przez użytkownika
# w pliku, którego nazwa także podana jest przez użytkownika.

# ciąg_przeszukiwany.count(szukany_ciag)


# rozwiązanie 1 = wczytanie całego pliku na raz
# nazwa_pliku = input("podaj nazwę pliku: ")
# nazwa_pliku = "pan-tadeusz.txt"
# poszukiwany_tekst = "Tadeusz"

# plik = open(nazwa_pliku, "r", encoding="utf-8")
# zawartosc_pliku = plik.read()
# plik.close()
# zawartosc_pliku = zawartosc_pliku.lower()
# poszukiwany_tekst = poszukiwany_tekst.lower()
# liczba_wystapien = zawartosc_pliku.count(poszukiwany_tekst)
# print(f"W pliku {nazwa_pliku} ciąg {poszukiwany_tekst} występuje {liczba_wystapien} razy.")


# rozwiązanie 2 = czytanie linia po linii
# nazwa_pliku = "pan-tadeusz.txt"
# poszukiwany_tekst = "Tadeusz"
# poszukiwany_tekst = poszukiwany_tekst.lower()

# liczba_wystapien = 0
# for linia in open(nazwa_pliku, "r", encoding="utf-8"):
#     liczba_wystapien_w_linii = linia.lower().count(poszukiwany_tekst)
#     liczba_wystapien += liczba_wystapien_w_linii

# print(f"W pliku '{nazwa_pliku}' ciąg '{poszukiwany_tekst}' występuje {liczba_wystapien} razy.")


# ciekawostki o f-stringach

# print(f"{1/3}")
# print(f"{1/3:.2f}")
# print(f"{1/3:%}")
# print(f"{1/3:.1%}")


# napis = "Jasio"
# print(f"|{napis}|")
# print(f"|{napis=}|")
# print(f"|{napis:<40}|")
# print(f"|{napis:>40}|")
# print(f"|{napis:^40}|")


# liczba = 123
# print(f"{liczba:06d}")
# print(f"{liczba:6d}")


# print(f"|{1/3:^50.3%}|")

# from datetime import datetime
# teraz = datetime.now()
# print(type(teraz))
# nazwa = f"{teraz:%Y%m%d_%H%M}.json"
# print(nazwa)


#### ZADANIE 12

# Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika poszukiwaną frazę oraz nazwę pliku.
# W wyniku działania wyszukiwarka powinna pokazać w której linii wystąpiła wyszukiwana fraza
# oraz całą linię. Wyszukiwarka powinna być nieczuła na wielkość liter.


# nazwa_pliku = "pan-tadeusz.txt"
# poszukiwany_tekst = "Tadeusz"
# poszukiwany_tekst = poszukiwany_tekst.lower()

# liczba_wystapien = 0
# numer_linii = 0
# for linia in open(nazwa_pliku, "r", encoding="utf-8"):
#     numer_linii += 1
#     liczba_wystapien_w_linii = linia.lower().count(poszukiwany_tekst)
#     liczba_wystapien += liczba_wystapien_w_linii
#     if liczba_wystapien_w_linii > 0:
#         print(f"{numer_linii:>5}: {linia.strip()}")

# print(f"W pliku '{nazwa_pliku}' ciąg '{poszukiwany_tekst}' występuje {liczba_wystapien} razy.")


# rozwiązanie nieco bardziej pythonowe
# enumerate = numer iteracji w pętli
# nazwa_pliku = "pan-tadeusz.txt"
# poszukiwany_tekst = "Tadeusz"
# poszukiwany_tekst = poszukiwany_tekst.lower()

# liczba_wystapien = 0
# for numer_linii, linia in enumerate(open(nazwa_pliku, "r", encoding="utf-8"), start=1):
#     liczba_wystapien_w_linii = linia.lower().count(poszukiwany_tekst)
#     liczba_wystapien += liczba_wystapien_w_linii
#     if liczba_wystapien_w_linii > 0:
#         print(f"{numer_linii:>5}: {linia.strip()}")

# print(
#     f"W pliku '{nazwa_pliku}' ciąg '{poszukiwany_tekst}' występuje {liczba_wystapien} razy."
# )


# # to:
# iteracja = 0
# for element in range(10):
#     print(iteracja, element)
#     iteracja = iteracja + 1

# # jest równoznaczne z tym:
# for iteracja, element in enumerate(range(10)):
#     print(iteracja, element)



### listy
