#############################################################################
# This python file was setup to provide more practice with list in Python 3 #
#############################################################################
# I will be using data sources that are apis, databases, and spreadsheets to show real world uses in python. 
# I wiill set up lists using these data sources and then you can use these list to practice different list operations on.
###############
# Spreadsheet #
###############
# Setting up a list from a csv file.
import csv
csvList = []
with open('GDP DATA.csv', mode='r') as file:
    raw_data = csv.reader(file)
    csvList = list(raw_data)
for i in range(0, len(csvList)):
    row = csvList[i]
    for j in range(1,60):
        row.pop(1)
    csvList[i]=row
# Your code here.

############
# Database #
############
# Creating the sqlite database, this will not need to be ran.
# Comment this out after running it the first time.
import sqlite3
dbconn = sqlite3.connect('analysis.db')
dbcur = dbconn.cursor()
try:
    dbcur.execute('''
    CREATE TABLE teachers (
        id int,
        first_name varchar(25),
        last_name varchar(50),
        school varchar(50),
        hire_date date,
        salary numeric
    );
    ''')
    print('Table created!')
    dbcur.execute('''
    INSERT INTO teachers(id, first_name, last_name, school, hire_date, salary)
    VALUES(1,'Janet','Smith','F.D. Roosevelt HS','2011-10-30',36200),
        (2,'Lee','Reynolds','F.D. Roosevelt HS','1993-05-22',65000),
        (3,'Samuel','Cole','Myers Middle School','2005-08-01',43500),
        (4,'Samantha','Bush','Myers Middle School','2011-10-30',36200),
        (5,'Betty','Diaz','Myers Middle School','2005-08-30',43500),
        (6,'Kathleen','Roush','F.D. Roosevelt HS','2010-10-22',38500)
    ''')
    print('Data written!')
    dbconn.commit()
    dbconn.close()
except:
    dbconn.rollback()
# Setting up a list from a database table.
import sqlite3
dbconn = sqlite3.connect('analysis.db')
dbcur = dbconn.cursor()
raw_data = dbcur.execute("SELECT * FROM teachers")
dbList = []
for i in raw_data.fetchall():
    dbList.append(list(i))
dbconn.close()
# Your code here.

#######
# API #
#######
# Setting up a list from an API call.
import requests
steamApiKey = "527ADDFE840218B854DDA41905BB6CA5" # Use you own API key here. One can be obtained from https://steamcommunity.com/dev/apikey.
steamID = "76561199092412457"
url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamApiKey}&steamid={steamID}&include_appinfo=1&format=json"
req = requests.get(url)
steam = req.json()
steam = steam['response']
steam = steam['games']
apiList = []
for i in steam:
    apiList.append(list(i.values()))
# Your code here.o9n