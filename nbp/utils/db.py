# przygotowanie connection stringa ze słownika z konfiguracją
return f"...."


# podłączenie do bazy - funkcja z connection stringa podanego jako argument zwraca db_connection
db_engine = create_engine(....)
db_connection = db_engine.connect()
return db_connection


# wykonanie zapytania typu select z bazy: parametr to zapytanie i db_connection, zwraca LISTĘ wyników
res = db_connection.execute(text(...))
wyniki = res.all()
return wyniki


# insert słownika do bazy: parametry to db_connection, nazwa tabeli i słownik z danymi
query = "INSERT INTO ... VALUES (...)"
res = db_connection.execute(text(query), slownik)
res = db_connection.commit()

