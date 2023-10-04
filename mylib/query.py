"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("Goose.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
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
    key_retro,
):
    """create example query"""
    conn = sqlite3.connect("Goose.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO Goose 
        (name,year,team,league,goose_eggs,broken_eggs,mehs,league_average_gpct,ppf,replacement_gpct,gwar,key_retro) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
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
            key_retro,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO Goose VALUES (
            {name},
            {year},
            {team},
            {league},
            {goose_eggs},
            {broken_eggs},
            {mehs},
            {league_average_gpct},
            {ppf},
            {replacement_gpct},
            {gwar},
            {key_retro});"""
    )


def update_record(
    record_id,
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
    key_retro,
):
    """update example query"""
    conn = sqlite3.connect("Goose.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE Goose 
        SET name =?,
        year=?,
        team=?,
        league=?,
        goose_eggs=?,
        broken_eggs=?,
        mehs=?,
        league_average_gpct=?,
        ppf=?,
        replacement_gpct=?,
        gwar=?,
        key_retro=?
        WHERE id=?
        """,
        (
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
            key_retro,
            record_id,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE Goose SET
        name={name},
        year={year},
        team={team},
        league={league},
        goose_eggs={goose_eggs},
        broken_eggs={broken_eggs},
        mehs={mehs},
        league_average_gpct={league_average_gpct},
        ppf={ppf},
        replacement_gpct={replacement_gpct},
        gwar={gwar},
        key_retro={key_retro}
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("Goose.db")
    c = conn.cursor()
    c.execute("DELETE FROM Goose WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM Goose WHERE id={record_id};")


def read_data():
    """read data"""
    conn = sqlite3.connect("Goose.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Goose")
    data = c.fetchall()
    log_query("SELECT * FROM Goose;")
    return data
