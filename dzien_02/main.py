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
nazwa_pliku = "pan-tadeusz.txt"
poszukiwany_tekst = "Tadeusz"
poszukiwany_tekst = poszukiwany_tekst.lower()

liczba_wystapien = 0
for linia in open(nazwa_pliku, "r", encoding="utf-8"):
    liczba_wystapien_w_linii = linia.lower().count(poszukiwany_tekst)
    liczba_wystapien += liczba_wystapien_w_linii

print(f"W pliku '{nazwa_pliku}' ciąg '{poszukiwany_tekst}' występuje {liczba_wystapien} razy.")

