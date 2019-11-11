#! Python 3
import datetime, sqlite3

#---------------------------------------- GET FOOD FROM HELLO FRESH------------------------------
def hello_fresh(url):
    import requests
    import urllib.request
    from bs4 import BeautifulSoup

    #year = datetime.date.today().year
    #week = datetime.date.today().isocalendar()[1] + 1

    #url = f'https://www.hellofresh.com/my-account/deliveries/menu/{year}-W{week}'
    #url = "https://www.hellofresh.com/recipes/firecracker-meatballs-5d892f029421962e5476df7b?week=2019-W45"
    response = requests.get(url)
    if response:
        print(response)

    ingredients = []
  
    soup = BeautifulSoup(response.text, "html.parser")
    for each in soup.select('p[class*="dsa dsby"]'):
        ingredients.append(each)
    print(ingredients)

    return ingredients

#---------------------------------------- RENDER VISUAL DEPICTION OF FOOD PLAN ------------------------------
'''
def display_day():
    print(breakfast, lunch, dinner, snacks)
'''
#---------------------------------------- CONVERT ANSWER TO BOOLEAN ------------------------------
def to_bool(answer):
        if answer.lower() == 'y' or answer.lower() == 'yes':
            return True
        else: 
            return False

#---------------------------------------- GET FOOD FROM THE DATABASE ------------------------------
def get_food(name = ""):    
    if name == "":
        name = input("Enter a food name for a search term: ")

    sqlite_select_query = f"""SELECT *
                        FROM food
                        WHERE name LIKE ?;"""

    result = sql_command(sqlite_select_query, name)
    food_item = handle_database_results(result)

    return food_item

# ---------------------------------------- GET RECIPE FROM SQLITE DATABASE -------------------------------------------------------
def get_recipe(database = "food_database.db"):
    name = input("Enter a recipe name to add to the meal: ")
    sqlite_search_query = f"""SELECT * 
                            FROM recipe
                            WHERE name LIKE ?;"""
    result = sql_command(sqlite_search_query, name)
    recipe = handle_database_results(result)

    return recipe

#---------------------------------------- HANDLE FOOD RESULTS FROM DATABASE ------------------------------
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

#---------------------------------------- ASK USER FOR INPUTS ------------------------------
def ask_for_input(meal = [], answer = ''):
    if meal == [] and answer == '':
        answer = input("Add first food: ")
        food_item = get_food(answer)
        if not food_item:
            return ask_for_input(meal)
        else:
            meal.append(food_item)
            return ask_for_input(meal)
    elif answer != '':
        food_item = get_food(answer)
        meal.append(food_item)
        return meal
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

#---------------------------------------- ADD FOOD TO SQLITE DATABASE ----------------------------------------
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
        snacks = to_bool(input("Would you eat this food for a snack? (yes or no): "))
        base = to_bool(input("Would you eat this food by itself? (yes or no): "))
        add_on = to_bool(input("Would you eat this with another food? (example, salsa, butter): "))

        sqlite_insert_query = f"""INSERT INTO food 
                                    ('name', 'serving', 'carbs', 'fat', 'protein', 'fiber', 'breakfast', 'lunch', 'dinner', 'snacks',
                                    'base_food', 'add_on')
                                    VALUES 
                                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (name, serving, carbs, fat, protein, fiber, breakfast, lunch, dinner, snacks, base, add_on)

        sql_command(sqlite_insert_query, data_tuple)
    else: return False

    return name

# -------------------------------- BUILD A RECIPE TO ADD TO THE DATABASE ---------------------------------------
def build_recipe():    
    really = to_bool(input("Would you like to add a new recipe to the database? "))
    if really:
        name = input("Enter a name for the recipe: ")
        serving = input("How many servings in the recipe? ")
        keep_going = True
        ingredient = {}
        i = 0
        while keep_going and i < 11:
            result = get_food()
            if not result:
                get_food()
            else:
                qty = input(f"How much {result[0][1]} ")
                ingredient[i] = [qty, result[0][0]]
                i += 1
                keep_going = to_bool(input("Add another? "))
        print (f"Recipe name: {name}.\n  Servings: {serving}.\n  {ingredient}")
        return [name, serving, ingredient]
    else:
        return False

# ---------------------------------------- ADD RECIPE TO DATABASE -------------------------------------------------------
def add_recipe_to_db():
    results = build_recipe()
    string1 = "'name', 'servings'"
    string2 = "?, ?"
    data = [results[0], int(results[1])]
    ingredient = results[2]

    for key in ingredient:
        string1 += f", 'Ingredient{str(key)}', 'IG{str(key)}Qty'"
        string2 += f", ?, ?"
        data.append(ingredient[key][1])
        data.append(ingredient[key][0])

    data_tuple = tuple(data)

    sqlite_input_statement = f"""INSERT INTO recipe ({string1}) VALUES ({string2});"""
    print(f"Command being sent: {sqlite_input_statement}\nData being sent: {data_tuple}")
    sql_command(sqlite_input_statement, data_tuple)

# ---------------------------------------- EXECUTE A SQLITE DATABASE COMMAND-------------------------------------------------------
def sql_command(command, data_tuple):
    database = "food_database.db"
    connection = None
    data = None

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

    except:
        print("Something went wrong")
        return False
    
    if connection:
        connection.close()
        print (f'The SQLite connection is closed')
        if data:
            return data
        else: 
            return True

add_recipe_to_db()