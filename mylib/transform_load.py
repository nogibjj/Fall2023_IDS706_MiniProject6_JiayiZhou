"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/Goose.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("Goose.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Goose")
    c.execute(
        """
        CREATE TABLE Goose (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            year INTEGER,
            team TEXT,
            league TEXT,
            goose_eggs INTEGER,
            broken_eggs INTEGER,
            mehs INTEGER,
            league_average_gpct REAL,
            ppf REAL,
            replacement_gpct REAL,
            gwar REAL,
            key_retro TEXT
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO Goose (
            name,
            year,
            team,
            league,
            goose_eggs,
            broken_eggs,
            mehs,
            league_average_gpct,
            ppf,
            replacement_gpct,
            gwar,
            key_retro
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "Goose.db"
