"""
Test goes here

"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transfrom_load"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_general_query():
    """tests general_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            """SELECT MatchDate, t1.TeamName AS Team1Name, t2.TeamName AS Team2Name,
                m.Team1Goals, m.Team2Goals, m.Team1Goals + m.Team2Goals AS TotalGoals
            FROM default.matchesdb_one AS m
            JOIN team_names AS t1 ON m.Team1 = t1.TeamID
            JOIN team_names AS t2 ON m.Team2 = t2.TeamID
            UNION ALL
            SELECT MatchDate, t1.TeamName AS Team1Name, t2.TeamName AS Team2Name, 
            m.Team1Goals, m.Team2Goals, m.Team1Goals + m.Team2Goals AS TotalGoals
            FROM default.wwc_matches_2_db AS m
            JOIN team_names AS t1 ON m.Team1 = t1.TeamID
            JOIN team_names AS t2 ON m.Team2 = t2.TeamID
            ORDER BY MatchDate;""",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_general_query()
