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

import yaml
from pathlib import  Path

# importy dla sqlalchemy:
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
# print(config)

# connection string = klucz do połączenia do bazy
db_conn_str = f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_post']}/{config['db_name']}"
# print(db_conn_str)

# budujemy silnik bazodanowy
db_engine = create_engine(db_conn_str)
# print(db_engine)

db_connection = db_engine.connect()
# print(db_connection)

results = db_connection.execute(text("SELECT * FROM players;"))
print(results)

db_connection.close()
