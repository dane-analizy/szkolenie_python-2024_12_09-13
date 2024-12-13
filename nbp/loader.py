# załadowanie danych z NBP:

# importy - m.in. z naszego pakietu
from sqlalchemy import text
from utils.config import load_config
from utils.db import connect_to_db, disconnect_from_db, insert_to_db, make_conn_str
from utils.nbp import nbp_rates

# stałe konfiguracyjne
# CONFIG_FILE = "db_config.yaml"
CONFIG_FILE = "db_config_lukasz.yaml"
LISTA_WALUT = ["EUR", "CHF", "GBP", "USD"]
ROK = 2024

# wczytanie konfiguracji związanej z bazą danych
config = load_config(CONFIG_FILE)

# połączenie z bazą
conn_str = make_conn_str(config)
db_conn = connect_to_db(conn_str)

# założenie tabeli jeśli nie istnieje w bazie
db_conn.execute(
    text("""
create table if not exists waluty (
        data varchar(10),
        waluta varchar(3),
        kurs float
);""")
)
# db_conn.commit()

# w pętli odczytanie notowań dzień po dniu, miesiąc po miesiącu i zapisanie ich do bazy
for m in range(1, 13):
    print(f"Miesiąc: {m}")
    for d in range(1, 32):
        notowanie = nbp_rates(
            rok=ROK, miesiac=m, dzien=d, obslugiwane_waluty=LISTA_WALUT
        )

        # # przyjdzie
        # {data:.., eur:.., chf:...}
        # # potrzebne:
        # {
        #     "data": ...
        #     "waluta": ...
        #     "kurs": ...
        # }

        for w in LISTA_WALUT:
            if w not in notowanie.keys():
                continue

            slownik_dla_bazy = {
                "data": notowanie["data"],
                "waluta": w,
                "kurs": notowanie[w],
            }
            insert_to_db(db_conn, "waluty", slownik_dla_bazy)

disconnect_from_db(db_conn)
