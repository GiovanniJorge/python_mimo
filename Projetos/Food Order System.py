# 1. Settings
italian_food = ["pasta bolognese", "pepperoni pizza", "margherita pizza", "lasagna"]
indian_food = ["butter chicken", "chicken tikka masala", "biryani", "samosas"]

# 2. Find meal
def find_meal(name, menu):
  if name in menu:
    return name

# 3. Select meal
def select_meal(name, food_type):
  if food_type == "italian":
    return find_meal(name, italian_food)
  elif food_type == "indian":
    return find_meal(name, indian_food)
  else:
    return None

# 4. Display meals
def display_available_meals(food_type):
  if food_type == "italian":
    print("\nAvailable Italian Meals: ")
    for food in italian_food:
      print(food)
  elif food_type == "indian":
    print("\nAvailable Indian Meals: ")
    for food in indian_food:
      print(food)
  else:
    print("Invalid food type")

# 5. Create summary
def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order:
    return f"\nYou ordered {amount} '{name}'"

# 6. Welcome
print("Welcome to the Food Order System!")
valid = True

# 7. Type of food
while valid:
  type_input = input("\nInsert the type of food that you want: ").lower()
  if type_input == "indian" or type_input == "italian":
    valid = False

# 8. Meal choice
    while True:
      display_available_meals(type_input)
      name_input = input("\nInsert your meal choice: ").lower()
      if name_input == select_meal(name_input, type_input):

# 9. Amount
        amount_input = input("Insert the amount: ")

# 10. Result
        result = create_summary(name_input, amount_input, type_input)
        print(result)
        break
      else:
        print("Meal not found")