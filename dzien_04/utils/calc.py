def bmi(wzrost: float | int, waga: float | int) -> float | None:
    """Funkcja wylicza współczynnik BMI na podstawie podanego wzrostu i wagi.
    Jeśli wzrost jest większy niż 3 to zakładamy, że podany jest w cm i przeliczamy to na m.

    Argumenty:
    - wzrost    : wzrost w cm lub m (dokonana będzie odpowiednia konwersja)
    - waga      : waga w kilogramach

    Rezultat:   wyliczony współczynnik BMI lub None jeśli zaistniał jakiś błąd
    """
    if not isinstance(waga, (int, float)):
        return None
    if not isinstance(wzrost, (int, float)): 
        return None
    if wzrost > 3:
        # zakładamy, że wzrost jest w cm -> przeliczamy na metry
        wzrost = wzrost / 100

    wspolczynnik_bmi = waga / wzrost**2
    return wspolczynnik_bmi
