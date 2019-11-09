import sqlite3

def to_bool(answer):
        if answer.lower() == 'y' or answer.lower() == 'yes':
            return True
        else: 
            return False

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

def get_food(name = "", database="food_database.db"):    
    if name == "":
        name = input("Enter a food name for a search term: ")

    sqlite_select_query = f"""SELECT *
                        FROM food
                        WHERE name LIKE ?;"""

    result = sql_connect(database, sqlite_select_query, name)
    food_item = handle_database_results(result)

    return food_item

def handle_database_results(database_results):

    if len(database_results) == 0:
        print(f"That wasn't found in the database")
        add_food_to_db()
        return False
    
    elif len(database_results) == 1:
        print(database_results)
        food_item = database_results
        choice = to_bool(input(f"Do you want to use {database_results[0][1]}? "))
        if choice:
            return food_item
        else:
            add_food_to_db()
            return False

    else:
        i = 0
        for each in database_results:
            if i < 10:
                print (f'{i} - {each}')
            i += 1
        
        which_one = input("Which one do you want to use? ")
        if which_one in '0123456789':
            return database_results[int(which_one)]
        else:
            return False

def ask_for_input(meal):
    if meal == []:
        answer = input("Add first food: ")
        food_item = get_food(answer)
        if not food_item:
            return ask_for_input(meal)
        else:
            meal.append(food_item)
            return ask_for_input(meal)
    
    else:
        answer = to_bool(input("Do you want to add another food? "))
        if not answer:
            return meal
        else:
            answer = input("Enter a food name: ")
            food_item = get_food(answer)
            if not food_item:
                return ask_for_input(meal)
            else: 
                meal.append(food_item)
                return ask_for_input(meal)

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
        print (f'The SQLite connection is closed')

    return data

meal = []
food_item = ask_for_input(meal)
print (f"{food_item} Inserted")