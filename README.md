## Fall2023_IDS706 Mini Project 6: Complex SQL Query for a MySQL Database
### by Jiayi Zhou [![CI](https://github.com/nogibjj/Fall2023_IDS706_MiniProject6_JiayiZhou/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_MiniProject6_JiayiZhou/actions/workflows/cicd.yml)

### Purpose
This is for class data engineering mini project 6. It uses Python Script interacting with SQL Database on Azure Databricks. It utilizes continuous integration using GitHub Actions to automatically set up environment, test, format and lint code.

### Functionality
The project does: ETL-Query: [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query For the ETL-Query lab:
  * [E] Extract a dataset from a URL with CSV format.
  * [T] Transform the data by cleaning, filtering to get it ready for analysis.
  * [L] Load the transformed data into a cloud database with Azure Databricks.
  * [Q] Write and execute a complex SQL query involving joins, aggregation, and sorting on Azure Databricks to analyze and retrieve insights from the data.

### Steps
I created the template based on mini project 5 and modified the template. Based on the template, I made the following changes:
1. Change the dataset from goose to women world cup. Women world cup is from FiveThirtyEight's public dataset. It is extracted into a local csv file, tranfromed the csv file with cleaning, and loaded into a .db file, and queryed with Azure Databricks.
2. Convert the main.py into a command-line tool
3. Update funcitonalities to extract, transform(add dataset), load, and query the data
4. Create a sql log to record all the actions performed in the query
5. Create an architectural diagram showing how the project works

### Query
This query accomplishes the following using a combination of subqueries, unions, aggregation, and sorting:
  * Unions (Combining Data): The query combines data from four different sources (tables) into a single derived table called "AllTeams." It does this by using UNION ALL to concatenate the team names from two tables, "default.matchesdb_one" (both from the team1 and team2 columns), and "default.wwc_matches_2_db" (again from both team1 and team2 columns). This effectively creates a list of all teams that participated in matches from both tables.
  * Aggregation: After the data is combined, the query performs aggregation. It uses the GROUP BY clause to group the concatenated team names (aliased as "Team") and calculates the count of rows (matches) associated with each unique team name using COUNT(*). This count represents the total number of matches played by each team.
  * Sorting: The results are then sorted using the ORDER BY clause. The sorting is done based on the TotalMatchesPlayed column (aliased as "TotalMatchesPlayed") in descending order. This means that the team with the most matches played will appear first in the result set, followed by teams with fewer matches.

### Result of query
<img width="342" alt="Screenshot 2023-10-07 at 7 04 42 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject6_JiayiZhou/assets/143651921/83763113-bc5b-429e-9d94-c2773849174f">

### Check format and error:
Make test, make format, and make lint are run in actions. The commands run smoothly.  


### Visualization of Process:
![Miniproject6](https://github.com/nogibjj/Fall2023_IDS706_MiniProject6_JiayiZhou/assets/143651921/4e028eb0-692d-4399-b865-2be4df73e2f4)



