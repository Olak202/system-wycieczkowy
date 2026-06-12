import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "wycieczki.db")


def dodaj_biuro():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO biura(nazwa, miasto, x, y)
        VALUES (?, ?, ?, ?)
        """, (
            nazwa_entry.get(),
            miasto_entry.get(),
            float(x_entry.get()),
            float(y_entry.get())
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Biuro zostało dodane"
        )

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


def pokaz_biura():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM biura")
    dane = cursor.fetchall()

    conn.close()

    wynik = ""

    for biuro in dane:
        wynik += f"{biuro}\n"

    messagebox.showinfo(
        "Lista biur",
        wynik if wynik else "Brak biur"
    )


def usun_biuro():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM biura WHERE id = ?",
            (int(id_entry.get()),)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Biuro usunięte"
        )

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


def aktualizuj_biuro():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE biura
        SET nazwa = ?, miasto = ?
        WHERE id = ?
        """, (
            nowa_nazwa_entry.get(),
            nowe_miasto_entry.get(),
            int(update_id_entry.get())
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Biuro zaktualizowane"
        )

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


root = tk.Tk()
root.title("Zarządzanie biurami")
root.geometry("450x600")

tk.Label(root, text="Nazwa biura").pack()
nazwa_entry = tk.Entry(root)
nazwa_entry.pack()

tk.Label(root, text="Miasto").pack()
miasto_entry = tk.Entry(root)
miasto_entry.pack()

tk.Label(root, text="X").pack()
x_entry = tk.Entry(root)
x_entry.pack()

tk.Label(root, text="Y").pack()
y_entry = tk.Entry(root)
y_entry.pack()

tk.Button(root, text="Dodaj biuro", command=dodaj_biuro).pack(pady=10)
tk.Button(root, text="Pokaż biura", command=pokaz_biura).pack(pady=10)

tk.Label(root, text="ID biura do usunięcia").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Button(root, text="Usuń biuro", command=usun_biuro).pack(pady=10)

tk.Label(root, text="ID biura do aktualizacji").pack()
update_id_entry = tk.Entry(root)
update_id_entry.pack()

tk.Label(root, text="Nowa nazwa").pack()
nowa_nazwa_entry = tk.Entry(root)
nowa_nazwa_entry.pack()

tk.Label(root, text="Nowe miasto").pack()
nowe_miasto_entry = tk.Entry(root)
nowe_miasto_entry.pack()

tk.Button(
    root,
    text="Aktualizuj biuro",
    command=aktualizuj_biuro
).pack(pady=10)

root.mainloop()