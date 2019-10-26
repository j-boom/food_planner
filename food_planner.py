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
        


