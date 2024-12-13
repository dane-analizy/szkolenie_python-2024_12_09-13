import requests


def nbp_rates(rok=2024, miesiac=9, dzien=1, obslugiwane_waluty=["EUR", "CHF", "USD"]):
    wyniki = {"data": f"{rok}-{miesiac:02}-{dzien:02}"}

    url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok}-{miesiac:02}-{dzien:02}?format=json"
    res = requests.get(url)

    if res.status_code != 200:
        print(f"Błąd: {res.status_code}")
        return wyniki

    dane = res.json()[0]

    # print(wyniki)
    kwotowania = dane["rates"]
    for waluta in kwotowania:
        if waluta["code"].upper() in obslugiwane_waluty:
            # print(f"{waluta['currency']} => {waluta['mid']}")
            klucz = waluta["code"].upper()
            wyniki[klucz] = waluta["mid"]
            # print(wyniki)

    return wyniki
