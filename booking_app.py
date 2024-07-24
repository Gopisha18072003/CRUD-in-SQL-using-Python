import mysql.connector
from datetime import datetime
from prettytable import PrettyTable

database = mysql.connector.connect(
    host='localhost',
    username='root',
    password='India@2021'
)

connection = database.cursor()
selectdb = 'use bus_booking'
connection.execute(selectdb)

connection = database.cursor()
# createTable = '''create table bookings
#                 (id int primary key auto_increment,
#                 name varchar(50),
#                 age int,
#                 noOfBookings int,
#                 dateOfBooking date,
#                 price int )'''
# connection.execute(createTable)


noOfSeats = 50
while True:

    choice = int(input('''
    1. Seat availability
    2. Booking portal
    3. Show all bookings
    4. Update booking details
    5. Cancel Booking
    6. Exit
    
    '''))
    if choice == 1:
        connection = database.cursor()
        sumQuery = 'SELECT SUM(noOfBookings) from bookings'
        connection.execute(sumQuery)
        totalBookings = connection.fetchone()
        if totalBookings[0]:
            print('Number of available seats: ', noOfSeats - totalBookings[0])
        else:
            print('Number of available seats: ', noOfSeats)
    elif choice == 2:
        connection = database.cursor()
        print('Enter your details')
        name = input('Name: ')
        age = int(input('Age: '))
        noOfBookings = int(input('Number of bookings: '))
        dateOfBooking = datetime.now().date()
        price = noOfBookings * 1500

        # Apply discount if age is greater than 60
        if age > 60:
            price -= 750

        # Prepare values and SQL query
        insertValue = [(name, age, noOfBookings, dateOfBooking, price)]
        insertQuery = '''
            INSERT INTO bookings(name, age, noOfBookings, dateOfBooking, price)
            VALUES (%s, %s, %s, %s, %s)
        '''

        # Execute the insert query
        connection.executemany(insertQuery, insertValue)

        # Get the ID of the last inserted row
        passengerId = connection.lastrowid

        # Commit the changes
        database.commit()

        # Print success message and booking ID
        print('Booking Successfully!')
        print('Your Booking ID is:', passengerId)

    elif choice == 3:
        connection = database.cursor()
        table = PrettyTable()
        table.field_names = ["Id", "Name", "Age", "Bookings", "Date", "Price"]
        selectQuery = 'select * from bookings'
        connection.execute(selectQuery)
        for row in connection:
            table.add_row(row)
        print(table)

    elif choice == 4:
        connection = database.cursor()
        passengerId = int(input('Enter your Id: '))
        checkId = 'select * from bookings where id = %s'
        connection.execute(checkId, (passengerId,))
        passenger = connection.fetchone()
        if passenger:
            newNoOfBookings = int(input('New Number of Bookings: '))
            searchOne = 'SELECT noOfBookings from bookings where id = %s'
            connection.execute(searchOne, (passengerId, ))
            previousBooking = connection.fetchone()
            additionalPrice = (newNoOfBookings-previousBooking[0]) * 1500
            updateQuery = 'UPDATE bookings SET noOfBookings = %s, price = price + %s WHERE id = %s'
            connection.execute(updateQuery, (newNoOfBookings, additionalPrice, passengerId))
            database.commit()
            print('Updation Successfully')
        else:
            print("No record found with ID:", passengerId)

    elif choice == 5:
        connection = database.cursor()
        passengerId = int(input('Enter your Id: '))

        # Check if the record exists
        checkId = 'SELECT * FROM bookings WHERE id = %s'
        connection.execute(checkId, (passengerId,))
        passenger = connection.fetchone()

        if passenger:
            # Record exists, proceed with deletion
            deleteQuery = 'DELETE FROM bookings WHERE id = %s'
            connection.execute(deleteQuery, (passengerId,))

            # Commit the changes
            database.commit()

            print("Booking cancelled successfully.")
        else:
            # Record does not exist
            print("No record found with ID:", passengerId)

    else:
        break










