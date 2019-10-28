food = {
    'Egg':['1 large', 1/3, 14/3, 19/3, 0, ["Breakfast", "Dinner"]],
    'Kerry Gold': ['1 Tbsp', 0, 12, 0, 0, ["Breakfast", "Lunch", "Dinner", "Snacks"]],
    'Apple, Honeycrisp': ['1 g', 16/112, 0, 0, 4, ["Any"]]
}

print(food['Egg'])
print(food['Egg'][-1])
print(food['Egg'][0])

def to_bool(answer):
        if answer.lower() == 'y' or answer.lower() == 'yes':
            return True
        else: 
            return False

breakfast = to_bool(input("Would you eat this for breakfast?  "))

print(breakfast)