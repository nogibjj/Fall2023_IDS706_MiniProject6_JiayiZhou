## Fall2023_IDS706 Mini Project 5: Python Script interacting with SQL Database
### by Jiayi Zhou [![CI](https://github.com/nogibjj/Fall2023_IDS706_MiniProject5_JiayiZhou/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_MiniProject5_JiayiZhou/actions/workflows/cicd.yml)

### Purpose
This is for class data engineering mini project 1. It uses Python Script interacting with SQL Database. It utilizes continuous integration using GitHub Actions to automatically set up environment, test, format and lint code. It also uses an AI Assistant--Copilot to assit the process.

### Functionality
The project does: ETL-Query: [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query For the ETL-Query lab:
  * [E] Extract a dataset from a URL with CSV format.
  * [T] Transform the data by cleaning, filtering, enriching, etc to get it ready for analysis.
  * [L] Load the transformed data into a SQLite database table using Python's sqlite3 module.
  * [Q] Write and execute SQL queries on the SQLite database to analyze and retrieve insights from the data.

### Steps
I created the template based on the template created by Professor Noah Gift and modified the template. Based on the template from professor, I made the following changes:
1. Change the dataset from food market to goose. Goose is from FiveThirtyEight's public dataset. It is extracted into a local csv file, tranfromed the csv file with cleaning, and loaded into a .db file, and queryed with SQLlite.
2. Convert the main.py into a command-line tool
3. Update funcitonalities to extract, transform(update, add, and delete), and load the data
4. Create a sql log to record all the actions performed in the query
5. Create an architectural diagram showing how the project works

### Dataset
The dataset is loaded in based on url.  Here is the url: [(https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv)](https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv). The file is a comma-separated value spreadsheet (CSV) called goose_rawdata.csv.  
<img width="497" alt="Screenshot 2023-09-12 at 10 19 05 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/assets/143651921/ca45cc76-2d2e-4d26-a2b5-6bff9dcaf0ee">

### Check format and error:
Make test, make format, and make lint are run in actions. The commands run smoothly.  
<img width="1118" alt="Screenshot 2023-09-30 at 5 56 36 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject5_JiayiZhou/assets/143651921/4304deed-8fac-43ab-a279-8509c00bd95f">

### Visualization of Process:
![process (3)](https://github.com/nogibjj/Fall2023_IDS706_MiniProject5_JiayiZhou/assets/143651921/f0480b87-bc09-49f4-9d9a-4f483343284c)

