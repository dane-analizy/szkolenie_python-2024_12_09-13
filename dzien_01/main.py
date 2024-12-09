# print("Ala ma kota")
# print('Ala ma kota')
# print('Ala "ma" kota') # tu jest komentarz
# print("Ala \"ma kota")

# # for element in lista:
# #     czynność

# # if coś:
# #     rób jedną rzecz
# # else:
# #     rób inną rzecz

# # while coś:
# #     rób te rzeczy


# """
# tu jest komentarz
# na wiele linii
# """

# a = 5
# print(a)
# a = 10
# print(a)

# b = 50
# c = a + b
# print(c)

# c = c + 40
# print(c)

# # typy zmienny
# liczba_calkowita = 123
# liczba_zmiennoprzecinkowa = 456.78
# napis = "abc123def"

# print(liczba_calkowita)
# print(liczba_zmiennoprzecinkowa)
# print(napis)


# # jak sprawdzić typ zmiennej?
# print(type(liczba_calkowita))
# print(type(liczba_zmiennoprzecinkowa))
# print(type(napis))

# wynik = liczba_calkowita + liczba_zmiennoprzecinkowa
# print("wynik działania:", wynik, type(wynik))

# wynik = liczba_calkowita * 5.0
# print("wynik działania:", wynik, type(wynik))

# wynik = liczba_calkowita * 5
# print("wynik działania:", wynik, type(wynik))


# # wynik = liczba_calkowita + napis
# # print("wynik działania:", wynik, type(wynik))

# wynik = liczba_calkowita *  napis
# print("wynik działania:", wynik, type(wynik))

# print("="*80)

# zmienna: int = 123.56
# print(type(zmienna))
# zmienna = "abc"
# print(type(zmienna))

# rzutowanie typów = casting

# zmienna_int = 1234
# print(zmienna_int, type(zmienna_int))

# zmienna_str = str(zmienna_int)
# print(zmienna_str, type(zmienna_str))

# zmienna_float = float(zmienna_int)
# print(zmienna_float, type(zmienna_float))

# zmienna_str = "12345"
# print(zmienna_str, type(zmienna_str))

# zmienna_int = int(zmienna_str)
# print(zmienna_int, type(zmienna_int))

# zmienna_str = "-123.45"
# print(zmienna_str, type(zmienna_str))

# zmienna_float = float(zmienna_str)
# print(zmienna_float, type(zmienna_float))


# pobranie czegoś od użytkownika

# zmienna = input("zapytanie: ")
# print(zmienna, type(zmienna))


#### ZADANIE 1

# Napisz program, który pobierze od użytkownika imię i nazwisko (osobno),
# a potem wypisze w konsoli pozdrowienie "Witaj IMIĘ NAZWISKO!"


# a = "napis"
# b = "inny"
# c = b + a
# print(c)
# print(b, a)

# zmienna_imie = input("Podaj imię: ")
# zmienna_nazwisko = input("Podaj nazwisko: ")
# # print("Witaj", zmienna_imie, zmienna_nazwisko, "!")
# # print("Witaj " + zmienna_imie + " " + zmienna_nazwisko + "!")

# # wstrzykiwanie zmiennych:
# # wersja 1 - python do 3.6
# # print("Witaj {} {}!".format(zmienna_imie, zmienna_nazwisko))

# # wersja 2 - python od 3.7 -> f-string
# print(f"Witaj {zmienna_imie} {zmienna_nazwisko}!")


#### ZADANIE 2

# Napisz program, który pobierze od użytkownika jego imię oraz rok urodzenia.
# Potem wypisze w konsoli pozdrowienie "Witaj IMIĘ" oraz wiek użytkownika.

