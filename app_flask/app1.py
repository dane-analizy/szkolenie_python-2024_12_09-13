# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# pakiet Flask
# pip install Flask

from flask import Flask

app = Flask("nasza aplikacja")


@app.route("/")
def strona_glowna():
    return "jestem stroną główną ale zmieniłem odpowiedź"


@app.route("/kontakt")
def kontakt():
    return "strona z kontaktem"

@app.route("/dodaj/<a>/<b>")
def dodaj(a,b):
    a = float(a)
    b = float(b)
    suma = a + b
    odpowiedz = str(suma)
    return odpowiedz

if __name__ == "__main__":
    app.run()
