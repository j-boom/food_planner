import sqlite3

connection = sqlite3.connect("food_database.db")
"""Create a dicitonary of food where the key is the name,
   and the value is a list where each entry is: [basic quantity, carb grams, fat grams, protein grams, fiber]"""

cursor = connection.cursor()

food = {
    'Egg':['1 large', 1/3, 14/3, 19/3, 0, ["Breakfast", "Dinner"]],
    'Kerry Gold': ['1 Tbsp', 0, 12, 0, 0, ["Breakfast", "Lunch", "Dinner", "Snacks"]],
    'Apple, Honeycrisp': ['1 g', 16/112, 0, 0, 4, ["Any"]],
    'Oscar Meyer, Deli Fresh Turkey Breast': ['1 oz', 4/4, 2/4, 18/4, 0, ["Any"]],
    'Kraft Shredded Cheddar': ['1 g', 1/28, 9/28, 6/28, 0, ["Any"]],
    'Hearty Multi-Grain Bread': ['1 oz', 33/2, 1/2, 2/2, 4/2, ["Any"]],
    'Tomatillo Salsa Verde': ['1 serving', 5, 1, 1, 1, ["Any"]],
    'Corn on the Cob': ['1 ear', 19, 1, 3, 2, ["Lunch", "Dinner", "Snacks"]],
    'Plantains, cooked': ['100 g', 31/100, 0, 1/100, 2/100, ["Any"]],
    'Flank Steak': ['1 oz', 0, 20/9.1, 55/9.1, 0, ["Lunch", "Dinner"]],
    'Sweet Potato Pizza Skillet': ['1 serving', 37/1.25, 27/1.25, 22/1.25, 7/1.25, ["Lunch", "Dinner"]],
    'Starkist - Spicy Buffalo Tuna Packet': ['1 pouch', 0, 1, 15, 0, ["Lunch", "Dinner", "Snacks"]],
    'Premier Protein - Chocolate Powder': ['1 scoop', 8, 4, 30, 3, ["Any"]],
    'Jack Links - Original Beef Jerky': ['1 oz', 4/1.2, 1/1.2, 18/1.2, 0, ["Lunch", "Dinner", "Snacks"]],
}

breakfast = False
lunch = False
dinner = False
snacks = False

for key in food:
    last_item = food[key][-1]
    if "breakfast" in last_item:
        breakfast = True
    elif "lunch"in last_item:
        lunch = True
    elif "dinner" in last_item:
        dinner = True
    elif "snacks" in last_item:
        snacks = True
    elif "Any" in last_item:
        breakfast = True
        lunch = True
        dinner = True
        snacks = True

    format_str = """INSERT INTO food (name, serving, carbs, fat, protein, fiber, breakfast, lunch, dinner, snacks) \
    VALUES ({food[key]},{food[key][0]}, {food[key][1]}, {food[key][2]}, {food[key][3]}, {food[key][4]}, {breakfast}, {lunch}, {dinner}, {snacks});"""
    connection.execute(format_str)
    
connection.commit()
print ("Records created successfully")
connection.close()