from flask import Flask, render_template

app = Flask("nasza druga aplikacja", template_folder="templatki2")


@app.route("/dodaj/<a>/<b>")
def dodaj(a, b):
    wynik = float(a) + float(b)
    return render_template("dodaj.html", liczba_a=a, liczba_b=b, suma=wynik)


@app.route("/odejmij/<a>/<b>")
def odejmij(a, b):
    dane_do_template = {
        "wynik": float(a) - float(b),
        "liczba_a": float(a),
        "liczba_b": float(b),
    }

    return render_template("odjemij.html", dane=dane_do_template)


@app.route("/lista")
def lista():
    dane = ["abc", 1, "cde", 23.56, "napis"]
    return render_template("lista.html", rekordy=dane)


if __name__ == "__main__":
    app.run(debug=True)
