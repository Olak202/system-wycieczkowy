import sqlite3

conn = sqlite3.connect("wycieczki.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS klienci (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    x REAL,
    y REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS biura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT NOT NULL,
    miasto TEXT,
    x REAL,
    y REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS przewodnicy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    x REAL,
    y REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS wycieczki (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT NOT NULL,
    klient_id INTEGER,
    biuro_id INTEGER,
    przewodnik_id INTEGER
)
""")
conn.commit()
conn.close()

print("Baza danych utworzona")