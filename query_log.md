```sql
SELECT team AS Team, COUNT(*) AS TotalMatchesPlayed FROM (SELECT team1 AS team FROM default.matchesdb_one UNION ALL SELECT team2 AS team FROM default.matchesdb_one UNION ALL SELECT team1 AS team FROM default.wwc_matches_2_db UNION ALL SELECT team2 AS team FROM default.wwc_matches_2_db) AS AllTeams GROUP BY Team ORDER BY TotalMatchesPlayed DESC;
```

```response from databricks
[Row(Team='South Korea', TotalMatchesPlayed=6), Row(Team='Australia', TotalMatchesPlayed=6), Row(Team='Spain', TotalMatchesPlayed=6), Row(Team='Cameroon', TotalMatchesPlayed=6), Row(Team='France', TotalMatchesPlayed=6), Row(Team='Norway', TotalMatchesPlayed=6), Row(Team='Sweden', TotalMatchesPlayed=6), Row(Team='Brazil', TotalMatchesPlayed=6), Row(Team='Costa Rica', TotalMatchesPlayed=6), Row(Team='New Zealand', TotalMatchesPlayed=6), Row(Team='Nigeria', TotalMatchesPlayed=6), Row(Team='Ecuador', TotalMatchesPlayed=6), Row(Team='Colombia', TotalMatchesPlayed=6), Row(Team='Thailand', TotalMatchesPlayed=6), Row(Team='Ivory Coast', TotalMatchesPlayed=6), Row(Team='Netherlands', TotalMatchesPlayed=6), Row(Team='Japan', TotalMatchesPlayed=6), Row(Team='Germany', TotalMatchesPlayed=6), Row(Team='USA', TotalMatchesPlayed=6), Row(Team='Switzerland', TotalMatchesPlayed=6), Row(Team='England', TotalMatchesPlayed=6), Row(Team='Mexico', TotalMatchesPlayed=6), Row(Team='China', TotalMatchesPlayed=4), Row(Team='Canada', TotalMatchesPlayed=4)]
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
[Row(Team='South Korea', TotalMatchesPlayed=9), Row(Team='Ivory Coast', TotalMatchesPlayed=9), Row(Team='New Zealand', TotalMatchesPlayed=9), Row(Team='Switzerland', TotalMatchesPlayed=9), Row(Team='Brazil', TotalMatchesPlayed=9), Row(Team='England', TotalMatchesPlayed=9), Row(Team='Spain', TotalMatchesPlayed=9), Row(Team='Cameroon', TotalMatchesPlayed=9), Row(Team='Norway', TotalMatchesPlayed=9), Row(Team='France', TotalMatchesPlayed=9), Row(Team='Japan', TotalMatchesPlayed=9), Row(Team='Nigeria', TotalMatchesPlayed=9), Row(Team='Mexico', TotalMatchesPlayed=9), Row(Team='Netherlands', TotalMatchesPlayed=9), Row(Team='Thailand', TotalMatchesPlayed=9), Row(Team='Costa Rica', TotalMatchesPlayed=9), Row(Team='Ecuador', TotalMatchesPlayed=9), Row(Team='Colombia', TotalMatchesPlayed=9), Row(Team='USA', TotalMatchesPlayed=9), Row(Team='Germany', TotalMatchesPlayed=9), Row(Team='Australia', TotalMatchesPlayed=9), Row(Team='Sweden', TotalMatchesPlayed=9), Row(Team='China', TotalMatchesPlayed=6), Row(Team='Canada', TotalMatchesPlayed=6)]
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
[Row(Team='South Korea', TotalMatchesPlayed=12), Row(Team='Switzerland', TotalMatchesPlayed=12), Row(Team='New Zealand', TotalMatchesPlayed=12), Row(Team='Germany', TotalMatchesPlayed=12), Row(Team='Netherlands', TotalMatchesPlayed=12), Row(Team='Brazil', TotalMatchesPlayed=12), Row(Team='Japan', TotalMatchesPlayed=12), Row(Team='Costa Rica', TotalMatchesPlayed=12), Row(Team='Australia', TotalMatchesPlayed=12), Row(Team='Cameroon', TotalMatchesPlayed=12), Row(Team='England', TotalMatchesPlayed=12), Row(Team='Spain', TotalMatchesPlayed=12), Row(Team='Colombia', TotalMatchesPlayed=12), Row(Team='Norway', TotalMatchesPlayed=12), Row(Team='France', TotalMatchesPlayed=12), Row(Team='USA', TotalMatchesPlayed=12), Row(Team='Sweden', TotalMatchesPlayed=12), Row(Team='Ivory Coast', TotalMatchesPlayed=12), Row(Team='Ecuador', TotalMatchesPlayed=12), Row(Team='Nigeria', TotalMatchesPlayed=12), Row(Team='Thailand', TotalMatchesPlayed=12), Row(Team='Mexico', TotalMatchesPlayed=12), Row(Team='China', TotalMatchesPlayed=8), Row(Team='Canada', TotalMatchesPlayed=8)]
```

```sql
SELECT team AS Team, COUNT(*) AS TotalMatchesPlayed FROM (SELECT team1 AS team FROM default.matchesdb_one UNION ALL SELECT team2 AS team FROM default.matchesdb_one UNION ALL SELECT team1 AS team FROM default.wwc_matches_2_db UNION ALL SELECT team2 AS team FROM default.wwc_matches_2_db) AS AllTeams GROUP BY Team ORDER BY TotalMatchesPlayed DESC;
```

```response from databricks
[Row(Team='Switzerland', TotalMatchesPlayed=15), Row(Team='Ivory Coast', TotalMatchesPlayed=15), Row(Team='New Zealand', TotalMatchesPlayed=15), Row(Team='Netherlands', TotalMatchesPlayed=15), Row(Team='Japan', TotalMatchesPlayed=15), Row(Team='Costa Rica', TotalMatchesPlayed=15), Row(Team='Australia', TotalMatchesPlayed=15), Row(Team='England', TotalMatchesPlayed=15), Row(Team='Spain', TotalMatchesPlayed=15), Row(Team='South Korea', TotalMatchesPlayed=15), Row(Team='Germany', TotalMatchesPlayed=15), Row(Team='Brazil', TotalMatchesPlayed=15), Row(Team='Cameroon', TotalMatchesPlayed=15), Row(Team='Colombia', TotalMatchesPlayed=15), Row(Team='Norway', TotalMatchesPlayed=15), Row(Team='France', TotalMatchesPlayed=15), Row(Team='Sweden', TotalMatchesPlayed=15), Row(Team='USA', TotalMatchesPlayed=15), Row(Team='Nigeria', TotalMatchesPlayed=15), Row(Team='Ecuador', TotalMatchesPlayed=15), Row(Team='Thailand', TotalMatchesPlayed=15), Row(Team='Mexico', TotalMatchesPlayed=15), Row(Team='Canada', TotalMatchesPlayed=10), Row(Team='China', TotalMatchesPlayed=10)]
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
[Row(Team='Switzerland', TotalMatchesPlayed=18), Row(Team='Ivory Coast', TotalMatchesPlayed=18), Row(Team='New Zealand', TotalMatchesPlayed=18), Row(Team='Germany', TotalMatchesPlayed=18), Row(Team='Netherlands', TotalMatchesPlayed=18), Row(Team='Japan', TotalMatchesPlayed=18), Row(Team='Costa Rica', TotalMatchesPlayed=18), Row(Team='Brazil', TotalMatchesPlayed=18), Row(Team='Australia', TotalMatchesPlayed=18), Row(Team='Cameroon', TotalMatchesPlayed=18), Row(Team='England', TotalMatchesPlayed=18), Row(Team='Spain', TotalMatchesPlayed=18), Row(Team='Colombia', TotalMatchesPlayed=18), Row(Team='France', TotalMatchesPlayed=18), Row(Team='Norway', TotalMatchesPlayed=18), Row(Team='Sweden', TotalMatchesPlayed=18), Row(Team='Ecuador', TotalMatchesPlayed=18), Row(Team='USA', TotalMatchesPlayed=18), Row(Team='Thailand', TotalMatchesPlayed=18), Row(Team='South Korea', TotalMatchesPlayed=18), Row(Team='Nigeria', TotalMatchesPlayed=18), Row(Team='Mexico', TotalMatchesPlayed=18), Row(Team='Canada', TotalMatchesPlayed=12), Row(Team='China', TotalMatchesPlayed=12)]
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
[Row(Team='Switzerland', TotalMatchesPlayed=21), Row(Team='Ivory Coast', TotalMatchesPlayed=21), Row(Team='New Zealand', TotalMatchesPlayed=21), Row(Team='Germany', TotalMatchesPlayed=21), Row(Team='South Korea', TotalMatchesPlayed=21), Row(Team='Netherlands', TotalMatchesPlayed=21), Row(Team='Brazil', TotalMatchesPlayed=21), Row(Team='Australia', TotalMatchesPlayed=21), Row(Team='Japan', TotalMatchesPlayed=21), Row(Team='Thailand', TotalMatchesPlayed=21), Row(Team='Costa Rica', TotalMatchesPlayed=21), Row(Team='Spain', TotalMatchesPlayed=21), Row(Team='Cameroon', TotalMatchesPlayed=21), Row(Team='England', TotalMatchesPlayed=21), Row(Team='France', TotalMatchesPlayed=21), Row(Team='Colombia', TotalMatchesPlayed=21), Row(Team='Norway', TotalMatchesPlayed=21), Row(Team='Sweden', TotalMatchesPlayed=21), Row(Team='USA', TotalMatchesPlayed=21), Row(Team='Ecuador', TotalMatchesPlayed=21), Row(Team='Mexico', TotalMatchesPlayed=21), Row(Team='Nigeria', TotalMatchesPlayed=21), Row(Team='China', TotalMatchesPlayed=14), Row(Team='Canada', TotalMatchesPlayed=14)]
```

