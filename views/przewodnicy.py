import tkinter as tk
from tkinter import messagebox
import sqlite3


def dodaj_przewodnika():
    try:
        conn = sqlite3.connect("../database/wycieczki.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO przewodnicy(imie, nazwisko, x, y)
        VALUES (?, ?, ?, ?)
        """, (
            imie_entry.get(),
            nazwisko_entry.get(),
            float(x_entry.get()),
            float(y_entry.get())
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Przewodnik został dodany"
        )

        imie_entry.delete(0, tk.END)
        nazwisko_entry.delete(0, tk.END)
        x_entry.delete(0, tk.END)
        y_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror(
            "Błąd",
            str(e)
        )


def pokaz_przewodnikow():
    conn = sqlite3.connect("../database/wycieczki.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM przewodnicy")

    dane = cursor.fetchall()

    conn.close()

    wynik = ""

    for przewodnik in dane:
        wynik += f"{przewodnik}\n"

    messagebox.showinfo(
        "Lista przewodników",
        wynik if wynik else "Brak przewodników"
    )


def usun_przewodnika():
    try:
        conn = sqlite3.connect("../database/wycieczki.db")
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM przewodnicy WHERE id = ?",
            (int(id_entry.get()),)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukces",
            "Przewodnik został usunięty"
        )

        id_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror(
            "Błąd",
            str(e)
        )


def aktualizuj_przewodnika():
    try:
        conn = sqlite3.connect("../database/wycieczki.db")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE przewodnicy
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
            "Przewodnik został zaktualizowany"
        )

        update_id_entry.delete(0, tk.END)
        nowe_imie_entry.delete(0, tk.END)
        nowe_nazwisko_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror(
            "Błąd",
            str(e)
        )


root = tk.Tk()
root.title("Zarządzanie przewodnikami")
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

tk.Button(
    root,
    text="Dodaj przewodnika",
    command=dodaj_przewodnika
).pack(pady=10)

tk.Button(
    root,
    text="Pokaż przewodników",
    command=pokaz_przewodnikow
).pack(pady=10)

tk.Label(root, text="ID przewodnika do usunięcia").pack(pady=5)

id_entry = tk.Entry(root)
id_entry.pack()

tk.Button(
    root,
    text="Usuń przewodnika",
    command=usun_przewodnika
).pack(pady=10)

tk.Label(root, text="ID przewodnika do aktualizacji").pack(pady=5)

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
    text="Aktualizuj przewodnika",
    command=aktualizuj_przewodnika
).pack(pady=10)

root.mainloop()