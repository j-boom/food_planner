

#---------------------------------- CLASS DEFINITIONS ------------------------------------------#
class Error(Exception):
    """Base Class for other exceptions"""
    pass

class WrongMeal(Error):
    """Raised when user didn't input the correct meal name"""
    pass

class Food:
    def __init__(self, name, protein, carbs, fat, fiber, sugar):
        self.name = name
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.sugar = sugar
        self.meals = []
        self.genres = []
        
    def __repr__(self):
        return f"{self.name} has {self.protein} grams of protein, {self.carbs} grams of carbs, and {self.fat} grams of fat"

    def add_food(self, name, protein, carbs, fat, fiber, sugar):
        pass
#--------------------------------- ADD FOOD TO FRAMEWORK OF MEALS -------------------------------#
def add_food(breakfast, lunch, dinner, snacks):
    food = input("Enter a food: ")
    meal = int(input("Which meal does it go in? 1: breakfast, 2: lunch, 3: dinner, 4: snacks "))
    
    if meal == 1:
        breakfast.append(food)
    elif meal == 2:
        lunch.append(food)
    elif meal == 3:
        dinner.append(food)
    else:
        snacks.append(food)
    
    multiple()

    def multiple():
        multiple = input("Do you want to add another? (y/n): ")
        if multiple in 'yn':
            if multiple == 'y':
                add_food(breakfast, lunch, dinner, snacks)
            elif multiple == 'n':
                pass
            else:
                print("Try again: ")
                multiple()        

    return breakfast, lunch, dinner, snacks


#---------------------------------------- RENDER VISUAL DEPICTION OF FOOD PLAN ------------------------------
def display_day():
    print(breakfast, lunch, dinner, snacks)


#---------------------------------------- ADD FOOD TO SQLite Database ----------------------------------------

def add_food_to_db():
    import sqlite3

    def to_bool(answer):
        if answer.lower() == 'y' or answer.lower() == 'yes':
            return True
        else: 
            return False

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

    try:
        connection = sqlite3.connect("food_database.db")
        cursor = connection.cursor()
        print("Successfully connected to SQlite")

        sqlite_insert_query = f"""INSERT INTO food 
                                    ('name', 'serving', 'carbs', 'fat', 'protein', 'fiber', 'breakfast', 'lunch', 'dinner', 'snacks')
                                    VALUES 
                                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (name, serving, carbs, fat, protein, fiber, breakfast, lunch, dinner, snacks)
        cursor.execute(sqlite_insert_query, data_tuple)
        connection.commit()
        print ("Records created successfully")

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table: ", error)

    finally:
        if connection:
            connection.close()
            print("The SQLite connection is closed")  

# ------------------------------------------------------------ Add Food --------------------------------------------------

# ---------------------------------------------------------- GET FOOD FROM HELLOFRESH ------------------------------------
def hello_fresh(url):
    import requests
    import urllib.request
    import datetime
    from bs4 import BeautifulSoup

    year = datetime.date.today().year
    week = datetime.date.today().isocalendar()[1] + 1

    #url = f'https://www.hellofresh.com/my-account/deliveries/menu/{year}-W{week}'
    #url = "https://www.hellofresh.com/recipes/firecracker-meatballs-5d892f029421962e5476df7b?week=2019-W45"
    response = requests.get(url)

    ingredients = []
  
    soup = BeautifulSoup(response.text, "html.parser")
    for each in soup.select('p[class*="dsa dsbv dshm"]'):
        ingredients.append(each)
    print(ingredients)

hello_fresh("https://www.hellofresh.com/recipes/firecracker-meatballs-5d892f029421962e5476df7b?week=2019-W45")