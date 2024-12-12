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

conn_str = f"postgres://{db_user}:{db_pass}@{db_host}:{db_post}/{db_name}"
