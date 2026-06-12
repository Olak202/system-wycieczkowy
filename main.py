import tkinter as tk
import subprocess
import sys


def otworz_klientow():
    subprocess.Popen([sys.executable, "views/klienci_view.py"])


def otworz_biura():
    subprocess.Popen([sys.executable, "views/biura_view.py"])


def otworz_przewodnikow():
    subprocess.Popen([sys.executable, "views/przewodnicy.py"])


def otworz_wycieczki():
    subprocess.Popen([sys.executable, "views/wycieczki.py"])


def otworz_mape():
    subprocess.Popen([sys.executable, "views/mapa.py"])


root = tk.Tk()
root.title("System Wycieczkowy")
root.geometry("400x400")

tk.Label(
    root,
    text="System Zarządzania Wycieczkami",
    font=("Arial", 16)
).pack(pady=20)

tk.Button(
    root,
    text="Klienci",
    command=otworz_klientow
).pack(pady=10)

tk.Button(
    root,
    text="Biura",
    command=otworz_biura
).pack(pady=10)

tk.Button(
    root,
    text="Przewodnicy",
    command=otworz_przewodnikow
).pack(pady=10)

tk.Button(
    root,
    text="Wycieczki",
    command=otworz_wycieczki
).pack(pady=10)

tk.Button(
    root,
    text="Mapa",
    command=otworz_mape
).pack(pady=10)

root.mainloop()