```sql
SELECT team AS Team, COUNT(*) AS TotalMatchesPlayed FROM (SELECT team1 AS team FROM default.matchesdb_one UNION ALL SELECT team2 AS team FROM default.matchesdb_one UNION ALL SELECT team1 AS team FROM default.wwc_matches_2_db UNION ALL SELECT team2 AS team FROM default.wwc_matches_2_db) AS AllTeams GROUP BY Team ORDER BY TotalMatchesPlayed DESC;
```

```response from databricks
[Row(Team='Switzerland', TotalMatchesPlayed=6), Row(Team='Germany', TotalMatchesPlayed=6), Row(Team='Costa Rica', TotalMatchesPlayed=6), Row(Team='Brazil', TotalMatchesPlayed=6), Row(Team='Australia', TotalMatchesPlayed=6), Row(Team='Mexico', TotalMatchesPlayed=6), Row(Team='France', TotalMatchesPlayed=6), Row(Team='USA', TotalMatchesPlayed=6), Row(Team='Ivory Coast', TotalMatchesPlayed=6), Row(Team='Ecuador', TotalMatchesPlayed=6), Row(Team='South Korea', TotalMatchesPlayed=6), Row(Team='New Zealand', TotalMatchesPlayed=6), Row(Team='Sweden', TotalMatchesPlayed=6), Row(Team='Colombia', TotalMatchesPlayed=6), Row(Team='England', TotalMatchesPlayed=6), Row(Team='Norway', TotalMatchesPlayed=6), Row(Team='Netherlands', TotalMatchesPlayed=6), Row(Team='Thailand', TotalMatchesPlayed=6), Row(Team='Nigeria', TotalMatchesPlayed=6), Row(Team='Spain', TotalMatchesPlayed=6), Row(Team='Japan', TotalMatchesPlayed=6), Row(Team='Cameroon', TotalMatchesPlayed=6), Row(Team='China', TotalMatchesPlayed=4), Row(Team='Canada', TotalMatchesPlayed=4)]
```

```sql
SELECT team AS Team, COUNT(*) AS TotalMatchesPlayed
            FROM (SELECT team1 AS team FROM default.matchesdb_one
                UNION ALL
                SELECT team2 AS team FROM default.matchesdb_one
                UNION ALL
                SELECT team1 AS team FROM default.wwc_matches_2_db
                UNION ALL
                SELECT team2 AS team FROM default.wwc_matches_2_db
                ) AS AllTeams
            GROUP BY Team
            ORDER BY TotalMatchesPlayed DESC;
```

```response from databricks
[Row(Team='Switzerland', TotalMatchesPlayed=9), Row(Team='Germany', TotalMatchesPlayed=9), Row(Team='Netherlands', TotalMatchesPlayed=9), Row(Team='Ivory Coast', TotalMatchesPlayed=9), Row(Team='Australia', TotalMatchesPlayed=9), Row(Team='England', TotalMatchesPlayed=9), Row(Team='Thailand', TotalMatchesPlayed=9), Row(Team='Japan', TotalMatchesPlayed=9), Row(Team='Sweden', TotalMatchesPlayed=9), Row(Team='France', TotalMatchesPlayed=9), Row(Team='USA', TotalMatchesPlayed=9), Row(Team='Nigeria', TotalMatchesPlayed=9), Row(Team='Brazil', TotalMatchesPlayed=9), Row(Team='Cameroon', TotalMatchesPlayed=9), Row(Team='New Zealand', TotalMatchesPlayed=9), Row(Team='Norway', TotalMatchesPlayed=9), Row(Team='Colombia', TotalMatchesPlayed=9), Row(Team='Mexico', TotalMatchesPlayed=9), Row(Team='Spain', TotalMatchesPlayed=9), Row(Team='South Korea', TotalMatchesPlayed=9), Row(Team='Costa Rica', TotalMatchesPlayed=9), Row(Team='Ecuador', TotalMatchesPlayed=9), Row(Team='Canada', TotalMatchesPlayed=6), Row(Team='China', TotalMatchesPlayed=6)]
```

```sql
SELECT team AS Team, COUNT(*) AS TotalMatchesPlayed
            FROM (SELECT team1 AS team FROM default.matchesdb_one
                UNION ALL
                SELECT team2 AS team FROM default.matchesdb_one
                UNION ALL
                SELECT team1 AS team FROM default.wwc_matches_2_db
                UNION ALL
                SELECT team2 AS team FROM default.wwc_matches_2_db
                ) AS AllTeams
            GROUP BY Team
            ORDER BY TotalMatchesPlayed DESC;
```

```response from databricks
[Row(Team='Switzerland', TotalMatchesPlayed=12), Row(Team='Ivory Coast', TotalMatchesPlayed=12), Row(Team='Brazil', TotalMatchesPlayed=12), Row(Team='Germany', TotalMatchesPlayed=12), Row(Team='Costa Rica', TotalMatchesPlayed=12), Row(Team='Australia', TotalMatchesPlayed=12), Row(Team='Cameroon', TotalMatchesPlayed=12), Row(Team='Japan', TotalMatchesPlayed=12), Row(Team='Norway', TotalMatchesPlayed=12), Row(Team='France', TotalMatchesPlayed=12), Row(Team='England', TotalMatchesPlayed=12), Row(Team='Sweden', TotalMatchesPlayed=12), Row(Team='USA', TotalMatchesPlayed=12), Row(Team='Ecuador', TotalMatchesPlayed=12), Row(Team='Mexico', TotalMatchesPlayed=12), Row(Team='South Korea', TotalMatchesPlayed=12), Row(Team='Thailand', TotalMatchesPlayed=12), Row(Team='New Zealand', TotalMatchesPlayed=12), Row(Team='Colombia', TotalMatchesPlayed=12), Row(Team='Nigeria', TotalMatchesPlayed=12), Row(Team='Spain', TotalMatchesPlayed=12), Row(Team='Netherlands', TotalMatchesPlayed=12), Row(Team='China', TotalMatchesPlayed=8), Row(Team='Canada', TotalMatchesPlayed=8)]
```

