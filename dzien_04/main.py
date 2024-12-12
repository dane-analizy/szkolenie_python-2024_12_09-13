# list-comprehention

# lista = [ wyrazenie(element) for element in kolekcja ]

# dict comprehention

# slownik = { el:el**2 for el in range(10) }
# print(slownik)

# slownik = {"kwadrat_"+str(el): el**2 for el in range(10)}
# print(slownik)


#### ZADANIE 25

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

from itertools import zip_longest, cycle

l1 = [1, 2, 3, 4, 5, 6]
l2 = ["a", "b", "c"]

print("zip_longest():")
for el1, el2 in zip_longest(l1, l2):
    print(el1, el2)

print("zip() + cycle():")
for el1, el2 in zip(l1, cycle(l2)):
    print(el1, el2)

