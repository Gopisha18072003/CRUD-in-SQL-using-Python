import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    username='root',
    password='India@2021'
)

connection = database.cursor()
# save query in a variable and then execute
# databaseCreationQuery = 'CREATE DATABASE bus_booking'
# connection.execute(databaseCreationQuery)
displayingDatabaseQuery = 'SHOW DATABASES'
connection.execute(displayingDatabaseQuery)

for databases in connection:
    print(databases)

connection = database.cursor()

database.close()