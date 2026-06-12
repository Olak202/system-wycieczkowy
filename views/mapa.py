import tkinter as tk
from tkintermapview import TkinterMapView
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "wycieczki.db")

root = tk.Tk()
root.title("Mapa wycieczek")
root.geometry("1000x700")

map_widget = TkinterMapView(root, width=1000, height=700)
map_widget.pack(fill="both", expand=True)

map_widget.set_position(52.069, 19.480)
map_widget.set_zoom(6)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Klienci
cursor.execute("SELECT imie, nazwisko, x, y FROM klienci")
for imie, nazwisko, x, y in cursor.fetchall():
    map_widget.set_marker(
        y,
        x,
        text=f"Klient: {imie} {nazwisko}"
    )

# Biura
cursor.execute("SELECT nazwa, x, y FROM biura")
for nazwa, x, y in cursor.fetchall():
    map_widget.set_marker(
        y,
        x,
        text=f"Biuro: {nazwa}"
    )

# Przewodnicy
cursor.execute("SELECT imie, nazwisko, x, y FROM przewodnicy")
for imie, nazwisko, x, y in cursor.fetchall():
    map_widget.set_marker(
        y,
        x,
        text=f"Przewodnik: {imie} {nazwisko}"
    )

conn.close()

root.mainloop()