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
