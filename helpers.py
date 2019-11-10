#! Python 3

import datetime
from sqlite_functions import sql_connect, add_food_to_db

'''#--------------------------------- MANUALLY ADD FOOD BY INGREDIENT TO FRAMEWORK OF MEALS -------------------------------#
def add_food_by_ingredient(breakfast, lunch, dinner, snacks):
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
'''
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
    for each in soup.select('p[class*="dsa "]'):
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
def get_food(name = "", database="food_database.db"):    
    if name == "":
        name = input("Enter a food name for a search term: ")

    sqlite_select_query = f"""SELECT *
                        FROM food
                        WHERE name LIKE ?;"""

    result = sql_connect(database, sqlite_select_query, name)
    food_item = handle_database_results(result)

    return food_item

#---------------------------------------- HANDLE RESULTS FROM DATABASE ------------------------------
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
def ask_for_input(meal, answer = ''):
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
