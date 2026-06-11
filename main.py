import tkinter as tk
from tkinter import messagebox


def logowanie():
    login = login_entry.get()
    haslo = haslo_entry.get()

    if login == "admin" and haslo == "admin":
        messagebox.showinfo("Sukces", "Zalogowano pomyślnie")
    else:
        messagebox.showerror("Błąd", "Nieprawidłowy login lub hasło")


root = tk.Tk()
root.title("System Wycieczkowy")
root.geometry("400x300")

tk.Label(root, text="Logowanie", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Login").pack()

login_entry = tk.Entry(root)
login_entry.pack()

tk.Label(root, text="Hasło").pack()

haslo_entry = tk.Entry(root, show="*")
haslo_entry.pack()

tk.Button(
    root,
    text="Zaloguj",
    command=logowanie
).pack(pady=20)

root.mainloop()