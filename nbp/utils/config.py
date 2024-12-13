from pathlib import Path

import yaml


def load_config(nazwa_pliku, enc="utf-8"):
    if not Path(nazwa_pliku).exists():
        print(f"Plik {nazwa_pliku} nie istnieje")
        return {}
    with open(nazwa_pliku, "r", encoding=enc) as p:
        config = yaml.safe_load(p)
        return config
    return {}
