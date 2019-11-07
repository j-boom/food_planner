#! Python 3

import datetime
from sqlite_functions import get_food

#--------------------------------- MANUALLY ADD FOOD BY INGREDIENT TO FRAMEWORK OF MEALS -------------------------------#
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

# ---------------------------------------------------------- GET FOOD FROM HELLOFRESH ------------------------------------
def hello_fresh(url):
    import requests
    import urllib.request
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

    return ingredients

#---------------------------------------- RENDER VISUAL DEPICTION OF FOOD PLAN ------------------------------
def display_day():
    print(breakfast, lunch, dinner, snacks)

# ------------------------------------ Add food to tracker ---------------------------------------------------------------------------------

def add_food_to_tracker(name):
    database = 'food_database.db'
    get_food(name, database)