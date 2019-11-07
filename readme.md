# This is my readme file.

The purpose of this project is to create a food planner that, given the goals for the daily macro counts in a week, and a set of planned dinners,
Will return a macro-balanced food plan and grocery list.

## SQLite Database Construct:

|Index | Name | Base Serving | Carbs (g) | Fat (g) | Protein (g) | Fiber (g) | Breakfast | Lunch | Dinner | Snacks | Last Used | Times Logged |
|------|------|--------------|-----------|---------|-------------|-----------|-----------|-------|--------|--------|-----------|--------------|
|INT|TEXT|TEXT|REAL|REAL|REAL|REAL|BOOL|BOOL|BOOL|BOOL|TEXT|INT|

## Problem Table:

| MEAL | Food | Quantity | CARBS | FAT | PROTEIN | FIBER|
|------|------|----------|-------|-----|---------|------|
|Breakfast| blank | blank | SUM(BREAKFAST_CARBS)| SUM(BREAKFAST_FAT)|SUM(BREAKFAST_PROTEIN)| SUM(BREAKFAST_FIBER)|
|food 1    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food 2    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food 3    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food n    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|Lunch| blank | blank | SUM(LUNCH_CARBS)| SUM(LUNCH_FAT)|SUM(LUNCH_PROTEIN)| SUM(LUNCH_FIBER)|
|food 1    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food 2    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food 3    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food n    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|Dinner| blank | blank | SUM(Dinner_CARBS)| SUM(Dinner_FAT)|SUM(Dinner_PROTEIN)| SUM(Dinner_FIBER)|
|food 1    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food 2    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food 3    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food n    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|Snacks| blank | blank | SUM(Snacks_CARBS)| SUM(Snacks_FAT)|SUM(Snacks_PROTEIN)| SUM(Snacks_FIBER)|
|food 1    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food 2    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food 3    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|
|food n    | name  |  var(qty) | base serv * qty carbs| base serv * qty fat| base serv * qty protein| base serv * qty fiber|

## Constraints for constraint propagation problem
This is definitely going to be a constraint propagation problem.  Constraints off the top of my head (generalized):
1.  One meal is always a set value. (go to HELLO FRESH and pull down meals).  Ask user to fill in meals otherwise
2.  Must have reasonable amount of food (perhaps set max amount and min amount of food)
3.  Favor my favorites, but provide variety (must flesh out what this means)
4.  Program should add food based on the meal and what's in it (i.e. need carbs and fat, so adds carrots and hummus, or apple and peanut butter, but not broccoli for breakfast)
5.  Meals should be evenly balanced - can't have 80% of food in breakfast - could base on calories (c_g * 4, p_g * 4, f_g * 9)
6.  Sum of all carbs (all 4 meals) must be +/- 5 g, Sum of all protein must be +/- 5g, sum of all fat must be +/- 2g
7.  Breakfast and lunch cannot add food to meals - just adjust quantity.  Can delete foods from a meal.  
8.  Snacks can add food 

## Plain language logic for functionality.

1. Choose dinner.
2. Populate dinner foods into meal container.
3. Select a daily breakfast and lunch (building blocks)
4. Use constraint propagation to create snacks and quantities in other meals.  
5. Display proposed meal by day
6. Get user feedback for meals (future functionality - incorporate user feedback into decision logic.  Future functionality, recognize that 2 pieces of bread + meat is a sandwich, and eggs, bacon and tortilla is a breakfast taco, etc.)
7. Generate a shopping list