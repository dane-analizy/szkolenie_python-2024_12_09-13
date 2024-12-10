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

# lista = [
#     1,
#     2,
#     "a",
#     "ala ma kota",
#     45.6,
#     [9,8,7]
# ]

# print(lista)
# print(type(lista))

# for el in lista:
#     print(el, type(el))


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i, el in enumerate(lista):
#     if i == 5:
#         break
# print(el)

# print(    lista[5]    )
# print(lista[0])

# print(len(lista)) # jest 10 elementów na liście, indeksowanych od 0 do 9 włącznie
# # print(lista[10]) => nie ma elementu o indeksie = 10

# print( lista[3:6] ) # od indeksu 3 włącznie do indeksu 6 wyłącznie
# print(lista[0:6])

# print(lista[:4])

# print(lista[4:   ])

# print( lista[2:8:3])

# print(list(range(2, 8, 3)))


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(lista[len(lista) - 1])

# print(lista[-1])

# print(lista[::-1])


# napis = "ala ma kota" # = ["a", "l", "a", " ", "m", "a", " ", "k", "o", "t", "a"]
# print(napis[:5])
# print(napis[::-1])


#### ZADANIE 13

# Napisz program, który pobierze od użytkownika słowo i sprawdzi czy jest palindromem,
# czyli czy pisane od przodu i od tyłu jest takie samo - np. sos, Anna, sedes, zaraz,
# kajak, zakaz, owocowo, potop, radar.

# slowo = input("podaj jakieś słowo: ").lower().strip()
# palind = slowo[::-1]
# if palind == slowo:
#     print(f"'{slowo}' jest palindromem")
# else:
#     print(f"'{slowo}' nie jest palindromem")


# lista = [] # == lista = list()
# print(lista)

# lista.append(1)
# print(lista)

# lista.append("abc")
# print(lista)

# lista.append(1)
# print(lista)

# lista.append(3)
# print(lista)

# lista.append(4)
# print(lista)

# lista.append("napis")
# print(lista)

# # s = "Ala ma Kota"
# # ss = s.lower()
# # print(s)
# # print(ss)

# lista.remove(1)
# print(lista)

# # lista.remove(1)
# # print(lista)

# lista.pop(2)
# print(lista)


# mutowalność listy - zmieniając jedną listę zmieniamy też inną - obie leżą w tym samym miejscu w pamięci
# l1 = [1,2,3]
# l2 = l1
# print("l1:", l1)
# print("l2:", l2)

# l2[1] = "napis"
# print("l2:", l2)

# print("l1:", l1)

# obejście tego problemu - kopia listy
# l1 = [1,2,3]
# l2 = l1.copy()
# print("l1:", l1)
# print("l2:", l2)

# l2[1] = "napis"
# print("l2:", l2)

# print("l1:", l1)


# lista = [1,2,3]
# lista.insert(1, "napis")
# print(lista)


#### ZADANIE 14

# Napisz program, który pobierze od użytkownika 10 liczb,
# zapamięta je (zapisze na liście), a na koniec wyświetli całą listę pobranych wartości.

# lista = []
# for i in range(10):
#     wartosc = float(input("Podaj liczbę:"))
#     lista.append(wartosc)

# print(lista)


# rozdzielenie ciągu znaków

# napis = "imie;nazwisko;wzrost;waga"
# print(napis)
# print(napis.split(";"))
# print(napis.split("i"))
# print(napis.split("zw"))


#### ZADANIE 15

# Wczytaj plik "zawodnicy.csv" i wyświetl na ekranie kolejne linie i pola z każdej z linii. Napisz co jest
# imieniem, nazwiskiem wzrostem i wagą. Kazdy rekord powinien być ponumerowany od 1.
# Oczekiwany wynik:
# 1 Imie: Tom, Nazwisko: Cruise, Wzrost: 170, Waga: 68
# 2 Imie: Scarlett, Nazwisko: Johansson, Wzrost: 160, Waga: 57
# ...

# 1. otworzyć plik
# 2. przejść linia po linii
# 3. każdą linię rozdzielić na składowe (pamiętaj o strip!)
# 4. rozdzielone elementy wyświetlić na ekranie - pamiętaj o numerowaniu wierzy (enumerate się przyda)


# nazwa_pliku = "zawodnicy.csv"
# sep = ";"

# for nr_linii, linia in enumerate(open(nazwa_pliku, "r", encoding="utf-8"), start=1):
#     rekord = linia.strip().split(sep)
#     print(f"{nr_linii}: Imie: {rekord[0]}, Nazwisko: {rekord[1]}, Wzrost: {rekord[2]}, Waga: {rekord[3]}")


# nazwa_pliku = "zawodnicy.csv"
# sep = ";"

# for nr_linii, linia in enumerate(open(nazwa_pliku, "r", encoding="utf-8"), start=1):
#     rekord = linia.strip().split(sep)
#     print("="*50)
#     print(rekord)

#     rekord_clean = []
#     for r in rekord:
#         rekord_clean.append(r.strip())

#     print(
#         f"{nr_linii}: Imie: {rekord_clean[0]}, Nazwisko: {rekord_clean[1]}, Wzrost: {rekord_clean[2]}, Waga: {rekord_clean[3]}"
#     )


# list comprehention = listy składane

# # coś to jest takie:
# lista = []
# for i in range(20):
#     lista.append(i)
# print(lista)

# # można zapisać krócej:
# lista2 = [i for i in range(20)]
# print(lista2)


# lista = [  i*2 for i in range(10)   ]
# print(lista)

# if i % 2:
#     nieparzysta

# # lista składana:
# lista = [i for i in range(10) if i % 2]
# print(lista)

# # to samo w rozbudowanej formie
# l2 = []
# for i in range(10):
#     if i % 2:
#         wynik = i
#         l2.append(wynik)
# print(l2)


# lista list

#### ZADANIE 16

# Korzystając z list składanych stwórz listę zawierającą elementy same będące listami.
# Każdy taki element ma zawierać numer potęgi (od 1 do 10) oraz wartość tej potęgi dla liczby 2.
# Wyświetl tę listę.

# [
#     [1, 2],
#     [2, 4],
#     [3, 8],
#     ...
# ]

# lista = [[p, 2**p] for p in range(1, 11)]
# print(lista)


#### ZADANIE 17

# Załaduj do postaci listy list zawartość pliku zawodnicy.csv. Użyj list comprehention.

# nazwa_pliku = "zawodnicy.csv"
# sep = ";"

# dane = [linia.strip().split(sep) for linia in open(nazwa_pliku, "r", encoding="utf-8")]
# print(dane)


# dane = [
#     [
#         encja.strip()
#         for encja in linia.strip().split(sep)
#     ]
#     for linia in open(nazwa_pliku, "r", encoding="utf-8")
# ]
# print(dane)


# bmi z pliku


#### ZADANIE 18

# Dla każdego wpisu w pliku zawodnicy.csv wyświetl na konsoli informację o imieniu, nazwisku,
# wadze i wzroście oraz współczynniku BMI.

# bmi = waga [kg] / (wzrost [m] ** 2)

nazwa_pliku = "zawodnicy.csv"
sep = ";"

dane = [linia.strip().split(sep) for linia in open(nazwa_pliku, "r", encoding="utf-8")]
print(dane)


# sortowanie
# z listy stringów do stringa
# zapisywanie do pliku
