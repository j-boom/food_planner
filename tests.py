import sqlite3


def sql_command(database, function):
    connection = None
    try: 
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        print("Successfully connected to SQLite")
        function
        cursor.execute(sqlite_query, data_tuple)

    except Error as e:
        print(e)

    return connection, cursor

def to_bool(answer):
        if answer.lower() == 'y' or answer.lower() == 'yes':
            return True
        else: 
            return False

def add_food_to_db(connection, cursor): 
    really = to_bool(input("Do you want to add a food to the database? "))
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

        cursor.execute(sqlite_insert_query, data_tuple)
        connection.commit()
        return True

    else:
        return False


def get_food(name, database):
    connection = None
    data = []

    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        print("Successfully connected to SQLite")

    except Error as e:
        print(e)    
        
    sqlite_insert_query = f"""SELECT *
                        FROM food
                        WHERE name LIKE ?;"""
    cursor.execute(sqlite_insert_query, (f'%{name}%',))
    data = cursor.fetchall()

    if len(data) == 0:
        print(f"{name} not found in database") 
        if not add_food_to_db(connection, cursor):
            print("Try again")
            return False
    
    elif name != data[0][1] and len(data) == 1:
        similar = to_bool(input(f"Do you want to use {data[0][1]}? "))
        if similar:
            data = data[0]
            return data
        else:
            similar = to_bool(input(f'Would you like to search again? '))
            if similar:
                new_name = input("Enter the name of the food you would like to search: ")
                get_food(new_name, database)
            else:
                if not add_food_to_db(connection, cursor):
                    return False
                else:
                    get_food(name, database)
    else:
        cursor.execute(sqlite_insert_query, (f'%{name}%',))
        data = cursor.fetchall()
        i = 0
        for each in data:
            if i < 10:
                print (f'{i} - {each}')
            i += 1
        which_one = input('Which one do you want to use? Select an option, or type "none" if none of these: ')

        if which_one in "0123456789":
            return data[int(which_one)]
        else:
            if not add_food_to_db(connection, cursor):
                return False
            else: get_food(name, database)

    if connection:
        connection.close
        print('The SQLite Connection is closed')


meal_item = get_food("Ground Beef", "food_database.db")

print(meal_item)