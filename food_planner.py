from helpers import add_food, display_day, add_food_to_db, hello_fresh
import sqlite3, datetime

"""
This is definitely going to be a constraint propagation problem.  Constraints off the top of my head (generalized):
1.  One meal is always a set value. (go to HELLO FRESH and pull down meals).  Ask user to fill in meals otherwise
2.  Must have reasonable amount of food (perhaps set max amount and min amount of food)
3.  Favor my favorites, but provide variety (must flesh out what this means)
4.  Program should add food based on the meal and what's in it (i.e. need carbs and fat, so adds carrots and hummus, or apple and peanut butter, but not broccoli for breakfast)
5.  Meals should be evenly balanced - can't have 80% of food in breakfast - could base on calories (c_g * 4, p_g * 4, f_g * 9)
6.  Sum of all carbs (all 4 meals) must be +/- 5 g, Sum of all protein must be +/- 5g, sum of all fat must be +/- 2g
7.  Breakfast and lunch cannot add food to meals - just adjust quantity.  Can delete foods from a meal.  
8.  Snacks can add food 
"""

hello_fresh(url)

for ingredient in ingredients:
    add_food(ingredient)