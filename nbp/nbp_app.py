from flask import Flask, render_template, redirect
from utils.config import load_config
from utils.db import connect_to_db, disconnect_from_db, make_conn_str, select_from_db

# stałe konfiguracyjne
# CONFIG_FILE = "db_config.yaml"
CONFIG_FILE = "db_config_lukasz.yaml"


app = Flask("aplikacja nbp")

config = load_config(CONFIG_FILE)
db_str = make_conn_str(config)


def kwotowania(waluta="EUR", data_od="2024-12-01", data_do="2024-12-31"):
    sql_query = f"""
    SELECT
        *    
    FROM waluty
    WHERE
        waluta = '{waluta.upper()}'
        AND data >= '{data_od}'
        AND data <= '{data_do}'
    """

    db_conn = connect_to_db(db_str)
    wyniki = select_from_db(db_conn, sql_query)
    disconnect_from_db(db_conn)
    return wyniki

def lista_walut():
    db_conn = connect_to_db(db_str)
    wyniki = select_from_db(db_conn, "SELECT DISTINCT waluta FROM waluty;")
    disconnect_from_db(db_conn)
    return wyniki


@app.route("/kurs/<waluta>/<od>/<do>")
def kurs(waluta, od, do):
    notowania = kwotowania(waluta, od, do)
    waluty = lista_walut()
    # return render_template("kursy.html", notowania=notowania)
    return render_template("kursy_2.html", kursy=notowania, dostepne_waluty=waluty)


@app.route("/")
def hp():
    return redirect("/kurs/eur/2024-01-01/2024-12-31")

if __name__ == "__main__":
    app.run(debug=True)