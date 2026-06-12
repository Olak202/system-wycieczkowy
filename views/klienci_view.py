import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "wycieczki.db")


def dodaj_klienta():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO klienci(imie, nazwisko, x, y)
        VALUES (?, ?, ?, ?)
        """, (
            imie_entry.get(),
            nazwisko_entry.get(),
            float(x_entry.get()),
            float(y_entry.get())
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Sukces", "Klient został dodany")

        imie_entry.delete(0, tk.END)
        nazwisko_entry.delete(0, tk.END)
        x_entry.delete(0, tk.END)
        y_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


def pokaz_klientow():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM klienci")
    dane = cursor.fetchall()

    conn.close()

    wynik = ""

    for klient in dane:
        wynik += f"{klient}\n"

    messagebox.showinfo(
        "Lista klientów",
        wynik if wynik else "Brak klientów"
    )


def usun_klienta():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM klienci WHERE id = ?",
            (int(id_entry.get()),)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Klient został usunięty"
        )

        id_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


def aktualizuj_klienta():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE klienci
        SET imie = ?, nazwisko = ?
        WHERE id = ?
        """, (
            nowe_imie_entry.get(),
            nowe_nazwisko_entry.get(),
            int(update_id_entry.get())
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Klient został zaktualizowany"
        )

    except Exception as e:
        messagebox.showerror("Błąd", str(e))


root = tk.Tk()
root.title("Zarządzanie klientami")
root.geometry("400x500")

tk.Label(root, text="Imię").pack(pady=5)
imie_entry = tk.Entry(root)
imie_entry.pack()

tk.Label(root, text="Nazwisko").pack(pady=5)
nazwisko_entry = tk.Entry(root)
nazwisko_entry.pack()

tk.Label(root, text="X").pack(pady=5)
x_entry = tk.Entry(root)
x_entry.pack()

tk.Label(root, text="Y").pack(pady=5)
y_entry = tk.Entry(root)
y_entry.pack()

tk.Button(root, text="Dodaj klienta", command=dodaj_klienta).pack(pady=10)
tk.Button(root, text="Pokaż klientów", command=pokaz_klientow).pack(pady=10)

tk.Label(root, text="ID klienta do usunięcia").pack(pady=5)
id_entry = tk.Entry(root)
id_entry.pack()

tk.Button(root, text="Usuń klienta", command=usun_klienta).pack(pady=10)

tk.Label(root, text="ID klienta do aktualizacji").pack(pady=5)
update_id_entry = tk.Entry(root)
update_id_entry.pack()

tk.Label(root, text="Nowe imię").pack(pady=5)
nowe_imie_entry = tk.Entry(root)
nowe_imie_entry.pack()

tk.Label(root, text="Nowe nazwisko").pack(pady=5)
nowe_nazwisko_entry = tk.Entry(root)
nowe_nazwisko_entry.pack()

tk.Button(
    root,
    text="Aktualizuj klienta",
    command=aktualizuj_klienta
).pack(pady=10)

root.mainloop()