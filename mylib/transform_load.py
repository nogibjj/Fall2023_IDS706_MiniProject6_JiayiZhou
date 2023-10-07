"""
Transforms and Loads data into the Azure Databricks database
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/wwc_matches_1.csv", dataset2="data/wwc_matches_2.csv"):
    """Transforms and Loads data into the Azure Databricks database"""
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'wwc_matches_1*'")
        result = c.fetchall()
        # c.execute("DROP TABLE IF EXISTS MatchesDB_ONE")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS MatchesDB_ONE (
                    id int,
                    date string,
                    group string,
                    team1 string,
                    team2 string,
                    team1_win real,
                    team2_win real,
                    tie real
                )
            """
            )
            # insert
            for _, row in df.iterrows():
                convert = (_,) + tuple(row)
                print(convert)
                c.execute(f"INSERT INTO MatchesDB_ONE VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'wwc_matches_2*'")
        result = c.fetchall()
        # c.execute("DROP TABLE IF EXISTS WWC_MATCHES_2_DB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS WWC_MATCHES_2_DB (
                    id int,
                    date string,
                    group string,
                    team1 string,
                    team2 string,
                    team1_win real,
                    team2_win real,
                    tie real
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO WWC_MATCHES_2_DB VALUES {convert}")
        c.close()

    return "success"
