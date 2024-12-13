from sqlalchemy import create_engine, text


def make_conn_str(config):
    """przygotowanie connection stringa ze słownika z konfiguracją"""

    db_type = config.get("db_type", "postgresql")

    if db_type == "sqlite":
        return f"sqlite:///{config['db_sqlite_file']}"

    if "db_host" not in config.keys():
        print("Brak klucza 'db_host' w konfiguracji")
        return None
    if "db_post" not in config.keys():
        print("Brak klucza 'db_post' w konfiguracji")
        return None
    if "db_user" not in config.keys():
        print("Brak klucza 'db_user' w konfiguracji")
        return None
    if "db_pass" not in config.keys():
        print("Brak klucza 'db_pass' w konfiguracji")
        return None
    if "db_name" not in config.keys():
        print("Brak klucza 'db_name' w konfiguracji")
        return None

    if db_type == "postgresql":
        return f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_post']}/{config['db_name']}"

    if db_type == "oracle":
        return f"oracle+cx_oracle2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_post']}/{config['db_name']}"


def connect_to_db(conn_str):
    """podłączenie do bazy - funkcja z connection stringa podanego jako argument zwraca db_connection"""
    db_engine = create_engine(conn_str)
    db_connection = db_engine.connect()
    return db_connection


def disconnect_from_db(db_conn):
    """zamknięcie połączenia z bazą"""
    db_conn.close()


def select_from_db(db_conn, sql_query):
    """wykonanie zapytania typu select z bazy: parametr to zapytanie i db_connection, zwraca LISTĘ wyników"""
    res = db_conn.execute(text(sql_query))
    # lista nazw kolumn:
    kolumny = list(res.keys())
    # wyniki zrzucone do listy krotek
    res_list = res.all()

    # listę krotek przepisujemy na listę słowników
    wyniki = []
    for record in res_list:
        slownik = {k: r for k, r in zip(kolumny, record)}
        # slownik = dict(zip(kolumny, record))
        wyniki.append(slownik)

    # to samo w wersji list & dict comprehention
    # wyniki = [
    #     {k: r for k, r in zip(kolumny, record)}
    #     for record in res_list
    # ]

    return wyniki


def insert_to_db(db_conn, table_name, record):
    """insert słownika do bazy: parametry to db_connection, nazwa tabeli i słownik z danymi"""
    kolumny = ",".join(record.keys())
    wartosci = ":" + ", :".join(record.keys())

    query = f"INSERT INTO {table_name} ({kolumny}) VALUES ({wartosci})"

    res = db_conn.execute(text(query), record)
    res = db_conn.commit()
