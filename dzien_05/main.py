# DBeaver -> https://dbeaver.io/

# połączenie z bazą danych
# pakiet sqlalchemy
# pip install SQLAchemy
#
# - pakiety:
# 	- pakiet do łączenia się z PostgreSQL
# 		- pip install psycopg2
# 	- pakiet do łączenia się z Oracle
# 		- pip install cx_oracle
# 	- pakiet do łączenia się z MS SQL
# 		- pip install pymssql

# connection string - adres do bazy danych

# conn_str = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_post}/{db_name}"

#### ZADANIE 32

# Napisz funkcję load_config(), która z podanego jako argument pliku YAML wczyta jego zawartość
# i zwróci w postaci słownika.

# from pathlib import Path

# # zainstaluj potrzebne pakiety:
# # pip install PyYAML SQLAlchemy psycopg2
# import yaml

# # importy dla sqlalchemy:
# from sqlalchemy import create_engine, text

# # CONFIG_FILE = "db_config.yaml"
# CONFIG_FILE = "db_config_lukasz.yaml"


# def load_config(nazwa_pliku, enc="utf-8"):
#     if not Path(nazwa_pliku).exists():
#         print(f"Plik {nazwa_pliku} nie istnieje")
#         return {}
#     with open(nazwa_pliku, "r", encoding=enc) as p:
#         config = yaml.safe_load(p)
#         return config
#     return {}


# config = load_config(CONFIG_FILE)
# # print(config)

# # connection string = klucz do połączenia do bazy
# db_conn_str = f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_post']}/{config['db_name']}"
# # print(db_conn_str)

# # budujemy silnik bazodanowy
# db_engine = create_engine(db_conn_str)
# # print(db_engine)

# db_connection = db_engine.connect()
# # print(db_connection)

# # wykonujemy zapytanie SQLowe:
# results = db_connection.execute(text("SELECT * FROM players "))

# # lista nazw kolumn:
# kolumny = list(results.keys())
# # print(kolumny)

# # wynikiem jest kursor
# # print(results)

# # zapisanie rezultatów do listy
# # results_list = results.all()

# # wyświetlamy kolejne rekordy z kursora
# # for i, r in enumerate(results):
# #     print(f"Rekord {i}:")
# #     print(r, end="\n\n")

# for record in results:
#     slownik = {k: r for k, r in zip(kolumny, record)}
#     print(slownik)


# # rozłączenie od bazy
# db_connection.close()




# wstawianie danych do bazy

from pathlib import Path
import yaml
from sqlalchemy import create_engine, text

# CONFIG_FILE = "db_config.yaml"
CONFIG_FILE = "db_config_lukasz.yaml"

def load_config(nazwa_pliku, enc="utf-8"):
    if not Path(nazwa_pliku).exists():
        print(f"Plik {nazwa_pliku} nie istnieje")
        return {}
    with open(nazwa_pliku, "r", encoding=enc) as p:
        config = yaml.safe_load(p)
        return config
    return {}


config = load_config(CONFIG_FILE)
db_conn_str = f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_post']}/{config['db_name']}"
db_engine = create_engine(db_conn_str)
db_connection = db_engine.connect()

# zapytanie do bazy
sql_query = """
INSERT INTO players (first_name,last_name,height,weight)
VALUES ('Zosia','Samosia', 182, 78);
"""

# wykonujemy zapytanie SQLowe:
results = db_connection.execute(text(sql_query))
print(results)
results = db_connection.commit()
print(results)


# rozłączenie od bazy
db_connection.close()
