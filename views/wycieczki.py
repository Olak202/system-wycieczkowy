import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "wycieczki.db")


def dodaj_wycieczke():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO wycieczki(
            nazwa,
            klient_id,
            biuro_id,
            przewodnik_id
        )
        VALUES (?, ?, ?, ?)
        """, (
            nazwa_entry.get(),
            int(klient_id_entry.get()),
            int(biuro_id_entry.get()),
            int(przewodnik_id_entry.get())
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Sukces", "Wycieczka została dodana")

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


def pokaz_wycieczki():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM wycieczki")
    dane = cursor.fetchall()

    conn.close()

    wynik = ""

    for wycieczka in dane:
        wynik += f"{wycieczka}\n"

    messagebox.showinfo(
        "Lista wycieczek",
        wynik if wynik else "Brak wycieczek"
    )


def usun_wycieczke():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM wycieczki WHERE id = ?",
            (int(id_entry.get()),)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Wycieczka została usunięta"
        )

        id_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


def aktualizuj_wycieczke():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE wycieczki
        SET nazwa = ?
        WHERE id = ?
        """, (
            nowa_nazwa_entry.get(),
            int(update_id_entry.get())
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Wycieczka została zaktualizowana"
        )

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


root = tk.Tk()
root.title("Zarządzanie wycieczkami")
root.geometry("400x550")

tk.Label(root, text="Nazwa wycieczki").pack(pady=5)
nazwa_entry = tk.Entry(root)
nazwa_entry.pack()

tk.Label(root, text="ID klienta").pack(pady=5)
klient_id_entry = tk.Entry(root)
klient_id_entry.pack()

tk.Label(root, text="ID biura").pack(pady=5)
biuro_id_entry = tk.Entry(root)
biuro_id_entry.pack()

tk.Label(root, text="ID przewodnika").pack(pady=5)
przewodnik_id_entry = tk.Entry(root)
przewodnik_id_entry.pack()

tk.Button(
    root,
    text="Dodaj wycieczkę",
    command=dodaj_wycieczke
).pack(pady=10)

tk.Button(
    root,
    text="Pokaż wycieczki",
    command=pokaz_wycieczki
).pack(pady=10)

tk.Label(root, text="ID wycieczki do usunięcia").pack(pady=5)
id_entry = tk.Entry(root)
id_entry.pack()

tk.Button(
    root,
    text="Usuń wycieczkę",
    command=usun_wycieczke
).pack(pady=10)

tk.Label(root, text="ID wycieczki do aktualizacji").pack(pady=5)
update_id_entry = tk.Entry(root)
update_id_entry.pack()

tk.Label(root, text="Nowa nazwa wycieczki").pack(pady=5)
nowa_nazwa_entry = tk.Entry(root)
nowa_nazwa_entry.pack()

tk.Button(
    root,
    text="Aktualizuj wycieczkę",
    command=aktualizuj_wycieczke
).pack(pady=10)

root.mainloop()