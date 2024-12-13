from flask import Flask, render_template

app = Flask("nasza druga aplikacja")


@app.route("/")
def hp():
    return render_template("hp.html")


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


@app.route("/produkty")
def produkty():
    return render_template("produkty.html")


if __name__ == "__main__":
    app.run()
