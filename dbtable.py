import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    username='root',
    password='India@2021'
)
# ********************CREATING A TABLE ********************
# connection = database.cursor()
# selectdb = 'use bus_booking'
# connection.execute(selectdb)
# tableCreationQuery = '''
#     create table passenger(
#         id int primary key auto_increment,
#         name varchar(50),
#         age int,
#         destination varchar(50))
# '''
# connection.execute(tableCreationQuery)

# ************* DESCRIBING A TABLE ***************
# connection = database.cursor()
# selectdb = 'use bus_booking'
# connection.execute(selectdb)
# describeTable = 'desc passenger'
# connection.execute(describeTable)
# for row in connection:
#     print(row)

# ******* INSERTING VALUES IN TABLE ************

# connection = database.cursor()
# selectdb = 'use bus_booking'
# connection.execute(selectdb)
# insertQuery = '''
#     insert into passenger(name , age, destination)
#     values (%s,%s, %s)
# '''
#
#
# insertValues = [
#     ("Ram", 23, "Delhi"),
#     ("Shyam", 22, "Bihar"),
#     ("Abhishek", 24, "Raipur")
# ]
#
# connection.executemany(insertQuery, insertValues)
# database.commit()
# database.close()

# ******** Inserting multiple values **********
# connection = database.cursor()
# selectdb = 'use bus_booking'
# connection.execute(selectdb)
# inputValues = []
# while True:
#     value = tuple(input('Enter "name age destination" for passenger: ').split())
#     name, age, destination = value[0], int(value[1]), value[2]
#     inputValue = (name, age, destination)
#     inputValues.append(inputValue)
#     isMore = input('Want to give more ? (yes/no) ')
#     if isMore == 'no':
#         break
#
# insertQuery = '''
#     insert into passenger(name , age, destination)
#     values (%s,%s, %s)
# '''
# connection.executemany(insertQuery, inputValues)
# database.commit()
# database.close()

# ********** SELECTING VALUE **********

connection = database.cursor()
selectdb = 'use bus_booking'
connection.execute(selectdb)

selectQuery = '''
    select * from passenger
'''
connection.execute(selectQuery)
for rows in connection:
    print(rows)
database.close()


