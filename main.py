import tkinter as tk

root = tk.Tk()
root.title("System Wycieczkowy")
root.geometry("800x600")

label = tk.Label(
    root,
    text="System zarządzania wycieczkami",
    font=("Arial", 16)
)

label.pack(pady=20)

root.mainloop()