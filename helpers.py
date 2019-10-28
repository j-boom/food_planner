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