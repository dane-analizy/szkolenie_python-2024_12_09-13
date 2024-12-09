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

# BIEZACY_ROK = 2024

# imie = input("Podaj swoje imię: ")
# rok_urodzenia = input("W którym roku się urodziłeś? ")
# wiek = BIEZACY_ROK - int(rok_urodzenia)
# print(f"Witaj {imie}, widzę że masz {wiek} lat")


# definicja BMI: https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a

# bmi = masa w kg / (wzrost w m)^2

# potęgowanie w Pythonie:
# x^y => x**y
# bmi = masa / wzrost**2

#### ZADANIE 3

# Napisz program, który pobierze od użytkownika masę i wzrost,
# a następnie policzy BMI i wypisze wynik na konsolę.
# Uwaga - przy pobieraniu danych napisz w jakich jednostkach mają być podane.


# weigth = input("Podaj Twoja mase [kg]: ")
# height = input("Podaj Twoj wzrost [cm]: ")

# bmi = float(weigth) / (float(height) / 100) ** 2

# print(f"Twoje BMI to: {bmi}")

# bmi_round = round(bmi, 2)
# print(f"Twoje BMI to: {bmi_round}")

# print(f"Twoje BMI to: {bmi:.3f}")


# instrukcje warunkowe

# jeżeli warunek jest prawdziwy
#     to wykonaj te czynności
# inaczej
#     wykonaj inne czynności

# zmienna = -10

# if zmienna > 0:
#     print(f"zmienna ma wartość {zmienna} i jest > 0")
#     # egeg
#     # gegeg
# else:
#     print("zmienna jest mniejsza niż 0")
#     # inna instrukcja
#     # jeszcze inna

# print("Po ifie")


# print(10 % 3) # reszta z dzielenia 10 przez 3
# print(10 // 3) # ile razy całkowicie mieści się 3 w 10

# liczba = 14
# if liczba % 2 == 0:
#     print(f"{liczba=} jest parzysta")
# else:
#     print(f"{liczba} nie jest parzysta")

# if w ifie
# liczba = 13
# if liczba > 0:
#     if liczba % 2 == 0:
#         print(f"{liczba=} jest parzysta i dodatnia")
#         # fafaf
#         # afagag
#         # agagag
#     else:
#         print(f"{liczba} nie jest parzysta i dodatnia")
#     print("Skończyłem operacje z dodatnią liczbą")
# else:
#     pass  # pass nic nie robi

# print("Koniec programu")


# konstrukcja elif

# liczba = 14
# if liczba % 3 == 0:
#     print(f"{liczba=} przy dzieleniu przez 3 nie zwraca reszty")
# elif liczba % 3 == 1:
#     print(f"{liczba=} przy dzieleniu przez 3 zwraca 1 reszty")
# elif liczba % 3 == 2:
#     print(f"{liczba=} przy dzieleniu przez 3 zwraca 2 reszty")
# else:
#     print("to jest zupełnie coś innego")


#### ZADANIE 4

# Napisz program, który pobierze od użytkownika masę i wzrost, a następnie policzy BMI i wypisze na konsolę.
# Dodatkowo - na podstawie wartości obliczonego BMI niech poda komentarz.
# < 16 => wygłodzenie
# 16 - 16.999 => wychudzenie
# 17 - 18,49 => niedowaga
# 18,5 - 24,999 => pożądana masa ciała
# 25 - 29,999 => nadwaga
# 30 - 34,999 => otyłość I stopnia
# 35 - 39,999 => otyłość II stopnia (duża)
# > 40 => otyłość III stopnia (chorobliwa)


# weigth = input("Podaj Twoja mase [kg]: ")
# height = input("Podaj Twoj wzrost [cm]: ")
# bmi = float(weigth) / (float(height) / 100) ** 2
# print(f"Twoje BMI to: {bmi}")


# if bmi < 16:
#     print(f"{bmi=:.2f} oznacza  wygłodzenie")
# elif bmi <= 17:
#     print(f"{bmi=:.2f} oznacza  wychudzenie")
# elif bmi <= 18.5:
#     print(f"{bmi=:.2f} oznacza  niedowaga")
# elif bmi <= 25:
#     print(f"{bmi=:.2f} oznacza  pożądana masa ciała")
# elif bmi <= 30:
#     print(f"{bmi=:.2f} oznacza  nadwaga")
# elif  bmi <= 35:
#     print(f"{bmi=:.2f} oznacza  otyłość I stopnia")
# elif bmi <= 40:
#     print(f"{bmi=:.2f} oznacza  otyłość II stopnia (duża)")
# else:
#     print(f"{bmi=:.2f} oznacza  otyłość III stopnia (chorobliwa)")


# if bmi > 12 and bmi < 40:
#     # efuwrgh


# True and True => True
# False and True => False

# True or False => True
# False or True => True


# pętle


# range() => zwraca kolejne liczby całkowite
# range(start=0, stop=10, step=1)

# for liczba in range(0, 10, 1):
#     print(liczba)

# for liczba in range(10):
#     print(liczba)


# for liczba in range(5, 10):
#     print(liczba)


# for liczba in range(5, 20, 3):
#     print(liczba)


#### ZADANIE 5

# Wyświetl 20 kolejnych potęg liczby 2.

# for liczba in range(20): # zaczynamy od 0, kończymy na 19 włącznie
#     potega = 2**liczba
#     print(f"2 ^ {liczba} = {potega}")

# iterable


# for w forze

# for x in range(1, 11):
#     for y in range(1, 11):
#         print(f"{x=} x {y=} = {x*y}")

#### ZADANIE 6

# Z tabliczki mnożenia 1..10 x 1..10 wyświetl tylko te wartości, które są mniejsze niż 69.

# for x in range(1, 11):
#     for y in range(1, 11):
#         wynik = x*y
#         if wynik < 69:
#             print(f"{x=} x {y=} = {wynik}")


# uwaga na wcięcia

# for x in range(1, 11):
#     if x % 2 == 0:
#         for y in range(1, 11):
#             wynik = x * y
#             if wynik < 69:
#                 print(f"{x=} x {y=} = {wynik}")


# inna logika

# for x in range(1, 11):
#     if x % 2 == 0:
#         for y in range(1, 11):
#             wynik = x * y
# if wynik < 69:
#     print(f"{x=} x {y=} = {wynik}")


# # przypisanie wielu zmiennych na raz
# a, b, c = 1, 2, 3

# # zamiana wartości zmiennych
# a = 1
# b = 2

# #  "tradycyjnie:"
# t = a
# a = b
# b = t

# # pythonowo:
# a, b = b, a


# # wynik
# a = 2
# b = 1



#### ZADANIE 7

# Napisz symulator lokaty Symulator ma przyjmować zmienne:
# - początkowa kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakładamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone po doliczeniu odsetek. 
# Zakładamy kapitalizację odsetek co miesiąc.