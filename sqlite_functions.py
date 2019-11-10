import sqlite3
from helpers import to_bool
#---------------------------------------- ADD FOOD TO SQLite Database ----------------------------------------
def add_food_to_db(database = "food_database.db"): 
    really = to_bool(input("Would you like to add a food to the database? "))
    if really:
        name = input("Food name: ")
        serving = input(f"Basic serving for {name}: ")
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

        sql_connect(database, sqlite_insert_query, data_tuple)
    else: return False

    return name

# ---------------------------------------- GET FOOD FROM SQLITE DATABASE -------------------------------------------------------
def sql_connect(database, command, data_tuple):
    connection = None

    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        print(f'Successfully connected to {database}')
  
        if "INSERT" in command:
            cursor.execute(command, data_tuple)
            connection.commit()

        elif "SELECT" in command:
            cursor.execute(command, (f'%{data_tuple}%',))
            data = cursor.fetchall()

    except Error as e:
        print(e)
    
    if connection:
        connection.close()
        print (f'The SQLite connection is closed')

    return data