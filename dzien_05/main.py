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

# conn_str = f"postgres+psycopg2://{db_user}:{db_pass}@{db_host}:{db_post}/{db_name}"

#### ZADANIE 32

# Napisz funkcję load_config(), która z podanego jako argument pliku YAML wczyta jego zawartość
# i zwróci w postaci słownika.

import yaml
from pathlib import  Path

def load_config(nazwa_pliku, enc="utf-8"):
    if not Path(nazwa_pliku).exists():
        print(f"Plik {nazwa_pliku} nie istnieje")
        return {}
    with open(nazwa_pliku, "r", encoding=enc) as p:
        config = yaml.safe_load(p)
        return config
    return {}

dbc = load_config("db_config.yaml")
print(dbc)