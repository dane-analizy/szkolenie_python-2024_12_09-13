# importy -> sqlalchemy


def make_conn_str(config):
    """przygotowanie connection stringa ze słownika z konfiguracją"""
    return "postgresql+psycopg2://...."


def connect_to_db(conn_str):
    """podłączenie do bazy - funkcja z connection stringa podanego jako argument zwraca db_connection"""
    db_engine = create_engine(conn_str)
    db_connection = db_engine.connect()
    return db_connection


def select_from_db(db_conn, sql_query):
    """wykonanie zapytania typu select z bazy: parametr to zapytanie i db_connection, zwraca LISTĘ wyników"""
    res = db_conn.execute(text(sql_query))
    wyniki = res.all()
    return wyniki


def insert_to_db(db_conn, table_name, record):
    """insert słownika do bazy: parametry to db_connection, nazwa tabeli i słownik z danymi"""
    kolumny = ... klucze
    wartosci = ... :klucze... 
    query = f"INSERT INTO {table_name} ({kolumny}) VALUES ({wartosci})"
    res = db_conn.execute(text(query), record)
    res = db_conn.commit()
