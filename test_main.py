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
            """SELECT team AS Team, COUNT(*) AS TotalMatchesPlayed,
            SUM(CASE WHEN outcome = 'team1' THEN 1 ELSE 0 END) AS TotalMatchesWon
            FROM (
            SELECT team1 AS team, 'team1' AS outcome
            FROM default.MatchesDB_ONE
            UNION ALL
            SELECT team2 AS team, 'team2' AS outcome
            FROM default.MatchesDB_ONE
            ) AS MatchResults
            JOIN (
            SELECT
            team1 AS team,
            'team1' AS outcome
            FROM default.WWC_MATCHES_2_DB
            UNION ALL
            SELECT team2 AS team, 'team2' AS outcome
            FROM default.WWC_MATCHES_2_DB
            ) AS ActualResults
            ON MatchResults.team = ActualResults.team
            GROUP BY Team
            ORDER BY TotalMatchesPlayed DESC;""",
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
