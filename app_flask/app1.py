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

if __name__ == "__main__":
    app.run()
