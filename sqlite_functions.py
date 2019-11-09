import sqlite3

#---------------------------------------- ADD FOOD TO SQLite Database ----------------------------------------

def add_food_to_db(name = ""):

    def to_bool(answer):
        if answer.lower() == 'y' or answer.lower() == 'yes':
            return True
        else: 
            return False

    if name == "":
        name = input("Food name: ")
    serving = input("Basic serving: ")
    carbs = float(input("How many grams of carbs in a serving? "))
    fat = float(input("How many grams of fat in a serving? "))
    protein = float(input("How many grams of protein in a serving? "))
    fiber = float(input("How many grams of fiber in a serving? "))
    breakfast = to_bool(input("Would you eat this food for breakfast? (yes or no): "))
    lunch = to_bool(input("Would you eat this food for lunch? (yes or no): "))
    dinner = to_bool(input("Would you eat this food for dinner? (yes or no): "))
    snacks = to_bool(input("Would you eat this food for a snack? (yes or no):"))

    sqlite_insert_query = f"""INSERT INTO food 
                                ('name', 'serving', 'carbs', 'fat', 'protein', 'fiber', 'breakfast', 'lunch', 'dinner', 'snacks')
                                VALUES 
                                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (name, serving, carbs, fat, protein, fiber, breakfast, lunch, dinner, snacks)
    cursor.execute(sqlite_insert_query, data_tuple)
    connection.commit()
    print ("Records created successfully")

# ---------------------------------------- GET FOOD FROM SQLITE DATABASE -------------------------------------------------------
'''
def get_food(name, database):
    create_connection(database)
    with connection:
        sqlite_insert_query = f"""SELECT *
        FROM food
        WHERE na = ?;"""
        cursor.execute(sqlite_insert_query, (name,))
        data = cursor.fetchone()
        if data is None: 
            add_food_to_db(name)
            get_food(name, database)
        else: 
            return data
    close_connection()
'''
# --------------------------------------- Functions for SQLite Connection -------------------------------------------------------

def create_connection(database):
    connection = None
    try: 
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        print("Successfully connected to SQLite")
        print(type(connection))
    except Error as e:
        print(e)

    return connection, cursor

def close_connection():
    if connection:
        connection.close
        print('The SQLite Connection is closed')


get_food("Apple, honeycrisp", "food_database.db")

def sql_connect(database, command, data_tuple):
    connection = None
    data = ()

    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        print(f'Successfully connected to {database}')
  
        if "INSERT" in command:
            print("INSERT FOUND")
            cursor.execute(command, data_tuple)
            connection.commit()

        elif "SELECT" in command:
            print("SELECT FOUND")
            cursor.execute(command, (f'%{data_tuple}%',))
            data = cursor.fetchall()

    except Error as e:
        print(e)
    
    if connection:
        connection.close()
        print (f'The SQLite conneciton is closed')

    return data